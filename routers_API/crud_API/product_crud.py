from fastapi import APIRouter

from ..models import product_models
from ..database import get_db
from ..schemas import product_schemas
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response
from uuid import UUID


def create_product_crud(request : product_schemas.product, db :Session = Depends(get_db)):
    newquestion = product_models.ProductModel(name = request.name, price = request.price,)
    db.add(newquestion)
    db.commit()
    return "Create successful"

def getall_product_crud( db: Session = Depends(get_db)):
    getall_ques = db.query(product_models.ProductModel).all()
    if not getall_ques:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not have data to get")
    return getall_ques