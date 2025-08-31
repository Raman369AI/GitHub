# Upstox Data Fetcher - Hello World

A Google Cloud Function that fetches historical stock data from Upstox API and stores it in Google Cloud Storage.

## Features

- Fetches historical candle data from Upstox API
- Transforms data for BigQuery compatibility
- Stores data in Google Cloud Storage as JSONL format
- Configurable via environment variables

## Setup

1. Install dependencies:
```bash
pip install -r config/requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Required Environment Variables:
- `client_id`: Upstox API client ID
- `client_secret`: Upstox API client secret
- `UPSTOX_AUTH_CODE`: Temporary OAuth authorization code
- `BUCKET`: Google Cloud Storage bucket name
- `UPSTOX_SYMBOL`: Stock symbol (default: NSE_EQ|INE002A01018)
- `UPSTOX_INTERVAL`: Data interval (default: 30minute)
- `UPSTOX_TO_DATE`: End date for data fetch
- `UPSTOX_FROM_DATE`: Start date for data fetch

## Deployment

Deploy as a Google Cloud Function:
```bash
gcloud functions deploy upstox-fetcher --runtime python39 --trigger-http --entry-point check_gcs_connection
```

## API Usage

The function accepts HTTP requests with optional JSON parameters:
```json
{
  "symbol": "NSE_EQ|INE002A01018",
  "interval": "30minute",
  "to_date": "2025-03-30",
  "from_date": "2023-06-01"
}
```