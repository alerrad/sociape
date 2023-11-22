from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient


# Connect to db
db_client = AsyncIOMotorClient(getenv("MONGO_URI"))
db = db_client.get_database("sociape")
