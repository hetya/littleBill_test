from fastapi import APIRouter
from hiboutik.hitboutik_api_class import HiboutikApi

# hiboutik_router = APIRouter(prefix="/hiboutik")
router = APIRouter()

@router.get("/search_customers_by_lastName/{lastName}")
async def get_customers_by_lastName(lastName : str):
    if lastName is None or lastName == '':
        raise HTTPException(status_code=400, detail="Bad Request : lastName is empty")
    r = HiboutikApi.get('/customers/search/?last_name=' + lastName)
    return r.json()

@router.get("/get_customer_sales/{customer_id}")
def get_customer_sales(customer_id : int):
    r = HiboutikApi.get('/customer/' + str(customer_id), {'p' : '1'})
    return r.json()

@router.get("/create_sales/{customer_id}/{quantity}")
def create_sales(customer_id : int, quantity : int):
    # for i in range(quantity):
        # r = HiboutikApi.post('/sales', {'store_id' : 1, 'customer_id' : customer_id, 'currency_code' : 'EUR'})
    r = HiboutikApi.post('/sales', {'store_id' : 1, 'customer_id' : customer_id, 'currency_code' : 'EUR'})
    print(r.json())
    return "sales created"