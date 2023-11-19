from fastapi import APIRouter


user_router = APIRouter(prefix="/user")


@user_router.get("/{username}")
async def get_user(username: str):
    pass


@user_router.post("/register")
async def register():
    pass


@user_router.post("/login")
async def login():
    pass


@user_router.post("/{username}/like")
async def like_profile():
    pass
