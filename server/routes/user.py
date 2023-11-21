from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from handlers import get_user, register_user
from models import UserSchema


user_router = APIRouter(prefix="/user")


@user_router.get("/{username}")
async def get_user_data(username: str):
    user = await get_user(username)

    if user:
        return {"success": True, "data": user}

    return {"success": False, "message": "User not found"}


@user_router.post("/register")
async def register(user: UserSchema):
    res = await register_user(jsonable_encoder(user))

    if res:
        return {"success": True, "message": "Added new user"}

    return {"success": False, "message": "Failed to register"}


@user_router.post("/login")
async def login():
    pass


@user_router.post("/{username}/like")
async def like_profile():
    pass
