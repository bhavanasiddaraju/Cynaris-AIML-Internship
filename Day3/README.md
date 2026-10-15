# W12D3 — Monitoring ML Models in Production

## Overview
A FastAPI machine learning API with request monitoring,
basic data drift detection, automated tests, and Docker CI/CD.

## Features
- Logistic Regression prediction API
- Health check endpoint
- Request count, error rate, and latency metrics
- Basic feature mean-shift drift detection
- Retraining recommendations
- Pytest automated tests
- Dockerfile and GitHub Actions workflow

## Run locally
Install application dependencies:

    pip install -r requirements.txt

Start the API:

    uvicorn app:app --reload

Open the API documentation:
http://127.0.0.1:8000/docs

## API endpoints
- GET /health
- POST /predict
- GET /monitoring

Example prediction request:

    {"value": 4}

## Run tests

    pip install -r requirements-dev.txt
    pytest -v

## Docker

    docker build -t w12d3-ml-monitoring .
    docker run -p 8000:8000 w12d3-ml-monitoring

## CI/CD
GitHub Actions performs linting, testing, and Docker image building.
Docker Hub publishing requires repository secrets.

## Monitoring
See monitoring.md for monitoring metrics, alerts, drift detection,
retraining triggers, and deployment safety.

## Limitations
The monitoring metrics are in-memory and reset on restart.
The mean-shift check is educational and is not a full statistical
drift test. Validate candidate models before deployment.
