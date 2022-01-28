from fastapi import APIRouter
from ..models import cart_models
from ..database import get_db
from ..schemas import cart_schemas,login
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response,Cookie
from ..crud_API import cart_crud
from  fastapi.responses import ORJSONResponse

from .. import header
router = APIRouter(
    tags=['Cart'],
    prefix="/cart"
)

@router.post("/createCartItem",status_code=status.HTTP_201_CREATED)
def create_cart(id:int, request : cart_schemas.Cart, db :Session = Depends(get_db),get_current_user : login.UserCreate = Depends(
    header.get_current_user)):
    return cart_crud.create_cart(id,request,db,)


@router.get("/getallCartItem",status_code=status.HTTP_200_OK,response_model=List[cart_schemas.Cart])
def getall_all( db: Session = Depends(get_db),get_current_user : login.UserCreate = Depends(
   header.get_current_user)):
    return cart_crud.get_all_cart(db)


@router.put("/cartItem",status_code=status.HTTP_200_OK)
def update_cart(id:int, response: Response, request: cart_schemas.Cart, db:Session =Depends(get_db),get_current_user : login.UserCreate = Depends(
    header.get_current_user)):
    return cart_crud.update_cart_crud(id,request,db)


@router.delete("/delete/cart/{id}",status_code= status.HTTP_202_ACCEPTED)
def delete_cart(id: int,db: Session = Depends(get_db), get_current_user : login.UserCreate = Depends(
    header.get_current_user)):
    return cart_crud.delete_cart(id,db)
