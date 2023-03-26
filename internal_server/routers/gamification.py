from fastapi import APIRouter, Depends, HTTPException, Response
from utils import gamification_crud
from models import model
from schemas import schema
from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/gamification", tags=["Gamification Endpoints"])

@router.post("/", response_model=model.Gamification)
async def create_item(gamification: model.Gamification, db: get_db = Depends()):
    result = gamification_crud.get_gamification(gamification.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Gamification already exists")
    return gamification_crud.create_gamification(gamification, db)

@router.get("/{gamification_id}", response_model=model.Gamification)
async def get_item(gamification_id: int, db: get_db = Depends()):
    result = gamification_crud.get_gamification(gamification_id, db)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Gamification doesnt exist")

@router.put("/", response_model=model.Gamification)
async def get_item(gamification: model.Gamification, db: get_db = Depends()):
    result = gamification_crud.update_gamification(gamification, db)
    if result:
        return gamification_crud.get_gamification(gamification.id, db)
    else:
        raise HTTPException(status_code=400, detail="Gamification doesnt exist")

@router.delete("/{gamification_id}", response_model=model.Gamification)
async def get_item(gamification_id: int, db: get_db = Depends()):
    result = gamification_crud.delete_gamification(gamification_id, db)
    if result:
        return Response("Gamification deleted")
    else:
        raise HTTPException(status_code=400, detail="Gamification doesnt exist")