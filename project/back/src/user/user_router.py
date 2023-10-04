from fastapi import APIRouter
from mongodb.mongo import Mongo
from pydantic import BaseModel
import pprint


router = APIRouter()

class IUser(BaseModel):
    login : str
    password : str
    user_id : int | None = None

# @router.get("/id")
# def get_id():
#     return {"id" : 1}

@router.get("/auth/login") # TODO : add jwt
def login(user : IUser):
    try:
        Mongo().get_users_collection().find_one({"login" : user.login, "password" : user.password})
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request : login or password is incorrect")
    return {"login" : "login"}

@router.post("/auth/signup")
def signup( user : IUser): # TODO: add username filter for characters like whitespaces, etc.
    if user.login is None or user.login == '' or user.login.len > 120 :
        raise HTTPException(status_code=400, detail="Bad Request : login is empty or too long")
    if user.password is None or user.password == ''or user.login.len > 120:
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
