from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 
from typing import Annotated

from src.database import get_db
from src.models.user import User 
from src.schemas.user import *  
from src.schemas.auth import *  

from src.core.security import get_password_hash, verify_password
from src.core.auth import authenticate_user


db = Annotated[Session, Depends(get_db)]

router = APIRouter()

@router.post("/auth/register", response_model=UserDTO)
async def register(user: UserCreateDTO, db: db):
    new_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/auth/token")
async def login_with_jwt_token(form_data: LoginDTO, db: db):
    user = authenticate_user(db, form_data.email, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print("FORM DATA", form_data)
    pass
