import pytest

from decimal import Decimal

from src.schemas.user import UserDTO 

@pytest.mark.asyncio
async def test_user_registration_api(new_user):
    assert new_user.id is not None
