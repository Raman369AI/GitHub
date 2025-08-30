# Data Science & Machine Learning Portfolio

This repository contains a collection of data science, machine learning, and web development projects organized in a standard structure.

## Repository Structure

```
├── projects/
│   ├── data-science/        # Data science and ML projects
│   ├── web-apps/           # Web applications and frontend projects
│   ├── algorithms/         # Algorithm implementations and practice
│   └── competitions/       # Coding competitions and hackathons
├── notebooks/
│   ├── courses/           # Educational notebooks from courses
│   └── exploratory/       # Experimental and research notebooks
├── datasets/              # Data files and datasets
├── docs/                  # Documentation
└── scripts/              # Utility scripts
```

## Technologies Used

- **Python**: Data science, machine learning, algorithms
- **JavaScript/React**: Web applications and frontend development
- **Jupyter Notebooks**: Data analysis and experimentation
- **Flask**: Web backend development
- **PyTorch/TensorFlow**: Deep learning frameworks
- **Apache Airflow**: Data pipeline orchestration

## Getting Started

Each project contains its own README with specific setup instructions. Most Python projects require:

```bash
pip install -r requirements.txt
```

For React projects:
```bash
npm install
npm start
```

## Important Security Notice for Web Applications

### myflaskapp (projects/web-apps/myflaskapp)

The applications within the `myflaskapp` directory require access to the Upstox API. Environment variables are used for secure credential management.

**Required Environment Variables:**
- `client_id`: Your Upstox API client ID
- `client_secret`: Your Upstox API client secret
- `BUCKET`: Google Cloud Storage bucket name
- `UPSTOX_AUTH_CODE`: Temporary authorization code from Upstox OAuth flow
- `UPSTOX_REDIRECT_URI`: OAuth redirect URI

### poisonous_mushrooms (projects/data-science/poisonous_mushrooms)

The Streamlit application connects to a FastAPI prediction service.

**Required Environment Variable:**
- `PREDICTION_API_URL`: Full URL to the prediction API endpoint

**Security Best Practices:**
- Never commit `.env` files or hardcode credentials
- Use environment variables for all sensitive configuration
- Rotate API keys and tokens regularly