# W12D5 — Production Monitoring Strategy

## 1. Metrics to Track
- API request volume and traffic patterns.
- API error rate and HTTP 4xx/5xx responses.
- Average and p95 response latency.
- CPU, memory, and container health.
- Input data quality and missing values.
- Prediction distribution and model performance.

## 2. Alerts
- Health endpoint failures: alert immediately.
- Server error rate above 5% over a monitoring window.
- p95 latency above the agreed service threshold.
- Sudden input feature or prediction distribution changes.
- Model performance below the required validation threshold.

## 3. Retraining Triggers
- Confirmed data or concept drift.
- Sustained decline in accuracy or other task metrics.
- Significant changes in incoming data.
- A scheduled review, if supported by fresh validated data.

Retraining must include data validation, model evaluation,
and approval before deployment. Keep the previous model
available for rollback.

## 4. CI/CD Pipeline
1. Install dependencies.
2. Run Ruff lint checks.
3. Run Pytest API tests.
4. Build the Docker image.
5. Publish the image to a registry when credentials
   and branch conditions permit.

## 5. Production Limitations
The current API stores metrics in memory, so they reset
when the process restarts. Production deployments should
use persistent monitoring, centralized logs, and an
external metrics backend. Drift thresholds must be
validated against representative production data.
