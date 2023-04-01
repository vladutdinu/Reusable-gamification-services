from datetime import date
from typing import Optional, List
from pydantic import BaseModel

class CustomerPoints(BaseModel):
    id: Optional[int]
    points: int

class Customer(BaseModel):
    id: Optional[int]
    customer_id: int
    points_id: Optional[int]

class CustomerWithPoints(BaseModel):
    id: Optional[int]
    customer_id: int
    points: Optional[CustomerPoints]

    class Config:
        orm_mode = True

class Token(BaseModel):
    id: Optional[int] 
    qr_code: str
    token: str

class Quest(BaseModel):
    id: Optional[int] 
    customer_id: int 
    quest: str
    target_quantity: int
    type: str
    quantity: int
    product_id: int
    points: int
    start_date: date
    end_date: date

class Coupon(BaseModel):
    id: Optional[int]
    customer_id: int
    description: str
    discount: int
    code: str
    start_date: date
    end_date: date

class Target(BaseModel):
    id: Optional[int] 
    product_id: int
    target_points: int
    battlepass_id: int

class Battlepass(BaseModel):
    id: Optional[int] 
    customer_id: int
    start_date: date
    end_date: date

class BattlepassTarget(BaseModel):
    targets: List[Target]
    start_date: date
    end_date: date

class Leaderboard(BaseModel):
    id: Optional[int] 
    customers: List[int]