import os
import pytest

from httpx import AsyncClient
from src.main import app
from httpx import ASGITransport

transport = ASGITransport(app=app)

@pytest.fixture
async def client():
    async with AsyncClient(
        base_url="http://testserver", 
        trust_env=False, 
        transport=transport) as client:
        yield client

