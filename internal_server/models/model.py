from typing import Optional, List
from pydantic import BaseModel

class Tier(BaseModel):
    id: Optional[int] 
    name: str
    price: int

    class Config:
        orm_mode = True

class Tier_Picked(BaseModel):
    tier: int

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
    token: Optional[str]

    class Config:
        orm_mode = True
