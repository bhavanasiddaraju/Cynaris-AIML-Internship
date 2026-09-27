
# W8D1 - Production RAG API

This project demonstrates a production-oriented Retrieval Augmented Generation API with retrieval evaluation, optimization, automated testing, Docker containerization, CI/CD and monitoring.

## Features

- TF-IDF based document retrieval
- RAG query pipeline
- Retrieval evaluation
- Hit@1
- Hit@3
- Mean Reciprocal Rank
- Retrieval latency comparison
- FastAPI API
- Automated tests
- Docker containerization
- GitHub Actions CI/CD
- Production monitoring strategy

## API Endpoints

### GET /

Returns the API status.

### GET /health

Returns the health status.

### POST /query

Example input:

```json
{
  "question": "What is RAG?",
  "top_k": 3
}
