# TODO move data from file
from sqlalchemy import Boolean, Integer, String, Column, Numeric
from src.database import Base
from src.models.mixins import JSONSerializer

class Stock(Base, JSONSerializer):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ticker = Column(String, unique=True)
    price = Column(Numeric(10, 2), nullable=False, default=0.00)
    exchange = Column(String, index=True)
