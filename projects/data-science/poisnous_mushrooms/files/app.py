from fastapi import FastAPI

from logging_config import get_logger

logger = get_logger(__name__)

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}