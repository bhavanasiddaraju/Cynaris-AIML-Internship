# ML API Monitoring Strategy

## Metrics to Track
- API availability and health endpoint status
- Request latency (p50, p95, and p99)
- Request volume and HTTP 4xx/5xx error rates
- Prediction distribution and input feature drift
- Model accuracy when ground-truth labels become available
- Container CPU, memory, and restart counts

## Alerts
- Health checks fail for 2 consecutive minutes
- HTTP 5xx error rate exceeds 5% over 5 minutes
- p95 latency exceeds 500 ms for 5 minutes
- Container repeatedly restarts or approaches memory limits
- Input or prediction distributions show significant drift

## Retraining Triggers
- Model performance falls below an agreed validation threshold
- Sustained feature or prediction drift is detected
- New labeled data becomes available in sufficient quantity
- Scheduled review identifies a meaningful data or business change

## Retraining Safeguards
- Validate data quality before training
- Compare candidate and production models
- Run automated tests and evaluate model metrics
- Promote only if validation criteria pass
- Keep the previous model available for rollback

## Implementation Note
These are proposed monitoring thresholds, not active alerts.
Production monitoring requires instrumentation, metrics collection,
alerting infrastructure, and access to labeled outcomes.
