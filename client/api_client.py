from httpx import Client, Response, URL
from httpx._types import QueryParamTypes, RequestFiles
from typing import Any

"""
Обертка (facade) httpx Client, будем все наши клиенты наследовать от 
этой обертки сделано для того чтобы удобно 
централизовано можно было добавлять allure шаги, работу с pydantic моделами
в одном месте
"""


class ApiClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParamTypes | None = None) -> Response:
        return self.client.get(url=url, params=params)

    def post(
        self,
        url: URL | str,
        files: RequestFiles | None = None,
        json: Any | None = None,
        params: QueryParamTypes | None = None,
    ) -> Response:
        return self.post(url=url, files=files, json=json, params=params)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        return self.patch(url=url, json=json)

    def delete(self, url: URL | str) -> Response:
        return self.delete(url=url)
