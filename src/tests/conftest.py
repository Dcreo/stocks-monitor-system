import pytest

from httpx import AsyncClient, ASGITransport

from src.main import app
from src.models import Base
from src.database import get_db

from fixtures.database import db, TestingSessionLocal, engine
from fixtures.stocks import * 
from fixtures.users import * 

from reports.config import * 

transport = ASGITransport(app=app)

@pytest.fixture(scope="session")
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture
async def client(setup_database):
    async def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        base_url="http://testserver", 
        trust_env=False, 
        transport=transport) as client:

        yield client

    app.dependency_overrides.clear()

