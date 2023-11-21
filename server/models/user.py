from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr, Field

from .link import LinkSchema


class UserSchema(BaseModel):
    username: str = Field(...)
    fullname: str = Field(...)
    bio: str = Field("")
    email: EmailStr = Field(...)
    avatar: str = Field("")
    links: list[LinkSchema] = Field([])
    likes: list[ObjectId] = Field([])
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "flowjackson",
                "fullname": "Zhalgas",
                "bio": "I am a good boi",
                "links": [],
                "likes": [],
                "avatar": "",
                "email": "someemail@gmail.com",
                "password": "12345678",
            }
        }
