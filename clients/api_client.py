from httpx import Client, Response, URL
from httpx._types import QueryParamTypes, RequestData, RequestFiles
from typing import Any


class ApiClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParamTypes | None = None) -> Response:
        """
        Метод для отправки GET запроса
        :param url: экдпоинт для отправки запроса
        :param params: Query параметры например (?key=params)
        :return: Возвращает объект ответ от эндпоинта
        """
        return self.client.get(url, params=params)

    def post(
        self,
        url: URL | str,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: Any | None = None,
    ) -> Response:
        """
        Метод для отправки POST запроса
        :param url: эндпоинт для отправки запроса
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded)
        :param files: данные для загрузки на сервер
        :param json: данные в формате JSON
        :return: Возвращает объект ответ от эндпоинта
        """
        return self.client.post(url, data=data, files=files, json=json)
