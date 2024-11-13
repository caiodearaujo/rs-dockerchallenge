from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pymysql

from utils import params

Base = declarative_base()


class AppLog(Base):
    __tablename__ = "app_logs"

    id = Column(Integer, primary_key=True)
    level = Column(String(10))
    message = Column(String(255))
    timestamp = Column(DateTime, default=datetime.now)


__DB_CONFIG__ = {
    "host": params.MARIADB_HOST,
    "user": "rs_user",
    "password": "rs_password",
    "database": "rs_challenge",
    "charset": "utf8",
}
__DATABASE_URI__ = f"mysql+pymysql://{__DB_CONFIG__['user']}:{__DB_CONFIG__['password']}@{__DB_CONFIG__['host']}/{__DB_CONFIG__['database']}"


def get_db_conn():
    return create_engine(__DATABASE_URI__)


def log_to_db(level, message):
    Session = sessionmaker(bind=get_db_conn())
    session = Session()
    try:
        new_log = AppLog(level=level, message=message)
        session.add(new_log)
        session.commit()
        print(f"Logged: {level} - {message}")
    except Exception as e:
        print(f"Failed to log: {level} - {message} - {e}")
    finally:
        session.close()


def get_logs():
    Session = sessionmaker(bind=get_db_conn())
    session = Session()
    try:
        logs = session.query(AppLog).all()
        return [
            {"level": log.level, "message": log.message, "timestamp": log.timestamp}
            for log in logs
        ]
    except Exception as e:
        print(f"Failed to get logs: {e}")
        return []
    finally:
        session.close()
