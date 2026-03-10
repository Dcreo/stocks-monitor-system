import pytest

from src.models import Stock

@pytest.mark.asyncio
async def test_get_stocks_api(client):
    response = await client.get("/stocks")

    assert response.status_code == 200

async def test_create_stock_api(client):
    response = await client.post("/stocks", json={
        "name": "Test company",
        "ticker": "TEST",
        "exchange": "TestExchange"
    })

    data = response.json()
    stock = Stock(**data)
    
    assert response.status_code == 200
    assert stock.id is not None

async def test_update_stocks_api(client):
    response = await client.get("/stocks")

    assert response.status_code == 200

