import asyncio
from os import getenv

from dotenv import load_dotenv
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Database
from uvicorn import run

from routes import link_router, user_router


# Load .env file
load_dotenv()

app = FastAPI()

# Register API routes
app.include_router(user_router, prefix="/api")
app.include_router(link_router, prefix="/api")


# Connect db
async def ping_connection() -> Database | None:
    try:
        db_client = AsyncIOMotorClient(getenv("MONGO_URI"))
        await db_client.admin.command("ping")
        print("Pinged your deployment, connected to db!")
        return db_client.get_database("sociape")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    db = asyncio.run(ping_connection())
    run(app)
