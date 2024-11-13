import logging
from conf.db import log_to_db


class DatabaseLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        log_to_db(record.levelname, self.format(record))


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(DatabaseLogHandler())
    return logger
