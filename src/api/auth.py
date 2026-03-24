from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from typing import Annotated
from src.database import get_db
from src.models.user import User 
from src.schemas.user import *  
from src.core.security import get_password_hash, verify_password


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
