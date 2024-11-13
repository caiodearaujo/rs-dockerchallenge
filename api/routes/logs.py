from flask import jsonify
from conf import db
from conf import get_logger

log = get_logger(__name__)


def get_logs_from_db():
    log.info("Getting logs from the database")
    logs = db.get_logs()
    return jsonify(logs)
