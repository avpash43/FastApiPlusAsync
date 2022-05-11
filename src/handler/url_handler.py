import typing
from src.adapter.http_client import HttpClient
from src.domain.url_model import UrlDto, UrlEntity
from src.repository.url_repository import UrlRepository


class UrlHandler:
    async def make_request_by_urls(self, urls: list[str]) -> list[dict]:
        result_list = []
        for url in urls:
            result: dict = await HttpClient().make_request_by_url(url)
            result_list.append(result)
        return result_list

    async def save_url_responses_to_db(self, model_list: list[UrlDto]) -> list[typing.Any]:
        id_list = []
        for model in model_list:
            last_record_id = await UrlRepository().save_url_response_to_db(model)
            id_list.append(last_record_id)
        return id_list

    async def get_all_url_responses(self) -> list[UrlEntity]:
        return await UrlRepository().get_all_url_responses()

    async def delete_url_response_by_id(self, url_id: int) -> typing.Any:
        return await UrlRepository().delete_url_response_by_id(url_id)
