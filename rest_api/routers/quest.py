from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from utils import quest_crud
from models import model
from database import SessionLocal

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/quest", tags=["Quest Endpoints"])


@router.post("/", response_model=model.Quest)
async def create_quest(quest: model.Quest, db: get_db = Depends()):
    result = quest_crud.get_quest(quest.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Quest already exist")
    return quest_crud.create_quest(quest, db).__dict__


@router.get("/{quest_id}", response_model=model.Quest)
async def get_quest(quest_id: int, db: get_db = Depends()):
    result = quest_crud.get_quest(quest_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="Quest doesnt exist")

@router.get("/all/{customer_id}", response_model=List[model.Quest])
async def get_quests_customer(customer_id: int, db: get_db = Depends()):
    result = quest_crud.get_quests_customer(customer_id, db)
    if result:
        return [quest.__dict__ for quest in result]
    else:
        raise HTTPException(status_code=400, detail="No quests")

@router.put("/", response_model=model.Quest)
async def update_quest(quest: model.Quest, db: get_db = Depends()):
    result = quest_crud.update_quest(quest, db)
    if result:
        return quest_crud.get_quest(quest.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Quest doesnt exist")

@router.put("/", response_model=model.Quest)
async def update_quest_status(quest_id: int, db: get_db = Depends()):
    result = quest_crud.update_quest_status(quest_id, db)
    if result:
        return quest_crud.get_quest(quest_id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Quest doesnt exist")

@router.delete("/{quest_id}", response_model=model.Quest)
async def delete_quest(quest_id: int, db: get_db = Depends()):
    result = quest_crud.delete_quest(quest_id, db)
    if result:
        return Response("Quest deleted")
    else:
        raise HTTPException(status_code=400, detail="Quest doesnt exist")
