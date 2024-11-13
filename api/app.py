from flask import Flask, request, jsonify
import sqlite3
import pandas as pd

from routes import get_models, train_model, predict, get_logs_from_db
from conf import get_logger


app = Flask(__name__)
log = get_logger(__name__)


@app.route("/", methods=["GET"])
def route_home():
    log.info("Hello World endpoint was reached")
    return jsonify({"message": "Hello, World!"})


@app.route("/ping", methods=["GET"])
def route_ping():
    log.info("Ping endpoint was reached")
    return jsonify({"message": "pong"})


@app.route("/models", methods=["GET"])
def route_model():
    log.info("Models endpoint was reached")
    return get_models()


@app.route("/train", methods=["GET"])
def route_train():
    log.info("Train endpoint was reached")
    return train_model()


@app.route("/logs", methods=["GET"])
def route_logs():
    log.info("Logs endpoint was reached")
    return get_logs_from_db()


@app.route("/predict", methods=["POST"])
def route_predict():
    log.info("Predict endpoint was reached")
    return predict(request)


if __name__ == "__main__":
    log.info("Starting Flask app")
    app.run(host="0.0.0.0", port=8080, debug=True)
