# Upstox Data Loader

A Google Cloud Function for loading historical stock data from Upstox API.

## Features

- Fetches historical candle data from Upstox API
- Configurable stock symbols, intervals, and date ranges
- Google Cloud Storage integration
- Environment variable configuration

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your Upstox API credentials
```

## Required Environment Variables

- `client_id`: Upstox API client ID
- `client_secret`: Upstox API client secret
- `UPSTOX_AUTH_CODE`: Temporary OAuth authorization code
- `bucket_name`: Google Cloud Storage bucket name
- `UPSTOX_SYMBOL`: Stock symbol (optional, default provided)
- `UPSTOX_INTERVAL`: Data interval (optional, default provided)
- `UPSTOX_TO_DATE`: End date (optional, default provided)
- `UPSTOX_FROM_DATE`: Start date (optional, default provided)

## Deployment

Deploy as a Google Cloud Function using the Google Cloud CLI.