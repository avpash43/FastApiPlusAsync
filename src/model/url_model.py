from pydantic import BaseModel


class UrlModel(BaseModel):
    url: str
    status: int
    content_type: str
