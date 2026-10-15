# ML API Monitoring Strategy

## 1. Application Monitoring
- Monitor API health using the GET /health endpoint.
- Track prediction request counts and response times.
- Record HTTP errors and failed requests.
- Monitor CPU, memory, and container resource usage.

## 2. Alerts
- Alert when the API health check fails.
- Alert when HTTP 5xx errors increase.
- Alert when response latency exceeds the service target.
- Alert when CPU or memory usage remains unusually high.

## 3. Model Monitoring
- Track prediction distributions over time.
- Monitor changes in incoming feature distributions.
- Compare predictions with actual outcomes when labels become available.
- Check for data drift and model performance degradation.

## 4. Retraining Triggers
- Retrain when model performance falls below the agreed threshold.
- Investigate significant data or concept drift.
- Retrain when enough new, representative labelled data is available.
- Validate the new model before deployment.

## 5. Deployment Safety
- Run automated tests before building the Docker image.
- Use versioned images and model versions.
- Keep the previous working version available for rollback.
- Never deploy a newly trained model without validation.
