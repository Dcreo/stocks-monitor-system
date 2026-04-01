import pytest

from src.schemas.auth import Token
from src.schemas.user import UserDTO, UserWithJwt
from src.models import User 
from src.tests.factories.user_factory import UserFactory

@pytest.fixture
def user_factory(db):
    UserFactory._meta.sqlalchemy_session = db
    
    return UserFactory

@pytest.fixture(name="new_user")
async def user_registration_with_api(user_factory, client):
    # TODO common paths for API in file
    user = user_factory()
    result = await client.post("/auth/register", json=user.to_dict())

    return UserDTO(**result.json())

@pytest.fixture(name="user_with_jwt")
async def user_login_with_jwt(client, new_user):
    response = await client.post("/auth/token", json={
        "email": new_user.email,
        "password": "12345678"
    })

    token = Token(**response.json())

    return UserWithJwt(
        id=new_user.id,
        email=new_user.email,
        username=new_user.username,
        jwt=token.access_token
    )
