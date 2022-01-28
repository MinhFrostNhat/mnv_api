from re import I
from sqlalchemy import Column, DateTime, Integer, String,Float,VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from ..database import Base

from uuid import UUID
import uuid
from fastapi_utils.guid_type import GUID,GUID_DEFAULT_SQLITE

class ProductModel(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    prouuid = Column(GUID,default=GUID_DEFAULT_SQLITE)
    name = Column(String(255))
    price = Column(Float)

    

    