"""
This module contains the functions to list all models tracked in the MLflow registry.
"""

from utils import params
import mlflow
from flask import jsonify
from conf import get_logger

log = get_logger(__name__)


def get_models():
    # List all models tracked in the MLflow registry
    log.info("Listing models from mlflow")
    mlflow.set_tracking_uri(params.MLFLOW_TRACKING_URI)
    mlflow.set_experiment("iris")
    models = mlflow.search_runs()
    return jsonify(models.to_dict(orient="records"))
