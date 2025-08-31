import json
import os
from datetime import datetime

import functions_framework
import requests
from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
bucket_name = os.getenv("BUCKET")
upstox_auth_code = os.getenv("UPSTOX_AUTH_CODE")

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
        # Ensure all required environment variables are loaded
        if not all([client_id, client_secret, bucket_name, upstox_auth_code]):
            missing_vars = [var_name for var_name, var_val in [("client_id", client_id), ("client_secret", client_secret), ("BUCKET", bucket_name), ("UPSTOX_AUTH_CODE", upstox_auth_code)] if not var_val]
            return f"Error: Missing environment variables: {', '.join(missing_vars)}", 500

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
            "code": upstox_auth_code, # Replaced hardcoded value
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": "https://google.com", # This might also need to be configurable
            "grant_type": "authorization_code"
        }

        # Make the POST request
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status() # Raise an exception for HTTP errors

        # It's good practice to get the access token if the above call is successful
        # access_token = response.json().get('access_token')
        # if not access_token:
        #     return "Error: Could not retrieve access token from Upstox.", 500

        base_url = "https://api.upstox.com/v2/historical-candle"
        symbol = "NSE_EQ|INE002A01018"
        interval = "30minute"
        to_date = "2025-03-30"
        from_date = "2023-06-01"
        request_json = request.get_json(silent=True)
        request_args = request.args

        if request_json:
            symbol = request_json.get('symbol', symbol)
            interval = request_json.get('interval', interval)
            to_date = request_json.get('to_date', to_date)
            from_date = request_json.get('from_date', from_date)
        elif request_args:
            symbol = request_args.get('symbol', symbol)
            interval = request_args.get('interval', interval)
            to_date = request_args.get('to_date', to_date)
            from_date = request_args.get('from_date', from_date)

        # Construct the full URL
        # This part of the code seems to fetch historical data without using the access token obtained above.
        # This might be an issue with the original logic or Upstox API requirements.
        # For now, I'm keeping the logic as is, but it's worth noting.
        data_fetch_url = f"{base_url}/{symbol}/{interval}/{to_date}/{from_date}"

        # Define headers for data fetching (might need Authorization header with access_token)
        data_headers = {
            "Accept": "application/json"
            # "Authorization": f"Bearer {access_token}" # Potentially needed
        }

        # Make the GET request
        data_response = requests.get(data_fetch_url, headers=data_headers)
        data_response.raise_for_status()
        json_data = data_response.json()

        candles = json_data.get('data', {}).get('candles')
        if candles is None:
            return "Error: 'candles' not found in Upstox API response.", 500

        transformed_data = transform_upstox_data(candles, symbol)

        # Upload the JSON string with the correct content type
        blob.upload_from_string(transformed_data, content_type='application/jsonl') # Using jsonl for line-delimited JSON

        return f"Successfully uploaded data to gs://{bucket_name}/{file_name}"

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - Response: {http_err.response.text}", getattr(http_err.response, 'status_code', 500)
    except Exception as e:
        return f"An unexpected error occurred: {e}", 500
