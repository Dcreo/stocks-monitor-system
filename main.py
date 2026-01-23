from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

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
    uvicorn.run("main:app", reload=True)
