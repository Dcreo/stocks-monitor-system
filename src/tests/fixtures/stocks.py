import pytest

from src.schemas.stock import StockDTO
from src.models import Stock
from src.tests.factories.stock_factory import StockFactory

@pytest.fixture
def stock_factory(db):
    StockFactory._meta.sqlalchemy_session = db
    
    return StockFactory

@pytest.fixture(name="new_stock")
async def created_stock_with_api(stock_factory, client):
    # TODO common paths for API in file
    stock = stock_factory()
    result = await client.post("/stocks", json=stock.to_dict())

    return StockDTO(**result.json())

