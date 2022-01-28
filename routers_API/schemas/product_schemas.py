from pydoc import text

from typing import List, Optional,Dict
from pydantic import UUID1, BaseModel,Json,ValidationError,validator
from datetime import date,datetime

import uuid



class product(BaseModel):
    name : str
    price : float
    class Config():
        orm_mode = True


class Show_subject(BaseModel):
    name : str
    price : float
    class Config():
        orm_mode = True
