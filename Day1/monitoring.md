
# W8D1 Production RAG Monitoring Strategy

## 1. Availability

Monitor the `/health` endpoint to verify that the API is available.

## 2. Latency

Track API response latency and retrieval latency to identify slow requests.

## 3. Error Rate

Monitor HTTP 4xx and 5xx responses and application exceptions.

## 4. Retrieval Quality

Track retrieval metrics such as Hit@1, Hit@3 and Mean Reciprocal Rank (MRR).

## 5. RAG Quality

Evaluate answer relevance, faithfulness and context quality using a representative evaluation dataset.

## 6. Resource Usage

Monitor CPU and memory usage of the Docker container.

## 7. Logging

Store application events, request information, errors and latency measurements while avoiding sensitive information.

## 8. Alerts

Configure alerts for API downtime, increased error rates, high latency and degradation in retrieval quality.
