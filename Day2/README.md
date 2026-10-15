# W12D2 — Docker for AI: ML Prediction API

## Overview
A FastAPI application serving predictions from a trained
scikit-learn Logistic Regression model.

## Features
- GET /health — checks API health
- POST /predict — returns a model prediction
- Dockerfile for containerising the application
- Pytest tests for API endpoints
- Ruff for Python code quality checks
- GitHub Actions CI/CD workflow
- Monitoring and retraining documentation

## Run locally
Install dependencies:

    pip install -r requirements.txt

Start the API:

    uvicorn app:app --reload

Open the interactive API documentation at:
http://127.0.0.1:8000/docs

## Run tests

    pip install -r requirements-dev.txt
    pytest -v

## Build and run with Docker

    docker build -t w12d2-ml-api .
    docker run -p 8000:8000 w12d2-ml-api

## Example prediction
Send POST /predict with this JSON body:

    {"value": 4}

## CI/CD
The GitHub Actions workflow checks code quality, runs tests,
and builds the Docker image. Docker Hub publishing on pushes
to main requires DOCKERHUB_USERNAME and DOCKERHUB_TOKEN
repository secrets.

## Monitoring
See monitoring.md for health checks, alerts, model monitoring,
retraining triggers, and deployment safety.
"""

(project_dir / "README.md").write_text(readme.strip() + "\n")

gitignore = """
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.venv/
venv/
.env
.ipynb_checkpoints/
