
from itertools import product
from ..models import cart_models,product_models
from ..database import get_db
from ..from_input import cart_schemas
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response


def create_cart(cart: cart_schemas.Cart,db :Session = Depends(get_db)):
    db_cart = cart_models.CartModel(quantity = cart.quantity,)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    userr =db.query(product_models.ProductModel).filter(product_models.ProductModel.price == 1000).first()
    user_cart =db.query(cart_models.CartModel).filter(cart_models.CartModel.id == 1).first()
    id_cart = user_cart.cart_id
    sub_price = userr.price * cart.quantity
    vat = sub_price *0.1
    total = vat + sub_price
    a = f" Cart_id : {id_cart},[ product_id:{userr.prouuid} ,price: {sub_price}, vat :{vat},total: {total}]"
    return a


def get_all_cart(db: Session = Depends(get_db)):
    get_all=db.query(cart_models.CartModel).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not have data to get!")
    return get_all


def update_cart_crud(id, request: cart_schemas.Cart, db:Session =Depends(get_db)):
    update_ques = db.query(cart_models.CartModel).filter(cart_models.CartModel.id == id)
    if not update_ques:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    update_ques.update({'id':id,'quantity': request.quantity})
    db.commit()
    userr =db.query(product_models.ProductModel).filter(product_models.ProductModel.price == 1000).first()
    
    user_cart =db.query(cart_models.CartModel).filter(cart_models.CartModel.id == 1).first()
    if not user_cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    id_cart = user_cart.cart_id
    sub_price = userr.price * request.quantity
    vat = sub_price *0.1
    total = vat + sub_price
    a = f" Cart_id : {id_cart},[ product_id:{userr.prouuid} ,price: {sub_price}, vat :{vat},total: {total}]"
    return a

def delete_cart(id: int,db: Session = Depends(get_db)):
    delete_cart_id = db.query(cart_models.CartModel).filter(cart_models.CartModel.id == id).delete(synchronize_session=False)
    if not delete_cart_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    db.commit()
    return "delete successful"