import pytest

from src.main import StockItem

@pytest.fixture(name="new_stock")
async def created_stock_with_api(client):
    # TODO common paths for API in file
    result = await client.post("/stocks", json={
        "name": "TestCompany",
        "ticker": "Ticker",
        "price": 3.14,
        "exchange": "Moex"
    })

    return StockItem(**result.json())
