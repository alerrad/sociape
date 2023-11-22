from pydantic import BaseModel, Field


class LinkSchema(BaseModel):
    icon: str = Field(...)
    title: str = Field(...)
    url: str = Field(...)
