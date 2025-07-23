from sqlalchemy import Column, Integer, String, DateTime, JSON, Boolean
from datetime import datetime
from app.db import Base

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    object_id = Column(Integer, nullable=False)
    bbox = Column(JSON, nullable=False)  # format: {"x": int, "y": int}
    area_name = Column(String, nullable=False)
    in_area = Column(Boolean, nullable=False)

class CountLog(Base):
    __tablename__ = "count_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    area_name = Column(String, nullable=False)
    direction = Column(String, nullable=False)  # 'in' or 'out'
    count = Column(Integer, nullable=False)
