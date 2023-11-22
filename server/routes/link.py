from fastapi import APIRouter, Security
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2AuthorizationCodeBearer as CodeBearer

from handlers import add_link, remove_link
from models import LinkSchema
from utils import verify_token


link_router = APIRouter(prefix="/link")
bearer = CodeBearer("authorize", tokenUrl="token")


@link_router.post("/add")
async def add_user_link(link: LinkSchema, token: str = Security(bearer)):
    if not token:
        return {"success": False, "message": "No token"}

    payload = verify_token(token)
    if payload is None:
        return {"success": False, "message": "Bad token"}

    uid: str = payload["id"]
    res = await add_link(uid, jsonable_encoder(link))

    if res:
        return {"success": True, "message": "Link added"}

    return {"success": False, "message": "Error occured"}


@link_router.delete("/remove")
async def remove_user_link(link: LinkSchema, token: str = Security(bearer)):
    if not token:
        return {"success": False, "message": "No token"}

    payload = verify_token(token)
    if payload is None:
        return {"success": False, "message": "Bad token"}

    uid: str = payload["id"]
    res = await remove_link(uid, jsonable_encoder(link))

    if res:
        return {"success": True, "message": "Link removed"}

    return {"success": False, "message": "Error occured"}
