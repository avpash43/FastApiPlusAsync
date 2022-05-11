from fastapi import APIRouter
from src.handler.url_handler import UrlHandler
from src.model.url_model import UrlModel

router = APIRouter(
    prefix="/v1/url",
    tags=["url"],
    responses={404: {"description": "Not found"}},
)


@router.post("/make_request_by_list")
async def add_url_list(urls: list[str]) -> list[dict]:
    return await UrlHandler().make_request_by_urls(urls)


@router.post("/save_response_to_db")
async def update_item(model_list: list[UrlModel]) -> str:
    return await UrlHandler().save_response_to_db(model_list)
