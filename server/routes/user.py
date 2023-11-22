import secrets

from fastapi import APIRouter, File, Security, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2AuthorizationCodeBearer as CodeBearer

from handlers import (get_user, like_profile, login_user, register_user,
                      update_profile,)
from models import UpdateUserSchema, UserLogin, UserSchema
from utils import sign_token, verify_token


user_router = APIRouter(prefix="/user")
bearer = CodeBearer("authorize", tokenUrl="token")


@user_router.get("/{username}")
async def get_user_data(username: str):
    user = await get_user(username)

    if user:
        return {"success": True, "data": user}

    return {"success": False, "message": "User not found"}


@user_router.post("/register")
async def register(user_data: UserSchema):
    res = await register_user(jsonable_encoder(user_data))

    if res:
        return {"success": True, "message": "Added new user"}

    return {"success": False, "message": "Failed to register"}


@user_router.post("/login")
async def login(user_data: UserLogin):
    res = await login_user(user_data.username, user_data.password)

    if res:
        token = sign_token({"id": res["id"], "username": res["username"]})

        return {"success": True, "token": token, "data": res}

    return {"success": False, "message": "Incorrect username or password"}


@user_router.post("/like/{profile_id}")
async def like_user_profile(profile_id: str, token: str = Security(bearer)):
    if not token:
        return {"success": False, "message": "No token"}

    payload = verify_token(token)
    if payload is None:
        return {"success": False, "message": "Bad token"}

    user_id = payload["id"]
    res = await like_profile(user_id, profile_id)

    if res:
        return {"success": True, "message": "(dis)Liked profile!"}

    return {"success": False, "message": "Error occured!"}


@user_router.patch("/update-profile")
async def modify_profile(
    data: UpdateUserSchema,
    token: str = Security(bearer),
):
    if not token:
        return {"success": False, "message": "No token"}

    payload = verify_token(token)

    if payload is None:
        return {"success": False, "message": "Bad token"}

    user_id: str = payload["id"]
    res = await update_profile(user_id, jsonable_encoder(data))

    if res:
        return {"success": True, "message": "Update profile!"}

    return {"success": False, "message": "Error occured!"}


@user_router.patch("/update-avatar")
async def update_avatar(
    picture: UploadFile = File(...),
    token: str = Security(bearer),
):
    if not token:
        return {"success": False, "message": "No token"}

    payload = verify_token(token)

    if payload is None:
        return {"success": False, "message": "Bad token"}

    user_id: str = payload["id"]

    file_name = secrets.token_hex(8) + picture.filename
    contents = await picture.read()

    with open(f"./uploads/{file_name}", "wb") as f:
        f.write(contents)

    res = await update_profile(user_id, {"avatar": file_name})

    if res:
        return {"success": True, "message": "Updated profile pic"}

    return {"success": False, "message": "Failed to update profile pic"}
