from typing import Optional, List, Union
from pydantic import BaseModel

class Tier(BaseModel):
    id: Optional[int] 
    name: str
    price: int

    class Config:
        orm_mode = True

class Gamification(BaseModel):
    id: Optional[int]
    name: str
    description: str
    tier: int

    class Config:
        orm_mode = True


class Customer(BaseModel):
    id: Optional[int]
    name: str
    type: str
    tier_picked: int

    class Config:
        orm_mode = True
