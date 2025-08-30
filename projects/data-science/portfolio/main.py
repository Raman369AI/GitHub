import functions_framework
import requests
import os
import json
from dotenv import load_dotenv
from google.cloud import storage
import pandas as pd
from io import StringIO
from datetime import datetime, timedelta

@functions_framework.http
def hello_get(request):
    """HTTP Cloud Function to fetch and store historical data from Upstox."""
    load_dotenv()
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    bucket_name = os.getenv("bucket_name")
    # UPSTOX_AUTH_CODE should be a temporary authorization code from the Upstox login flow.
    # This code is used to obtain an access token.
    upstox_auth_code = os.getenv("UPSTOX_AUTH_CODE")

    if not all([client_id, client_secret, bucket_name, upstox_auth_code]):
        missing_vars = [
            var_name for var_name, var_val in [
                ("client_id", client_id),
                ("client_secret", client_secret),
                ("bucket_name", bucket_name),
                ("UPSTOX_AUTH_CODE", upstox_auth_code)
            ] if not var_val
        ]
        print(f"Error: Missing environment variables: {', '.join(missing_vars)}")
        return {"error": f"Missing environment variables: {', '.join(missing_vars)}"}, 500

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # NOTE: The original code mentioned 'code = "1UL15m"' was a mock and likely to fail.
    # The proper flow usually involves:
    # 1. Using the 'upstox_auth_code' (obtained via user login redirect) to get an access token.
    # 2. Using the access token in the Authorization header for subsequent API calls.
    # The historical-candle endpoint might not require the auth code directly,
    # but rather an access token obtained using that code.
    # For now, I am keeping the direct call to historical-candle as per original structure,
    # but this might need adjustment based on Upstox API's exact auth flow for this endpoint.

    # Step 1: Get Access Token (Illustrative - actual implementation might vary)
    # token_url = "https://api.upstox.com/v2/login/authorization/token"
    # token_payload = {
    #     "code": upstox_auth_code,
    #     "client_id": client_id,
    #     "client_secret": client_secret,
    #     "redirect_uri": os.getenv("UPSTOX_REDIRECT_URI"), # This should also be an env var
    #     "grant_type": "authorization_code"
    # }
    # token_headers = {
    #     "accept": "application/json",
    #     "Content-Type": "application/x-www-form-urlencoded"
    # }
    # try:
    #     token_response = requests.post(token_url, headers=token_headers, data=token_payload)
    #     token_response.raise_for_status()
    #     access_token = token_response.json().get("access_token")
    #     if not access_token:
    #         print("Error: Could not retrieve access token from Upstox.")
    #         return {"error": "Could not retrieve access token"}, 500
    # except requests.exceptions.RequestException as e:
    #     print(f"Error obtaining access token: {e}")
    #     return {"error": f"Failed to obtain access token: {e}"}, 500

    # Step 2: Fetch Historical Data
    base_url = "https://api.upstox.com/v2/historical-candle"
    # Default values, can be overridden by request parameters
    symbol = request.args.get("symbol", "NSE_EQ|INE002A01018")
    interval = request.args.get("interval", "30minute")
    to_date = request.args.get("to_date", datetime.now().strftime('%Y-%m-%d'))
    from_date_default = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    from_date = request.args.get("from_date", from_date_default)

    # Construct the full URL
    data_url = f"{base_url}/{symbol}/{interval}/{to_date}/{from_date}"

    # Define headers for data fetching
    # If an access token is required, it should be included here.
    data_headers = {
        "Accept": "application/json"
        # "Authorization": f"Bearer {access_token}" # Add if token is obtained and required
    }

    try:
        # Make the GET request
        response = requests.get(data_url, headers=data_headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        # --- Data Processing and Storage (Example: save to GCS) ---
        # file_name = f"{symbol}_{from_date}_{to_date}_{interval}.json"
        # blob = bucket.blob(file_name)
        # blob.upload_from_string(json.dumps(response.json()), content_type='application/json')
        # print(f"Data uploaded to GCS: gs://{bucket_name}/{file_name}")

        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Response: {http_err.response.text}")
        return {"error": f"HTTP error: {http_err.response.text}"}, getattr(http_err.response, 'status_code', 500)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": f"An unexpected error occurred: {e}"}, 500
