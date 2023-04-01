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

class Monster(BaseModel):
    id: Optional[int] 
    name: str

class AllMonsters(BaseModel):
    name: List[str]

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
    done: int

class Coupon(BaseModel):
    id: Optional[int]
    customer_id: int
    description: str
    discount: int
    code: str
    start_date: date
    end_date: date
    done: int

class Target(BaseModel):
    id: Optional[int] 
    product_id: int #specific producs for each customers preference
    target_points: int
    battlepass_id: int
    done: int

class Battlepass(BaseModel):
    id: Optional[int] 
    customer_id: int
    start_date: date
    end_date: date

class BattlepassTarget(BaseModel):
    targets: List[Target]
    start_date: date
    end_date: date

class LeaderboardObject(BaseModel):
    index: str
    name: str
    points: int

class LeaderboardResult(BaseModel):
    leaderboard_result: List[LeaderboardObject]
    start_date: date
    end_date: date

class Leaderboard(BaseModel):
    id: Optional[int]
    start_date: date
    end_date: date

class SpinningWheel(BaseModel):
    id: Optional[int] 
    start_date: date
    end_date: date

class SpinningWheelRewards(BaseModel):
    slice: List[str]
    start_date: date
    end_date: date