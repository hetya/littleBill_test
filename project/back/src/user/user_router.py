import os
import jwt
import bcrypt
import datetime
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Header
from mongodb.mongo import Mongo

router = APIRouter()

class IUser(BaseModel):
    login : str
    password : str


def create_jwt(user_id: str):
    SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 120
    if SECRET_KEY is None or ALGORITHM is None or ACCESS_TOKEN_EXPIRE_MINUTES is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": user_id,
        "exp": expiration_time
    }
    
    return {"access_token": jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)}

def decode_jwt(authorization: str = Header(None)):
    SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    ALGORITHM = "HS256"
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    if SECRET_KEY is None or ALGORITHM is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
        return None
    try:
        token_type, token = authorization.split()
        if token_type != "Bearer":
            raise HTTPException(status_code=401, detail="Invalid token type")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Unauthorized : token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Unauthorized : invalid token")
    return None


@router.post("/auth/login")
async def login(user : IUser):
    try:
        user_data = Mongo().get_users_collection().find_one({"login" : user.login})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    if user_data is None or not bcrypt.checkpw(user.password.encode('utf-8'), user_data['password']):
        raise HTTPException(status_code=400, detail="Bad Request : login or password is incorrect")
    return create_jwt(str(user_data['_id']))

@router.post("/auth/signup")
async def signup( user : IUser):
    if user.login is None or user.login == '' or len(user.login) > 120 :
        raise HTTPException(status_code=400, detail="Bad Request : login is empty or too long")
    if user.password is None or user.password == ''or len(user.login) > 120:
        raise HTTPException(status_code=400, detail="Bad Request : password is empty or too long")
    new_user = {
        "login" : user.login,
        "password" : bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    }
    try:
        new_user_id = Mongo().get_users_collection().insert_one(new_user).inserted_id
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request : login already exists")
    return create_jwt(str(new_user_id))
