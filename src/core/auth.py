import jwt
from datetime import datetime, timedelta, timezone
from src.models.user import User
from src.core.security import verify_password
from src.settings import env

def get_user(db, email: str):
   user = db.query(User).filter_by(email=email).first()

   if not user:
       return None

   return user

def authenticate_user(db, email: str, password: str):
    user = get_user(db, email)

    if not user:
        return False

    if not verify_password(password, user.password):
        return False

    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, env.secret_key, algorithm=env.algorithm)
    return encoded_jwt
