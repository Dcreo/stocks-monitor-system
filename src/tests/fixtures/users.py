import pytest

from src.schemas.user import UserDTO
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

