from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from .link import LinkSchema


class UserSchema(BaseModel):
    username: str = Field()
    bio: str = Field("")
    links: list[LinkSchema] = Field([])
    email: EmailStr = Field()
    password: str = Field()
    verified: bool = Field(False)
