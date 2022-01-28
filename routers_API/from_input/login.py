from typing import List, Optional,Dict
from pydantic import BaseModel,Json,ValidationError,validator
from datetime import date,datetime



class UserInfoBase(BaseModel):
    username: str
    fullname: str
    class Config():
        orm_mode = True


class UserCreate(UserInfoBase):
    password: str


class UserInfo(UserInfoBase):
    id: int

class login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None