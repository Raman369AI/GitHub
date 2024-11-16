version: '3.8'

services:
  fastapi:
    image: raman.azurecr.io/app-fastapi:latest
    container_name: app-fastapi
    ports:
      - "8000:8000"
    networks:
      - app-network

  streamlit:
    image: raman.azurecr.io/app-streamlit:latest
    container_name: app-streamlit
    ports:
      - "8501:8501"
    networks:
      - app-network
    depends_on:
      - fastapi

networks:
  app-network:
    driver: bridge
