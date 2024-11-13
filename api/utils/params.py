import os
import dotenv


def get_env_value(key: str, default: str) -> str:
    dotenv.load_dotenv()
    return os.getenv(key, default)


MARIADB_HOST = get_env_value("MARIADB_HOST", "db")
MLFLOW_TRACKING_URI = get_env_value("MLFLOW_TRACKING_URI", "http://mlflow:5000")
