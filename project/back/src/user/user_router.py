from fastapi import APIRouter, HTTPException
from mongodb.mongo import Mongo
from pydantic import BaseModel
import pprint


router = APIRouter()

class IUser(BaseModel):
    login : str
    password : str

# @router.get("/id")
# def get_id():
#     return {"id" : 1}

@router.post("/auth/login") # TODO : add jwt
def login(user : IUser):
    try:
        user_data = Mongo().get_users_collection().find_one({"login" : user.login, "password" : user.password})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    if user_data is None:
        raise HTTPException(status_code=400, detail="Bad Request : login or password is incorrect")
    return {"connected"}

@router.post("/auth/signup")
def signup( user : IUser): # TODO: add username filter for characters like whitespaces, etc.
    if user.login is None or user.login == '' or len(user.login) > 120 :
        raise HTTPException(status_code=400, detail="Bad Request : login is empty or too long")
    if user.password is None or user.password == ''or len(user.login) > 120:
        raise HTTPException(status_code=400, detail="Bad Request : password is empty or too long")
    new_user = {
        "login" : user.login,
        "password" : user.password
    }
    try:
        Mongo().get_users_collection().insert_one(new_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request : login already exists")
    return {"signup" : "ok"}
