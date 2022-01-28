from typing import List, Optional,Dict
from pydantic import  BaseModel
from datetime import date,datetime
from uuid import UUID
import uuid
from .product_schemas import product
from .user_schemas import Show_user


class Cart(BaseModel):
    quantity: int
    

    class Config():
        orm_mode = True


class Show(BaseModel):
    quantity : int
   



    class Config():
        orm_mode = True