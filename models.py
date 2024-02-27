from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.sql import func

Base=declarative_base()
  
class Management(Base):
    __tablename__ = "management_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    task_name = Column(String(200))
    category = Column(String(200))
    status = Column(String(100), nullable=False)
    date = Column(DateTime, default=func.now())

    def __init__(self, task_name, category, status):
        self.task_name = task_name
        self.category = category
        self.status = status