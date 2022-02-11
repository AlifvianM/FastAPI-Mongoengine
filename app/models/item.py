from pydantic import BaseModel
from typing import List, Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class UpdatedItem(BaseModel):
    name: Optional[str]
    description: Optional[str] = None
    price: Optional[float]
    tax: Optional[float] = None
