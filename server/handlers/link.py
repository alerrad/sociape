from bson.objectid import ObjectId

from .config import db


user_collection = db.get_collection("users")


async def add_link(uid: str, link: dict) -> bool:
    try:
        await user_collection.find_one_and_update(
            {"_id": ObjectId(uid)}, {"$push": {"links": link}}
        )
        return True
    except Exception as err:
        print(err)
        return False


async def remove_link(uid: str, link_title: str) -> bool:
    try:
        await user_collection.find_one_and_update(
            {"_id": ObjectId(uid)}, {"$pull": {"links": {"title": link_title}}}
        )
        return True
    except Exception as err:
        print(err)
        return False
