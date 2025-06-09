from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class QueryLog(Base):
    __tablename__ = 'query_logs'
    id = Column(Integer, primary_key=True, index=True)
    engine = Column(String(50), nullable=False)
    mode = Column(String(10), nullable=False)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())