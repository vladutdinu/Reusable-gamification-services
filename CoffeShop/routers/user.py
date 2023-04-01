from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from utils import user_crud
from models import model
from database import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/user", tags=["User Endpoints"])
@router.post("/")
async def SignUp(user:model.UserSignUp, db: get_db = Depends()):
    result = user_crud.get_user_by_email(user.email, get_db)
    if result:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    return user_crud.create_user(model.User(name=user.name,
       password=user.password,
       ranking=user_crud.get_last_ranking(db)+1), db)
@router.post("/")
async def LogIn(user:model.UserLogIn, db: get_db = Depends()):
    result = user_crud.get_user_by_email(user.email, get_db)
    if result:
        if result.password!=user.password:
            raise HTTPException(status_code=400, detail="Password incorect")
            
        else:
            return 1    
    else:
        raise HTTPException(status_code=400, detail="User with this email doesnt exist")
@router.get("/{user_email}", response_model=model.User)
async def get_user_by_email(user_email: str, db: get_db = Depends()):
    result = user_crud.get_product_by_email(user_email, db)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="User doesnt exist")
@router.put("/", response_model=model.User)
async def update_user(user: model.User, db: get_db = Depends()):
    result = user_crud.update_user(user, db)
    if result:
        return user_crud.get_user_by_id(user.id, db)
    else:
        raise HTTPException(status_code=400, detail="User doesnt exist")

@router.delete("/{user_id}", response_model=model.Product)
async def delete_product(user_id: int, db: get_db = Depends()):
    result = user_crud.delete_user(user_id, db)
    if result:
        return Response("User deleted")
    else:
        raise HTTPException(status_code=400, detail="User doesnt exist")
    