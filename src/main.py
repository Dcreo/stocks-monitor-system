from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, condecimal
from src.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Annotated, Optional
from src.models import Stock

import uvicorn
import os
import src.models as models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class StockItem(BaseModel):
    id: Optional[int] = None
    name: str
    ticker: str
    exchange: str
    price: condecimal(max_digits=10, decimal_places=2) | None = None

class StockUpdate(StockItem):
    name: Optional[str] = None
    ticker: Optional[str] = None
    exchange: Optional[str] = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db = Annotated[Session, Depends(get_db)]

@app.get("/")
def index():
    return "Stocks monitor!"

@app.get("/stocks")
def stocks():
    return "Public Stocks list"

@app.get("/stocks/{id}")
def stock(id):
    return f"Stock with id: {id}"

@app.post("/stocks")
async def create_stock(stock: StockItem, db: db):
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

@app.patch("/stocks/{stock_id}")
async def update_stock(stock_id: int, stock_data: StockUpdate, db: db):
    stock = db.get(Stock, stock_id)
    # print("***********************")
    # print(stock_data)
    # print(stock)
    # print("***********************")
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, port=8081)
