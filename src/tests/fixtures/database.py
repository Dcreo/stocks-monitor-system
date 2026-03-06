import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Stock

# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(engine)

    session = TestingSessionLocal()

    yield session

    session.close()
    Base.metadata.drop_all(engine)

