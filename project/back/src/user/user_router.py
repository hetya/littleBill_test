import os
import jwt
import bcrypt
import datetime
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from mongodb.mongo import Mongo

router = APIRouter()

class IUser(BaseModel):
    login : str
    password : str

def create_jwt(user_id : str):
    SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 120
    if SECRET_KEY is None or ALGORITHM is None or ACCESS_TOKEN_EXPIRE_MINUTES is None:
        raise HTTPException(status_code=500, detail="Internal Server Error 2")
        return None
    data = {"sub": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            }
    return jwt.encode({"exp": ACCESS_TOKEN_EXPIRE_MINUTES}, SECRET_KEY, algorithm=ALGORITHM)
    


@router.post("/auth/login") # TODO : add jwt
def login(user : IUser):
    try:
        user_data = Mongo().get_users_collection().find_one({"login" : user.login})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error 1")
    if user_data is None or not bcrypt.checkpw(user.password.encode('utf-8'), user_data['password']):
        raise HTTPException(status_code=400, detail="Bad Request : login or password is incorrect")
    return create_jwt(str(user_data['_id']))

@router.post("/auth/signup")
def signup( user : IUser): # TODO: add username filter for characters like whitespaces, etc.
    if user.login is None or user.login == '' or len(user.login) > 120 :
        raise HTTPException(status_code=400, detail="Bad Request : login is empty or too long")
    if user.password is None or user.password == ''or len(user.login) > 120:
        raise HTTPException(status_code=400, detail="Bad Request : password is empty or too long")
    new_user = {
        "login" : user.login,
        "password" : bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    }
    try:
        Mongo().get_users_collection().insert_one(new_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request : login already exists")
    return {"signup" : "ok"}
