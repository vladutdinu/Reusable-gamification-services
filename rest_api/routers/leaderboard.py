from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from utils import leaderboard_crud
from models import model
from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/leaderboard", tags=["leaderboard Endpoints"])

@router.post("/", response_model=model.Leaderboard)
async def create_leaderboard(leaderboard: model.Leaderboard, db: get_db = Depends()):
    result = leaderboard_crud.get_leaderboard(leaderboard.id, db)
    if result:
        raise HTTPException(status_code=400, detail="leaderboard already exist")
    return leaderboard_crud.create_leaderboard(leaderboard, db).__dict__

@router.get("/{leaderboard_id}", response_model=model.Leaderboard)
async def get_leaderboard(leaderboard_id: int, db: get_db = Depends()):
    result = leaderboard_crud.get_leaderboard(leaderboard_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="leaderboard doesnt exist")
    
@router.get("/all/{customer_id}", response_model=List[model.Leaderboard])
async def get_leaderboards_customer(customer_id: int, db: get_db = Depends()):
    result = leaderboard_crud.get_leaderboards_customer(customer_id, db)
    if result:
        return [leaderboard.__dict__ for leaderboard in result]
    else:
        raise HTTPException(status_code=400, detail="No leaderboards")

@router.put("/", response_model=model.Leaderboard)
async def update_leaderboard(leaderboard: model.Leaderboard, db: get_db = Depends()):
    result = leaderboard_crud.update_leaderboard(leaderboard, db)
    if result:
        return leaderboard_crud.get_leaderboard(leaderboard.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="leaderboard doesnt exist")

@router.put("/", response_model=model.Leaderboard)
async def update_leaderboard_status(leaderboard_id: int, db: get_db = Depends()):
    result = leaderboard_crud.update_leaderboard_status(leaderboard_id, db)
    if result:
        return leaderboard_crud.get_leaderboard(leaderboard_id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="leaderboard doesnt exist")

@router.delete("/{leaderboard_id}", response_model=model.Leaderboard)
async def delete_leaderboard(leaderboard_id: int, db: get_db = Depends()):
    result = leaderboard_crud.delete_leaderboard(leaderboard_id, db)
    if result:
        return Response("leaderboard deleted")
    else:
        raise HTTPException(status_code=400, detail="leaderboard doesnt exist")