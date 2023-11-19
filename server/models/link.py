from pydantic import BaseModel, Field


class LinkSchema(BaseModel):
    icon: str = Field(...)
    title: str = Field(...)
    url: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "icon": "/youtube.png",
                "title": "My YT channel",
                "url": "https://youtube.com/alerrad",
            }
        }
