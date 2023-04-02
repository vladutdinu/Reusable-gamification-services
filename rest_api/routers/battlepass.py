from fastapi import APIRouter, Depends, HTTPException, Response
from utils import battlepass_crud, customer_crud, coupon_crud
from models import model
from schemas import schema
from database import SessionLocal
from datetime import date, timedelta
from random import randint
# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/battlepass", tags=["Battlepass Endpoints"])

@router.post("/", response_model=model.Battlepass)
async def create_battlepass(battlepass: model.Battlepass, db: get_db = Depends()):
    result = battlepass_crud.get_battlepass(battlepass.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Battlepass already exist")
    return battlepass_crud.create_battlepass(battlepass, db).__dict__


@router.get("/{battlepass_id}", response_model=model.Battlepass)
async def get_battlepass(battlepass_id: int, db: get_db = Depends()):
    result = battlepass_crud.get_battlepass(battlepass_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="Battlepass doesnt exist")

@router.post("/all/", response_model=model.BattlepassTarget)
async def get_battlepass_with_targets(battlepass_requester: model.BattlepassRequester, db: get_db = Depends()):
    customer = customer_crud.get_customer_with_points_by_id(battlepass_requester.customer_id, db)
    battlepass = battlepass_crud.get_battlepass_with_targes(battlepass_requester.current_date, battlepass_requester.customer_id, db)

    for target in battlepass.targets:
        if customer.points.current_points >= target.target_points and target.done == 0:
            coupon_crud.create_coupon(model.Coupon(
                customer_id = customer.customer_id,
                description = "Random description " + str(target.target_points),
                discount = int(randint(0,100)),
                code = "C"+str(target.target_points),
                start_date = battlepass_requester.current_date,
                end_date = battlepass_requester.current_date + timedelta(days=10)
            ), db)
            battlepass_crud.update_target_status(target, 1, db)

    return battlepass_crud.get_battlepass_with_targes(battlepass_requester.current_date, battlepass_requester.customer_id, db).__dict__

@router.put("/", response_model=model.Battlepass)
async def update_battlepass(battlepass: model.Battlepass, db: get_db = Depends()):
    result = battlepass_crud.update_battlepass(battlepass, db)
    if result:
        return battlepass_crud.get_battlepass(battlepass.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Battlepass doesnt exist")

@router.delete("/{battlepass_id}", response_model=model.Battlepass)
async def delete_battlepass(battlepass_id: int, db: get_db = Depends()):
    result = battlepass_crud.delete_battlepass(battlepass_id, db)
    if result:
        return Response("Battlepass deleted")
    else:
        raise HTTPException(status_code=400, detail="Battlepass doesnt exist")

@router.post("/target/", response_model=model.Target)
async def create_target(target: model.Target, db: get_db = Depends()):
    result = battlepass_crud.get_target_by_id(target.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Target already exist")
    return battlepass_crud.create_target(target, db).__dict__


@router.get("/target/{target_id}", response_model=model.Target)
async def get_target(target_id: int, db: get_db = Depends()):
    result = battlepass_crud.get_target_by_id(target_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="Target doesnt exist")


@router.put("/target/", response_model=model.Target)
async def update_target(target: model.Target, db: get_db = Depends()):
    result = battlepass_crud.update_target(target, db)
    if result:
        return battlepass_crud.get_target_by_id(target.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Target doesnt exist")

@router.put("/target/{target_id}", response_model=model.Target)
async def update_target_status(target_id: int, db: get_db = Depends()):
    result = battlepass_crud.update_target_status(target_id, db)
    if result:
        return battlepass_crud.get_target_by_id(target_id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Target doesnt exist")

@router.delete("/target/{target_id}", response_model=model.Target)
async def delete_target(target_id: int, db: get_db = Depends()):
    result = battlepass_crud.delete_target(target_id, db)
    if result:
        return Response("Battlepass deleted")
    else:
        raise HTTPException(status_code=400, detail="Target doesnt exist")

