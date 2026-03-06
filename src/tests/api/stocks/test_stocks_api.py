import pytest

@pytest.mark.asyncio
async def test_get_stocks_api(client):
    response = await client.get("/stocks")

    print("***************")
    print(response.text)
    print("***************")
    assert response.status_code == 200
