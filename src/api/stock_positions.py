from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from typing import Annotated

from src.database import get_db
# from src.models.stock import Stock

# from src.schemas.stock import StockDTO, StockUpdateDTO

db = Annotated[Session, Depends(get_db)]

router = APIRouter()

@router.get("/stock_positions")
def stocks():
    return "Protected stock positions route"
