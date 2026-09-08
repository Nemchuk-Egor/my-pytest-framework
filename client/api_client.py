from httpx import Client, Response, URL
from httpx._types import QueryParamTypes, RequestData, RequestFiles
import typing


class ApiClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParamTypes) -> Response:
        return self.client.get(url=url, params=params)

    def post(
            self,
            url: URL | str,
            data: RequestData | None = None,
            files: RequestFiles | None = None,
            json: typing.Any | None = None,
    ) -> Response:
        return self.client.post(url=url, data=data, files=files, json=json)

    def patch(
            self,
            url: URL | str,
            data: RequestData | None = None,
            files: RequestFiles | None = None,
            json: typing.Any | None = None,
    ) -> Response:
        return self.client.patch(url=url, data=data, files=files, json=json)

    def delete(self, url: URL | str, params: QueryParamTypes | None = None) -> Response:
        return self.client.delete(url=url, params=params)