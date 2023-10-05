from fastapi import FastAPI, Depends
from hiboutik import hiboutik_router
from user import user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hiboutik_router.router, prefix="/hiboutik")
app.include_router(user_router.router, prefix="/user")

@app.get("/")
async def read_root():
    return {"Hello" : "World"}
