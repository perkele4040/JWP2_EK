from sqlalchemy import create_engine, inspect, text, select, func, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.orm import Session


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)
