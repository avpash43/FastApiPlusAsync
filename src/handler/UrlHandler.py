from src.external.HttpClientAdapter import HttpClientAdapter


class UrlHandler:
    async def make_request_by_urls(self, urls: list[str]) -> list[dict]:
        result_list = []
        for url in urls:
            result: dict = await HttpClientAdapter().make_request_by_url(url)
            result_list.append(result)
        return result_list

    async def save_response_to_db(self, model_list) -> str:
        return ""
