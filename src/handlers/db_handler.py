import os
import logging
import datetime
from urllib.parse import quote
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL = "mssql+pyodbc://{user}:{pwd}@{host}:{port}/{db}?driver={driver}"

MSSQL = URL.format(
    host=os.getenv('host'),
    port=os.getenv('port'),
    db=os.getenv('db'),
    user=os.getenv('user'),
    pwd=quote(os.getenv('pwd')),
    driver=os.getenv('driver', "ODBC Driver 17 for SQL Server"),
)

Base = declarative_base()

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String(50), index=True)
    message = Column(String(255))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


engine = create_engine(MSSQL, echo=True, pool_size=5, max_overflow=10)
Base.metadata.create_all(bind=engine)
Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

class CustomDBLogger(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        log_entry = Log(
            level=record.levelname,
            message=self.format(record),
            timestamp=datetime.datetime.utcnow()
        )
        try:
            with Session() as session:
                try:
                    session.add(log_entry)
                    session.commit()
                except Exception as e:
                    session.rollback()
                    print(f"Failed to log to database: {e}")
        except Exception as e:
            print(f"Failed to log to database: {e}")

    def get_memory(self):
        try:
            with Session() as session:
                logs = session.query(Log).all()
                return [{'level': log.level, 'message': log.message, 'timestamp': log.timestamp} for log in logs]
        except Exception as e:
            logging.error(f"Failed to retrieve logs from database: {e}")
            return []
