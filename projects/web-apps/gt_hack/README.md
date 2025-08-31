# iPhone Pricing Analysis Tool

A Streamlit application that uses AI agents to analyze iPhone pricing trends and provide pricing strategy recommendations.

## Features

- **Mathematical Analysis**: ARIMAX forecasting for 6-month price predictions
- **Market Analysis**: Event-driven price impact analysis using Gemini AI
- **Web Research**: Automated market research for iPhone shipments and revenue
- **Recommendations**: AI-powered pricing strategy recommendations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Required Environment Variables:
- `GEMINI_API_KEY`: Your Google Gemini API key
- `OLLAMA_API_BASE`: Ollama API endpoint (default: http://localhost:11434)
- `OLLAMA_API_KEY`: Ollama API key (if required)
- `PRICE_DATA_FILE`: Path to iPhone price data CSV

## Usage

```bash
streamlit run src/app.py
```

## Data Requirements

The application expects a CSV file with iPhone price data containing columns:
- Date
- New (price)
- CPIAUCSL
- Unemployment_Rate
- Interest Rates
- CPI

## Architecture

- `src/app.py`: Main Streamlit application
- `data/`: Data files
- `docs/`: Documentation and notebooks
- `config/`: Configuration files