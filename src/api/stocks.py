from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from typing import Annotated

from src.database import get_db
from src.models.stock import Stock

from src.schemas.stock import StockDTO, StockUpdateDTO

db = Annotated[Session, Depends(get_db)]

router = APIRouter()

@router.get("/stocks")
def stocks():
    return "Public Stocks list"

@router.get("/stocks/{id}")
def stock(id):
    return f"Stock with id: {id}"

@router.post("/stocks")
async def create_stock(stock: StockDTO, db: db):
    new_stock = Stock(
        name=stock.name,
        ticker=stock.ticker,
        exchange=stock.exchange,
        price=stock.price
    )

    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    
    return new_stock 

@router.patch("/stocks/{stock_id}")
async def update_stock(stock_id: int, data: StockUpdateDTO, db: db):
    stock = db.get(Stock, stock_id)

    if not stock:
        return {"error": "Stock not found"}

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(stock, field, value)

    db.commit()
    db.refresh(stock)

    return stock

@router.delete("/stocks/{stock_id}")
async def delete_stock(stock_id: int, db: db):
    stock = db.get(Stock, stock_id)
    
    if not stock:
        return {"error": "Stock not found"}

    db.delete(stock)
    db.commit()

    return stock


