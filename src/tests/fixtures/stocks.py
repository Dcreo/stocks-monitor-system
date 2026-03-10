import pytest

@pytest.fixture
async def create_stock_with_api():
    # TODO common paths for API in file
    result = await client.post("/users", {
        
    })
