# W12D4 — End-to-End MLOps Pipeline Review

## Overview
A FastAPI machine learning service with automated tests,
Docker container configuration, CI/CD, and monitoring documentation.

## API Endpoints
- GET /health — checks API health
- POST /predict — returns a prediction and probability
- GET /monitoring — returns request, error, and latency metrics

## Run Locally
Install dependencies:

    pip install -r requirements.txt

Start the service:

    uvicorn app:app --reload

Open API documentation:
http://127.0.0.1:8000/docs

## Test
Install development dependencies:

    pip install -r requirements-dev.txt

Run:

    pytest -v

## Docker
Build the image:

    docker build -t w12d4-mlops .

Run the container:

    docker run -p 8000:8000 w12d4-mlops

## CI/CD
GitHub Actions performs linting, tests, and Docker image building.
Docker Hub publishing requires repository secrets:
DOCKERHUB_USERNAME and DOCKERHUB_TOKEN.

## Monitoring
See monitoring.md for metrics, alerts, retraining triggers,
and safe deployment practices.

## Limitations
Monitoring metrics are currently in memory and reset on restart.
Production use requires persistent monitoring and deployment safeguards.
