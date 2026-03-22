from typing import List, Annotated, Optional
from pydantic import BaseModel, condecimal

class StockDTO(BaseModel):
    id: Optional[int] = None
    name: str
    ticker: str
    exchange: str
    price: condecimal(max_digits=10, decimal_places=2) | None = None

class StockUpdateDTO(StockDTO):
    name: Optional[str] = None
    ticker: Optional[str] = None
    exchange: Optional[str] = None

