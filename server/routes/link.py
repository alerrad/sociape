from fastapi import APIRouter


link_router = APIRouter(prefix="/link")


@link_router.post("/add")
async def add_link():
    pass


@link_router.delete("/remove")
async def remove_link():
    pass


@link_router.get("/{username}")
async def get_user_links(username: str):
    pass
