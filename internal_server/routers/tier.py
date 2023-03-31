from fastapi import APIRouter, Depends, HTTPException, Response
from utils import tier_crud
from models import model
from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/tier", tags=["Tier Endpoints"])

@router.post("/", response_model=model.Tier)
async def create_item(tier: model.Tier, db: get_db = Depends()):
    result = tier_crud.get_tier(tier.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Tier already exists")
    return tier_crud.create_tier(tier, db)

@router.get("/{tier_id}", response_model=model.Tier)
async def get_item(tier_id: int, db: get_db = Depends()):
    result = tier_crud.get_tier(tier_id, db)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Tier doesnt exist")

@router.put("/", response_model=model.Tier)
async def get_item(tier: model.Tier, db: get_db = Depends()):
    result = tier_crud.update_tier(tier, db)
    if result:
        return tier_crud.get_tier(tier.id, db)
    else:
        raise HTTPException(status_code=400, detail="Tier doesnt exist")

@router.delete("/{tier_id}", response_model=model.Tier)
async def get_item(tier_id: int, db: get_db = Depends()):
    result = tier_crud.delete_tier(tier_id, db)
    if result:
        return Response("Tier deleted")
    else:
        raise HTTPException(status_code=400, detail="Tier doesnt exist")