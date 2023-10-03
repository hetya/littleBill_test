from fastapi import APIRouter
from hiboutik.hitboutik_api_class import HiboutikApi

# hiboutik_router = APIRouter(prefix="/hiboutik")
router = APIRouter()

@router.get("/search_customers_by_lastName/{lastName}")
async def get_customers_by_lastName(lastName : str):
    if lastName is None or lastName == '':
        raise HTTPException(status_code=400, detail="Bad Request : lastName is empty")
    try:
        r = HiboutikApi.get('/customers/search/?last_name=' + lastName)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    print(r.status_code)
    print(r.json())
    return r.json()


