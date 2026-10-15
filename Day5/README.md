# W12D5 — Production AI System: Full Pipeline

## Overview
A machine learning API with automated testing, Docker
containerization, CI/CD configuration, and monitoring documentation.

## API Endpoints
- GET /health — checks service health.
- POST /predict — returns a prediction and probability.
- GET /monitoring — reports request and latency metrics.

## Run Locally
Install dependencies:

    pip install -r requirements.txt

Start the API:

    uvicorn app:app --reload

API documentation:
http://127.0.0.1:8000/docs

## Run Tests

    pip install -r requirements-dev.txt
    pytest -v

## Docker

    docker build -t w12d5-ml-api .
    docker run -p 8000:8000 w12d5-ml-api

## CI/CD
The GitHub Actions workflow performs linting, testing,
and Docker image building. Docker Hub publishing is
configured for pushes to the main branch.

Configure these GitHub repository secrets for publishing:
- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN

## Monitoring
See monitoring.md for metrics, alert conditions,
and model retraining triggers.

## Limitations
The example model uses synthetic data, and monitoring
metrics are stored in memory. Production deployment
requires representative data, persistent monitoring,
and validated model deployment procedures.
