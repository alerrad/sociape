from bson.objectid import ObjectId
from passlib.context import CryptContext

from main import db


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
        "likes": user["likes"],
        "email": user["email"],
        "verified": user["verified"],
    }


async def login_user(username: str, password: str) -> dict | bool:
    user = await user_collection.find_one({"username": username})

    if not user:
        return False

    if bcrypt_context.verify(password, user["password"]):
        return user_helper(user)

    return False


async def register_user(user_data: dict) -> str | bool:
    user = await user_collection.find_one({"username": user_data["username"]})

    if user:
        return False

    user_data["password"] = bcrypt_context.hash(user_data["password"])
    user_data["verified"] = False
    user_data["links"] = []
    user_data["likes"] = []
    user_data["avatar"] = ""
    user_data["bio"] = ""

    res = await user_collection.insert_one(user_data)
    return ObjectId(res.inserted_id)


async def get_user(username: str) -> dict | None:
    user = await user_collection.find_one({"username": username})
    return user_helper(user)


async def update_bio(uid: str, new_bio: str) -> bool:
    try:
        await user_collection.find_one_and_update(
            {"_id": ObjectId(uid)}, {"$set": {"bio": new_bio}}
        )
        return True
    except Exception as err:
        print(err)
        return False


async def update_fullname(uid: str, new_fullname: str) -> bool:
    try:
        await user_collection.find_one_and_update(
            {"_id": ObjectId(uid)}, {"$set": {"fullname": new_fullname}}
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
            if not profile["verified"] and len(profile["likes"]) + 1 >= 5:
                await user_collection.find_one_and_update(
                    {"_id": profile_id},
                    {"$push": {"likes": user_id}, "$set": {"verified": True}},
                )

            else:
                await user_collection.find_one_and_update(
                    {"_id": profile_id}, {"$push": {"likes": user_id}}
                )

        return True

    except Exception as err:
        print(err)
        return False


async def update_avatar(uid: str, new_avatar: str) -> bool:
    try:
        await user_collection.find_one_and_update(
            {"_id": ObjectId(uid)}, {"$set": {"avatar": new_avatar}}
        )
        return True
    except Exception as err:
        print(err)
        return False
