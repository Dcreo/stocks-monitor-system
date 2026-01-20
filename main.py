from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def index():
    return "Stocks monitor!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
