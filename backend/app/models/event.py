from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from ..database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    source_ip = Column(String(45), nullable=False)
    destination_ip = Column(String(45), nullable=False)
    protocol = Column(String(20), nullable=False)
    description = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    severity = Column(String(20), default="low")  # low, medium, high