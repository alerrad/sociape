from dotenv import get_key
from fastapi import APIRouter, FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routes import link_router, user_router

app = FastAPI()

# Register API routes
app.include_router(user_router, prefix="/api")
app.include_router(link_router, prefix="/api")

# Connect db
MONGO_URI = get_key(".env", "MONGO_URI")
db_client = AsyncIOMotorClient(MONGO_URI)
db = db_client.get_database("sociape")

try:
    db_client.admin.command("ping")
    print("Pinged your deployment, connected to db!")
except Exception as err:
    print(err)

# uvicorn main:app --reload
