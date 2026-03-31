from src.models.user import User
from src.core.security import verify_password

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

