from fastapi import APIRouter

router = APIRouter()

@router.get("/id")
def get_id():
    return {"id" : 1}

@router.get("/auth/login")
def get_login():
    return {"login" : "login"}

@router.post("/auth/signup")
def post_signup():
    return {"signup" : "signup"}