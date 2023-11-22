from bson.objectid import ObjectId
from passlib.context import CryptContext

from .config import db


user_collection = db.get_collection("users")
bcrypt_context = CryptContext(schemes=["bcrypt"])


def user_helper(user: dict) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "fullname": user["fullname"],
        "bio": user["bio"],
        "avatar": user["avatar"],
        "links": user["links"],
        "likes": list(map(str, user["likes"])),
        "email": user["email"],
    }


async def login_user(username: str, password: str) -> dict | bool:
    user = await user_collection.find_one({"username": username})

    if not user:
        return False

    if bcrypt_context.verify(password, user["password"]):
        return user_helper(user)

    return False


async def register_user(user_data: dict) -> bool:
    user = await user_collection.find_one({"username": user_data["username"]})

    if user:
        return False

    user_data["password"] = bcrypt_context.hash(user_data["password"])

    try:
        await user_collection.insert_one(user_data)
        return True
    except Exception as err:
        print(err)
        return False


async def get_user(username: str) -> dict | None:
    user = await user_collection.find_one({"username": username})
    return user_helper(user) if user else None


async def update_profile(uid: str, updated_fields: dict) -> bool:
    if len(updated_fields) < 1:
        return False

    try:
        await user_collection.find_one_and_update(
            {"_id": ObjectId(uid)}, {"$set": updated_fields}
        )
        return True
    except Exception as err:
        print(err)
        return False


async def like_profile(uid: str, profile_uid: str) -> bool:
    try:
        user_id, profile_id = ObjectId(uid), ObjectId(profile_uid)
        profile = await user_collection.find_one({"_id": profile_id})

        if profile is None:
            return False

        if user_id in profile["likes"]:
            await user_collection.find_one_and_update(
                {"_id": profile_id}, {"$pull": {"likes": user_id}}
            )

        else:
            await user_collection.find_one_and_update(
                {"_id": profile_id}, {"$push": {"likes": user_id}}
            )

        return True

    except Exception as err:
        print(err)
        return False
