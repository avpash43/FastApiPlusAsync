import typing
from src.domain.url_model import UrlDto, UrlEntity
from src.repository.database import database, url_info


async def save_url_response_to_db(model: UrlDto) -> typing.Any:
    query = url_info.insert().values(url=model.url, status=model.status, content_type=model.content_type)
    return await database.execute(query)


async def get_all_url_responses() -> list[UrlEntity]:
    query = url_info.select()
    return await database.fetch_all(query)


async def delete_url_response_by_id(url_id: int) -> typing.Any:
    query = url_info.delete().where(url_info.c.id == url_id)
    return await database.execute(query)
