from fastapi import APIRouter, Depends, HTTPException
import math
from .hitboutik_api_class import HiboutikApi
from user.user_router import decode_jwt


# prefix="/hiboutik"
router = APIRouter()

@router.get("/search_customers_by_lastName/{lastName}")
async def get_customers_by_lastName(lastName : str, token_data: dict = Depends(decode_jwt)):
    if lastName is None or lastName == '':
        raise HTTPException(status_code=400, detail="Bad Request : lastName is empty")
    r = HiboutikApi.get('/customers/search/?last_name=' + lastName)
    return r.json()

@router.get("/get_customer_sales/{customer_id}/{page_number}")
async def get_customer_sales(customer_id : int, page_number : int, token_data: dict = Depends(decode_jwt)):
    HIBOUTIK_API_NUMBER_OF_SALES_PER_PAGE = 250
    MY_API_NUMBER_OF_SALES_PER_PAGE = 5
    if customer_id is None or customer_id == '' or type(customer_id) is not int or customer_id < 0:
        raise HTTPException(status_code=400, detail="Bad Request : Bad customer_id")
    if page_number is None or page_number == '' or type(page_number) is not int or page_number < 0:
        raise HTTPException(status_code=400, detail="Bad Request : Bad page_number")
    hiboutik_api_page = math.floor(page_number / (HIBOUTIK_API_NUMBER_OF_SALES_PER_PAGE + 1)) + 1
    r = HiboutikApi.get('/customer/' + str(customer_id) + '/sales/', {'p' : hiboutik_api_page})
    index_last_sales = ((page_number * MY_API_NUMBER_OF_SALES_PER_PAGE) % HIBOUTIK_API_NUMBER_OF_SALES_PER_PAGE)
    index_start_sales = index_last_sales - MY_API_NUMBER_OF_SALES_PER_PAGE
    return r.json()[index_start_sales:index_last_sales]



