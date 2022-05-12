import typing

from fastapi import APIRouter
from src.handler.url_handler import UrlHandler
from src.domain.url_model import UrlDto, UrlEntity

router = APIRouter(
    prefix="/v1/url",
    tags=["url"],
    responses={404: {"description": "Not found"}},
)


@router.post("/make_request_by_list", response_model=list[dict])
async def get_responses_by_url_list(urls: list[str]):
    return await UrlHandler().make_request_by_urls(urls)


@router.post("/save_url_response_to_db", response_model=list[typing.Any])
async def save_url_responses_to_db(model_list: list[UrlDto]):
    return await UrlHandler().save_url_responses_to_db(model_list)


@router.get("/get_all_url_responses", response_model=list[UrlEntity])
async def get_all_url_responses():
    return await UrlHandler().get_all_url_responses()


@router.delete("/delete_url_response_by_id/{url_id}", response_model=typing.Any)
async def get_all_url_responses(url_id: int):
    return await UrlHandler().delete_url_response_by_id(url_id)


@router.get("/fill_agg_table", response_model=typing.Any)
async def get_all_url_responses():
    return await UrlHandler().fill_agg_table()
