# Poisonous Mushrooms Classifier

A machine learning application that predicts whether mushrooms are poisonous or edible based on their characteristics.

## Architecture

- **FastAPI Backend** (`app/fast_api/`): ML model serving with REST API
- **Streamlit Frontend** (`app/stream/`): User-friendly web interface
- **Docker Support**: Containerized deployment

## Features

- Interactive web interface for mushroom classification
- RESTful API for programmatic access
- Docker containerization for easy deployment
- Environment variable configuration for security

## Setup

### FastAPI Backend

1. Navigate to the FastAPI directory:
```bash
cd app/fast_api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API server:
```bash
uvicorn app:app --reload
```

### Streamlit Frontend

1. Navigate to the Streamlit directory:
```bash
cd app/stream
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp ../../.env.example .env
# Set PREDICTION_API_URL=http://localhost:8000/predict
```

4. Run the Streamlit app:
```bash
streamlit run stream.py
```

## Environment Variables

- `PREDICTION_API_URL`: URL to the FastAPI prediction endpoint

## Docker Deployment

Use Docker Compose to run both services:
```bash
docker-compose up
```

## API Usage

Send POST requests to `/predict` with mushroom features:
```json
{
  "cap-diameter": 5.2,
  "cap-shape": "x",
  "cap-surface": "s",
  "cap-color": "n"
}
```