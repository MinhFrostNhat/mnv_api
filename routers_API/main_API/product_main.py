from fastapi import APIRouter
from ..models import product_models
from ..database import get_db
from ..schemas import product_schemas,login
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response,Cookie
from ..crud_API import product_crud
from  fastapi.responses import ORJSONResponse

from .. import header
router = APIRouter(
    tags=['Product'],
    prefix="/product"
)

@router.post("/create",status_code=status.HTTP_201_CREATED)
def create_question(id:str, request : product_schemas.product, db :Session = Depends(get_db),get_current_user : login.UserCreate = Depends(
    header.get_current_user)):
    return product_crud.create_product_crud(request,db)


@router.get("/getall",status_code=status.HTTP_200_OK,response_model=List[product_schemas.product])
def getall_question( db: Session = Depends(get_db),get_current_user : login.UserCreate = Depends(
   header.get_current_user)):
    return product_crud.getall_product_crud(db)
