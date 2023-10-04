from pymongo import MongoClient
from fastapi import HTTPException
import os

class Mongo(MongoClient):
    def __init__(self):
        if (MONGO_URI := os.environ.get('MONGODB_URI')) is not None:
            super().__init__(MONGO_URI)
        else:
            super().__init__(MONGO_URI)
            raise Exception("MONGODB_URI is not set")
            raise HTTPException(status_code=500, detail="Internal Server Error")
        # super().__init__(MONGO_URI)
        self.users = self.users
        # self.users_collection = None
        self.hiboutik = self.hiboutik
        self.hiboutik_collection = self.hiboutik.hiboutik_collection
        try:
            self.users.users_collection.create_index([("login", 1)], unique=True)
        except DuplicateKeyError:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def get_users_collection(self):
        return self.users.users_collection
    
    def get_hiboutik_collection(self):
        # if self.hiboutik_collection is None:
            # self.hiboutik_collection = self.hiboutik.hiboutik_collection
        return self.hiboutik_collection