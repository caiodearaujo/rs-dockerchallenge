from routes.train import train_model
from routes.models import get_models
from routes.predict import predict
from routes.logs import get_logs_from_db

ROUTES = [train_model, get_models, predict, get_logs_from_db]
