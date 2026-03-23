from fastapi import FastAPI
from src.database import engine

from src.api import stocks
from src.api import auth

import uvicorn
import src.models as models

app = FastAPI()

app.include_router(stocks.router)
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, port=8081)
