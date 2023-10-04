from fastapi import FastAPI
from hiboutik import hiboutik_router
from user import user_router

app = FastAPI()

app.include_router(hiboutik_router.router, prefix="/hiboutik")
app.include_router(user_router.router, prefix="/user")

@app.get("/")
def read_root():
    return {"Hello" : "World"}

from pymongo import MongoClient
import os
if (MONGO_URI := os.environ.get('MONGODB_URI')) is not None:
    client = MongoClient(MONGO_URI)
else:
    # pass
    print (MONGO_URI)

dbs = client.list_database_names()
print(dbs)