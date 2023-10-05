from fastapi.testclient import TestClient
from fastapi import status
from ..main import app
import pytest

client = TestClient(app)
headers={}

def test_home_missing_header():
    response = client.get("/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_home_bad_header():
    response = client.get("/", headers={"Authorization": "Bearer dummy_value"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_login():
    global headers
    response = client.post("/user/auth/login", json={"login" : "aaa", "password" : "aaa"})
    assert response.status_code == status.HTTP_200_OK
    headers = {"Authorization": "Bearer " + response.json()['access_token']}

def test_home():
    response = client.get("/", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Hello" : "World"}

def test_get_customers_by_lastName():
    response = client.get("/hiboutik/search_customers_by_lastName/Didierjean", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "customers_id": 5,
            "last_name": "Didierjean",
            "first_name": "Thibaud",
            "email": "dj.t@tech.io",
            "phone": "0765454345",
            "vat": "",
            "country": "FRA",
            "date_of_birth": "0000-00-00",
            "validity": "0000-00-00",
            "loyalty_points": 0,
            "intial_loyalty_points": 0,
            "prepaid_purchases": "0.00",
            "store_credit": "0.00",
            "customers_ref_ext": "",
            "last_order_date": "0000-00-00",
            "customers_code": ""
        },
        {
            "customers_id": 7,
            "last_name": "Didierjean",
            "first_name": "Maxime",
            "email": "didierjean@gmail.com",
            "phone": "0245638657",
            "vat": "",
            "country": "FRA",
            "date_of_birth": "0000-00-00",
            "validity": "0000-00-00",
            "loyalty_points": 101,
            "intial_loyalty_points": 0,
            "prepaid_purchases": "0.00",
            "store_credit": "0.00",
            "customers_ref_ext": "",
            "last_order_date": "2023-06-28",
            "customers_code": ""
        }
    ]

def test_get_customer_sales_empty_customer():
    response = client.get("/hiboutik/get_customer_sales/10/1", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

def test_get_customer_sales_empty_customer_page_2():
    response = client.get("/hiboutik/get_customer_sales/10/2", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

def test_get_customer_sales_customer_with_3_sales():
    response = client.get("/hiboutik/get_customer_sales/3/1", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
    {
        "sale_id": 11,
        "created_at": "2023-06-28 16:03:54",
        "completed_at": "2023-06-28 16:04:29",
        "date_z": 20230628,
        "store_id": 1,
        "vendor_id": 1,
        "unique_sale_id": "2023-06-1-5",
        "customer_id": 3,
        "currency": "EUR",
        "total": "47.00",
        "billing_address": 0,
        "shipping_address": 0
    },
    {
        "sale_id": 9,
        "created_at": "2023-06-28 16:03:33",
        "completed_at": "2023-06-28 16:04:40",
        "date_z": 20230628,
        "store_id": 1,
        "vendor_id": 1,
        "unique_sale_id": "2023-06-1-6",
        "customer_id": 3,
        "currency": "EUR",
        "total": "9.00",
        "billing_address": 0,
        "shipping_address": 0
    },
    {
        "sale_id": 2,
        "created_at": "2023-06-28 15:46:18",
        "completed_at": "2023-06-28 16:05:38",
        "date_z": 20230628,
        "store_id": 1,
        "vendor_id": 1,
        "unique_sale_id": "2023-06-1-10",
        "customer_id": 3,
        "currency": "EUR",
        "total": "42.00",
        "billing_address": 0,
        "shipping_address": 0
    }
]

def test_get_customer_sales_customer_with_6_sales_page_2():
    response = client.get("/hiboutik/get_customer_sales/2/2", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
    {
        "sale_id": 1,
        "created_at": "2023-06-28 15:34:50",
        "completed_at": "2023-06-28 16:06:50",
        "date_z": 20230628,
        "store_id": 1,
        "vendor_id": 1,
        "unique_sale_id": "2023-06-1-12",
        "customer_id": 2,
        "currency": "EUR",
        "total": "34.00",
        "billing_address": 0,
        "shipping_address": 0
    }
]