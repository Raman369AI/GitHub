# gunicorn_conf.py
import multiprocessing

# Set the bind address to 0.0.0.0 and port 80 for Azure compatibility

from logging_config import get_logger

logger = get_logger(__name__)

bind = "0.0.0.0:80"
# Set the number of worker processes
workers = 4
# Increase the timeout if necessary
timeout = 120
# Optional: Set logging levels
loglevel = "info"
accesslog = "-"
errorlog = "-"
