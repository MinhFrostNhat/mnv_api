
from sqlalchemy import Column, DateTime, String,Float,Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from ..database import Base
from uuid import UUID
from fastapi_utils.guid_type import GUID,GUID_DEFAULT_SQLITE

class CartModel(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(GUID,default=GUID_DEFAULT_SQLITE)
    quantity = Column(Integer)
    
    
