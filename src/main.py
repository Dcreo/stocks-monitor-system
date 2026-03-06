from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from src.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Annotated

import uvicorn
import os
import src.models as models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Stock(BaseModel):
    name: str
    ticker: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def index():
    return "Stocks monitor!"

@app.get("/stocks")
def stocks():
    return "Public Stocks list"

@app.get("/stocks/{id}")
def stock(id):
    return f"Stock with id: {id}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, port=8081)
