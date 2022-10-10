import joblib

from boxkite.monitoring.collector import BaselineMetricCollector
from boxkite.monitoring.service import ModelMonitoringService
from flask import Flask, request


model = joblib.load("../model/AAPL.joblib")

monitor = ModelMonitoringService(
    baseline_collector=BaselineMetricCollector(path="./histogram.prom")
)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def predict():
    features = request.json
    score = model.predict([features])[0]
    pid = monitor.log_prediction(
        request_body=request.data,
        features=features,
        output=score,
    )
    return {"result": score, "prediction_id": pid}


@app.route("/metrics", methods=["GET"])
def metrics():
    return monitor.export_http()[0]


if __name__ == "__main__":
    app.run()
