import pytest

@pytest.mark.auth
@pytest.mark.api
async def test_login_with_jwt(user_with_jwt):
    parts = user_with_jwt.jwt.split(".")

    # TODO check correct JWT parts
    assert len(parts) == 3
    assert hasattr(user_with_jwt, "jwt")
