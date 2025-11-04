import functions_framework
import requests
import os
import json
from dotenv import load_dotenv
from google.cloud import storage
import pandas as pd
from io import StringIO
from datetime import datetime, timedelta


from logging_config import get_logger

logger = get_logger(__name__)

@functions_framework.http
def hello_get(request):
    """HTTP Cloud Function to fetch and store historical data from Upstox."""
    load_dotenv()
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    bucket_name = os.getenv("bucket_name")

    if not client_id or not client_secret or not bucket_name:
        print("Error: client_id, client_secret, or bucket_name not set in environment variables.")
        return {"error": "Missing environment variables"}, 500

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)


    upstox_auth_code = os.getenv("UPSTOX_AUTH_CODE")
    if not upstox_auth_code:
        return {"error": "UPSTOX_AUTH_CODE environment variable is required"}, 500
    base_url = "https://api.upstox.com/v2/historical-candle"
    symbol = os.getenv("UPSTOX_SYMBOL", "NSE_EQ|INE002A01018")
    interval = os.getenv("UPSTOX_INTERVAL", "30minute")
    to_date = os.getenv("UPSTOX_TO_DATE", "2024-12-19")
    from_date = os.getenv("UPSTOX_FROM_DATE", "2023-06-01")

    # Construct the full URL
    url = f"{base_url}/{symbol}/{interval}/{to_date}/{from_date}"

    # Define headers
    headers = {
        "Accept": "application/json"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # --- Data Processing and Storage ---
    
    return response.json()

