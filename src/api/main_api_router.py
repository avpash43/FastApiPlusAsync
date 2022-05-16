import typing

from fastapi import APIRouter
from src.handler import url_handler
from src.domain.url_model import UrlDto, UrlEntity

router = APIRouter(
    prefix="/v1/url",
    tags=["url"],
    responses={404: {"description": "Not found"}},
)


@router.post("/make-request-by_list", response_model=list[dict])
async def get_responses_by_url_list(urls: list[str]):
    return await url_handler.make_request_by_urls(urls)


@router.post("/save-url-response-to_db", response_model=list[typing.Any])
async def save_url_responses_to_db(model_list: list[UrlDto]):
    return await url_handler.save_url_responses_to_db(model_list)


@router.get("/get-all-url-responses", response_model=list[UrlEntity])
async def get_all_url_responses():
    return await url_handler.get_all_url_responses()


@router.delete("/delete-url-response-by-id/{url_id}", response_model=typing.Any)
async def get_all_url_responses(url_id: int):
    return await url_handler.delete_url_response_by_id(url_id)


@router.get("/fill-agg-table", response_model=typing.Any)
async def get_all_url_responses():
    return await url_handler.fill_agg_table()
