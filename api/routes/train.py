"""
This module contains the train_model function that trains a Logistic Regression model on the iris dataset and logs the accuracy on mlflow.
"""

import mlflow

from conf import get_logger

from flask import jsonify

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from utils import params

log = get_logger(__name__)


def train_model():
    # Load the iris dataset
    log.info("Loading iris dataset")
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Train model
    log.info("Training model")
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # Log the accuracy on mlflow
    log.info("Logging accuracy on mlflow")
    mlflow.set_tracking_uri(params.MLFLOW_TRACKING_URI)
    mlflow.set_experiment("iris")
    mlflow.set_experiment_tags(
        {
            "dataset": "iris",
            "strategy": "LogisticRegression",
            "challenge": "RocketScience",
        }
    )
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

    run_id = mlflow.active_run().info.run_id
    log.info("Model trained with accuracy: %s at run_id: %s", accuracy, run_id)
    return jsonify({"accuracy": accuracy, "mlflow_run_id": run_id})
