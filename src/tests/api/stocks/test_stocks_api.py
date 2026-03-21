import pytest

from src.main import StockItem
from decimal import Decimal

@pytest.mark.asyncio
async def test_get_stocks_api(client):
    response = await client.get("/stocks")

    assert response.status_code == 200

@pytest.mark.asyncio
async def test_create_stock_api(client):
    response = await client.post("/stocks", json={
        "name": "Test company",
        "ticker": "TEST",
        "exchange": "TestExchange"
    })

    stock = StockItem(**response.json())

    assert response.status_code == 200
    assert stock.id is not None
    assert stock.name == "Test company"

@pytest.mark.asyncio
async def test_update_stocks_api(client, new_stock):
    response = await client.patch(f"/stocks/{new_stock.id}", json={
        "name": "New Company Name",
        "price": 10.10
    })

    updated_stock = StockItem(**response.json())

    assert response.status_code == 200
    assert updated_stock.name == "New Company Name" 
    assert updated_stock.price == Decimal("10.10")

@pytest.mark.asyncio
async def test_delete_stock_api(client, new_stock):
    response = await client.delete(f"/stocks/{new_stock.id}")
    
    deleted_stock = StockItem(**response.json())

    assert response.status_code == 200
    assert deleted_stock.id == new_stock.id

