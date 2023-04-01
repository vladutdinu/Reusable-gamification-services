from fastapi import APIRouter, Depends, HTTPException, Response
from utils import token_crud
from models import model
from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/token", tags=["Token Endpoints"])

@router.post("/", response_model=model.Token)
async def create_item(token: model.Token, db: get_db = Depends()):
    result = token_crud.get_token(token.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Token already exist")
    return token_crud.create_token(token, db).__dict__

@router.get("/{token_id}", response_model=model.Token)
async def get_item(token_id: int, db: get_db = Depends()):
    result = token_crud.get_token(token_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="Token doesnt exist")

@router.put("/", response_model=model.Token)
async def get_item(token: model.Token, db: get_db = Depends()):
    result = token_crud.update_token(token, db)
    if result:
        return token_crud.get_token(token.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Token doesnt exist")

@router.delete("/{token_id}", response_model=model.Token)
async def get_item(token_id: int, db: get_db = Depends()):
    result = token_crud.delete_token(token_id, db)
    if result:
        return Response("Token deleted")
    else:
        raise HTTPException(status_code=400, detail="Token doesnt exist")