from utils import params
import mlflow
import mlflow.sklearn
from flask import jsonify
import mlflow.tracking
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from conf import get_logger

log = get_logger(__name__)


def get_latest_model_id():
    log.info("Getting latest model ID")
    mlflow.set_tracking_uri(params.MLFLOW_TRACKING_URI)
    client = mlflow.tracking.MlflowClient()
    experiment = client.get_experiment_by_name("iris")
    latest_run = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        order_by=["start_time DESC"],
        max_results=1,
    )
    return latest_run[0].info.run_id if latest_run else None


def predict(request):
    mlflow.set_tracking_uri(params.MLFLOW_TRACKING_URI)
    log.info("Initiating prediction")
    model_id = request.args.get("model_id", get_latest_model_id())
    log.info("Model ID found: %s", model_id)

    model_uri = f"runs:/{model_id}/model"
    try:
        model = mlflow.sklearn.load_model(model_uri)
    except Exception as e:
        log.error("Model not found %s", e)
        return jsonify({"message": "Model not found", "model_uri": model_uri}), 500

    try:
        iris = load_iris()
        X = iris.data
        y = iris.target

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        input_data = X_test[:5]
        log.info("Input data: %s", input_data)
    except Exception as e:
        log.error("Invalid input data %s", e)
        return jsonify({"message": "Invalid input data", "input_data": input_data}), 500

    try:
        prediction = model.predict(input_data)
        log.info("Prediction: %s", prediction)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        log.error("Prediction failed %s", e)
        return jsonify({"message": "Prediction failed"}), 500
