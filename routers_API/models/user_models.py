from sqlalchemy import Column, Integer, String,ForeignKey,BOOLEAN,NVARCHAR,VARCHAR,DATE
from ..database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class userinfo(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True,)
    username = Column(String(225), unique=True)
    password = Column(String(255))

    