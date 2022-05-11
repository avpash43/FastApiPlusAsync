import aiohttp


class HttpClientAdapter:
    async def make_request_by_url(self, url: str) -> dict:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return {"url": url, "status_code": response.status, "content-type": response.content_type}
        except OSError:
            print(f"{url} url is not valid")
