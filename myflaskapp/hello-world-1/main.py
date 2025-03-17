import functions_framework
import os
import json
from dotenv import load_dotenv
from google.cloud import storage
import requests
from datetime import datetime

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
bucket_name = os.getenv("BUCKET")

def transform_upstox_data(data, symbol):
    """
    Transforms Upstox candle data into a format suitable for BigQuery.

    Args:
        data: A list of lists (array of arrays) representing Upstox candle data.
        symbol: The stock symbol (e.g., "NSE_EQ|INE002A01018").

    Returns:
        A string where each line is a JSON object representing a row for BigQuery.
    """
    bq_data = []
    for candle in data:
        # Parse the timestamp string into a datetime object
        timestamp_str = candle[0]
        timestamp = datetime.fromisoformat(timestamp_str)

        bq_data.append({
            "timestamp": timestamp.isoformat(),  # Convert back to ISO 8601 string (without timezone)
            "open": float(candle[1]),
            "high": float(candle[2]),
            "low": float(candle[3]),
            "close": float(candle[4]),
            "volume": int(candle[5]),
            "unknown": int(candle[6]),
            "symbol": symbol,
        })

    # Create a string with JSON objects on separate lines
    json_lines = "\n".join([json.dumps(row) for row in bq_data])
    return json_lines

@functions_framework.http
def check_gcs_connection(request):
    """HTTP Cloud Function to check GCS connection and upload a test JSON object."""
    file_name = 'stock.json'
    try:
        bucket_name = os.getenv("BUCKET")
        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
        # 1. Connect to Cloud Storage
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        url = "https://api.upstox.com/v2/login/authorization/token"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Define the payload (data to be sent in the POST request)
        payload = {
            "code": "TCVbsY",
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": "https://google.com",
            "grant_type": "authorization_code"
        }

        # Make the POST request
        response = requests.post(url, headers=headers, data=payload)
        #access_token = response.json()['access_token']
        base_url = "https://api.upstox.com/v2/historical-candle"
        symbol = "NSE_EQ|INE002A01018"          # Replace with actual symbol
        interval = "30minute"          # Replace with desired interval (e.g., '1min', '1day')
        to_date = "2025-03-16"     # Replace with the desired end date
        from_date = "2023-06-01"   # Replace with the desired start date
        request_json = request.get_json(silent=True)
        request_args = request.args

        if request_json and 'symbol' in request_json and 'interval' in request_json and 'to_date' in request_json and 'from_date' in request_json:
            symbol = request_json['symbol']
            interval = request_json['interval']
            to_date = request_json['to_date']
            from_date = request_json['from_date']
        elif request_args and 'symbol' in request_args and 'interval' in request_args and 'to_date' in request_args and 'from_date' in request_args:
            symbol = request_args['symbol']
            interval = request_args['interval']
            to_date = request_args['to_date']
            from_date = request_args['from_date']
        # Construct the full URL
        url = f"{base_url}/{symbol}/{interval}/{to_date}/{from_date}"

        # Define headers
        headers = {
            "Accept": "application/json"
        }

        # Make the GET request
        data = requests.get(url, headers=headers)
        json_data = data.json()
        transformed_data = transform_upstox_data(json_data['data']['candles'], symbol)

        # Upload the JSON string with the correct content type
        blob.upload_from_string(transformed_data, content_type='application/json')

        return f"Successfully uploaded test JSON to gs://{bucket_name}/{file_name}"

    except Exception as e:
        return f"Error: {e}", 500
