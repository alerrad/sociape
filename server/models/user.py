from typing import Optional

from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(...)
    fullname: str = Field(...)
    bio: str = Field("")
    email: str = Field(...)
    avatar: str = Field("")
    links: list[dict] = Field([])
    likes: list[str] = Field([])
    password: str = Field(...)


class UserLogin(BaseModel):
    username: str = Field(...)
    password: str = Field(...)


class UpdateUserSchema(BaseModel):
    fullname: str = Optional[str]
    bio: str = Optional[str]
    email: str = Optional[str]
    avatar: str = Optional[str]
