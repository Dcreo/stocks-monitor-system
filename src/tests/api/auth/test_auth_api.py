import pytest

@pytest.mark.auth
@pytest.mark.api
async def test_login_with_jwt(client, new_user):
    response = await client.post("/auth/token", json={
        "email": new_user.email,
        "password": "12345678"
    })

    print(response.json())

    pass
