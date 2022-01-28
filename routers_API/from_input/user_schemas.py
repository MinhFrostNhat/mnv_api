from typing import List, Optional,Dict
from pydantic import BaseModel,Json,validator





class UserInfoBase(BaseModel):
    username: str
    

    class Config():
        orm_mode = True


class UserCreate(UserInfoBase):
    password: str

    @validator('username', 'password')
    def user_no_(cls, u):
        if not u:
            raise ValueError(f'username or password can not blank')
        return u
    class Config():
        orm_mode = True


class Show_user(BaseModel):
    username: str
    class Config():
        orm_mode = True