from sqlalchemy import Boolean, Integer, String, Column
from database import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ticker = Column(String, unique=True)
