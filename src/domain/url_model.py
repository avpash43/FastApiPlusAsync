from pydantic import BaseModel


class UrlEntity(BaseModel):
    id: int
    url: str
    status: int
    content_type: str


class UrlDto(BaseModel):
    url: str
    status: int
    content_type: str
