from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from utils import spinningwheel_crud
from models import model
from database import SessionLocal
from datetime import date
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/spinningwheel", tags=["Spinningwheel Endpoints"])

@router.post("/", response_model=model.SpinningWheel)
async def create_spinning_wheel(spinningwheel: model.SpinningWheel, db: get_db = Depends()):
    result = spinningwheel_crud.get_spinning_wheel(spinningwheel.id, db)
    if result:
        raise HTTPException(status_code=400, detail="spinningwheel already exist")
    return spinningwheel_crud.create_spinning_wheel(spinningwheel, db).__dict__

@router.post("/reward/", response_model=model.SpinningWheelReward)
async def create_spinning_wheel_reward(spinning_wheel_reward: model.SpinningWheelReward, db: get_db = Depends()):
    result = spinningwheel_crud.get_spinning_wheel_reward(spinning_wheel_reward.id, db)
    if result:
        raise HTTPException(status_code=400, detail="spinningwheel reward already exist")
    return spinningwheel_crud.create_spinning_wheel_reward(spinning_wheel_reward, db).__dict__


@router.get("/{spinningwheel_id}", response_model=model.SpinningWheel)
async def get_spinning_wheel(spinningwheel_id: int, db: get_db = Depends()):
    result = spinningwheel_crud.get_spinning_wheel(spinningwheel_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="spinningwheel doesnt exist")

@router.get("/reward/{spinning_wheel_reward_id}", response_model=model.SpinningWheel)
async def get_spinning_wheel(spinning_wheel_reward_id: int, db: get_db = Depends()):
    result = spinningwheel_crud.get_spinning_wheel_reward(spinning_wheel_reward_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="spinningwheel doesnt exist")

@router.get("/all/{current_date}", response_model=model.SpinningWheelRewards)
async def get_spinning_wheel_rewards(current_date: date, db: get_db = Depends()):
    result = spinningwheel_crud.get_spinning_wheel_with_rewards(current_date, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="No spinningwheels")

@router.put("/", response_model=model.SpinningWheel)
async def update_spinningwheel(spinningwheel: model.SpinningWheel, db: get_db = Depends()):
    result = spinningwheel_crud.update_spinning_wheel(spinningwheel, db)
    if result:
        return spinningwheel_crud.get_spinning_wheel(spinningwheel.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="spinningwheel doesnt exist")

@router.put("/reward/", response_model=model.SpinningWheelRewards)
async def update_spinningwheel_reward(spinning_wheel_reward: model.SpinningWheelRewards, db: get_db = Depends()):
    result = spinningwheel_crud.update_spinning_wheel_reward(spinning_wheel_reward, db)
    if result:
        return spinningwheel_crud.get_spinning_wheel_with_rewards(spinning_wheel_reward.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="spinning_wheel_reward doesnt exist")

@router.delete("/{spinningwheel_id}", response_model=model.SpinningWheel)
async def delete_spinningwheel(spinningwheel_id: int, db: get_db = Depends()):
    result = spinningwheel_crud.delete_spinning_wheel(spinningwheel_id, db)
    if result:
        return Response("spinningwheel deleted")
    else:
        raise HTTPException(status_code=400, detail="spinningwheel doesnt exist")

@router.delete("/reward/{spinning_wheel_reward_id}", response_model=model.SpinningWheel)
async def delete_spinningwheel(spinning_wheel_reward_id: int, db: get_db = Depends()):
    result = spinningwheel_crud.delete_spinning_wheel_reward(spinning_wheel_reward_id, db)
    if result:
        return Response("spinning_wheel_reward deleted")
    else:
        raise HTTPException(status_code=400, detail="spinning_wheel_reward doesnt exist")