from fastapi import APIRouter

from ..models import user_models
from ..database import get_db
from ..from_input import user_schemas
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response


def get_user_by_username(db: Session, username: str):
    return db.query(user_models.userinfo).filter(user_models.userinfo.username == username).first()


def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = user_models.userinfo(username=user.username,password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "successfull"


def get_all_user(db: Session = Depends(get_db)):
    get_all=db.query(user_models.userinfo).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not have data to get")
    return get_all


def list_spec_user_crud(id:int, db: Session = Depends(get_db)):
    get_spec_user = db.query(user_models.userinfo).filter(user_models.userinfo.id == id).first()
    if not get_spec_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    return get_spec_user

def update_user_crud(id, requests: user_schemas.UserCreate, db: Session = Depends(get_db)):
    update_user_info=db.query(user_models.userinfo).filter(user_models.userinfo.id == id)
    if not update_user_info.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    update_user_info.update({"id":id,"password":requests.password})
    db.commit()
    return "good update successful"

def delete_crud(id, db: Session = Depends(get_db)):
    delete_user_info = db.query(user_models.userinfo).filter(user_models.userinfo.id == id).delete(synchronize_session=False)
    if not delete_user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    db.commit()
    return "delete successful"