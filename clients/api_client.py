from httpx import Client, Response, URL
from httpx._types import RequestData, RequestFiles, QueryParamTypes
from typing import Any


class ApiClient:
    def __init__(self, client: Client):
        self.client = client

    def post(
        self,
        url: URL | str,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: Any | None = None,
    ) -> Response:
        return self.client.post(url, data=data, json=json, files=files)

    def get(self, url: URL | str, params: QueryParamTypes | None = None) -> Response:
        return self.client.post(url, params=params)

    def patch(
        self,
        url: URL | str,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: Any | None = None,
    ) -> Response:
        return self.client.patch(url, data=data, files=files, json=json)

    def delete(self, url: URL | str) -> Response:
        return self.client.delete(url)
