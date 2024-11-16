# Use the Python 3.9 base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 80 for Azure
EXPOSE 80

  
# Start the FastAPI app with Uvicorn on port 80
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app:app", "-c", "gunicorn_conf.py", "--log-level", "debug"]
