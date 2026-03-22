import json

from sqlalchemy import Boolean, Integer, String, Column, Numeric
from src.database import Base
from .mixins import JSONSerializer

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, unique=True)
    password = Column(String, index=True)
