from fastapi import APIRouter
from src.handler.UrlHandler import UrlHandler

router = APIRouter(
    prefix="/v1/url",
    tags=["url"],
    responses={404: {"description": "Not found"}},
)


@router.post("/make_request_by_list")
async def add_url_list(urls: list[str]):
    return await UrlHandler().make_request_by_urls(urls)

