from fastapi import APIRouter
from ..models import user_models
from ..database import get_db
from ..schemas import user_schemas,login
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response,Cookie
from ..crud_API import user_crud
from  fastapi.responses import ORJSONResponse

from .. import header
router = APIRouter(
    tags=['User'],
    prefix="/user"
)

@router.post("/create", status_code=status.HTTP_200_OK,response_class=ORJSONResponse)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
        db_user = user_crud.get_user_by_username(db, username=user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")

        return user_crud.create_user(db=db, user=user)


@router.get('/getall',tags=['User'],response_model=List[user_schemas.Show_user])
def get_all_user(db: Session = Depends(get_db),get_current_user : login.UserCreate = Depends(
    header.get_current_user)):
    return user_crud.get_all_user(db)

@router.get('/get-spec-user/{id}',response_model=user_schemas.Show_user,status_code=status.HTTP_200_OK)
def list_spec_user(id:int, respone: Response, db: Session = Depends(get_db), get_current_user : login.UserCreate = Depends(
    header.get_current_user)):
    return user_crud.list_spec_user_crud(id,db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id, requests: user_schemas.UserCreate, db: Session = Depends(get_db), get_current_user : login.UserCreate = Depends(
    header.get_current_user)):
    return user_crud.update_user_crud(id,requests,db)

@router.delete("/delete/{id}",status_code=status.HTTP_202_ACCEPTED)
def delete(id, response: Response, db: Session = Depends(get_db),get_current_user : login.UserCreate = Depends(
    header.get_current_user)):
    return user_crud.delete_crud(id,db)


