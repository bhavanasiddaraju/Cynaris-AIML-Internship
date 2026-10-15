from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression

app = FastAPI(title="W12D1 ML Prediction API")

X = [[0], [1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)


class PredictionInput(BaseModel):
    value: float


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: PredictionInput):
    prediction = int(model.predict([[data.value]])[0])
    return {"input": data.value, "prediction": prediction}
