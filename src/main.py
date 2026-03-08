from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from src.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Annotated
from src.models import Stock

import uvicorn
import os
import src.models as models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class NewStock(BaseModel):
    name: str
    ticker: str
    exchange: str

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
async def create_stock(stock: NewStock, db: db):
    new_stock = Stock(
        name=stock.name,
        ticker=stock.ticker,
        exchange=stock.exchange
    )

    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    
    return new_stock 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, port=8081)
