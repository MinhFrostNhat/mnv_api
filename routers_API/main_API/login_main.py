from fastapi import APIRouter
from .. import jwttoken

from fastapi.security import OAuth2PasswordRequestForm
from ..database import get_db
from  ..models import user_models
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response
router = APIRouter()




@router.post("/login",status_code=status.HTTP_200_OK,tags=['login'])
def login_sys(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    userr = db.query(user_models.userinfo).filter(user_models.userinfo.username == request.username).first()
    if not userr:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"incorrect username")
    userr = db.query(user_models.userinfo).filter(user_models.userinfo.password == request.password).first()
    if not userr:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"incorrect password")

    access_token = jwttoken.create_access_token(data={"sub": userr.username})
    return {"access_token": access_token, "token_type": "bearer"}