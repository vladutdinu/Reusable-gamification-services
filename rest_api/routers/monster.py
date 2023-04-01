from fastapi import APIRouter, Depends, HTTPException
from utils import monster_crud
from models import model
from database import SessionLocal
from fastapi.responses import FileResponse

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/monster", tags=["Monster Endpoints"])


@router.get("/{monster_name}")
async def get_monster(monster_name: str, db: get_db = Depends()):
    result = monster_crud.get_monster(monster_name, db)
    if result:
        return FileResponse("./monstruleti/"+result.name)
    else:
        raise HTTPException(status_code=400, detail="Monster doesnt exist")

@router.get("/", response_model=model.AllMonsters)
async def get_all_monsters(db: get_db = Depends()):
    result = monster_crud.get_all_monsters(db)
    if result:
        return model.AllMonsters(name=[monster.name for monster in result])
    else:
        raise HTTPException(status_code=400, detail="Monsters doesnt exist")