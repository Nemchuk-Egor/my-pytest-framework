from __future__ import annotations

from typing import Any

from httpx import Client, Response, URL
from httpx._types import QueryParamTypes, RequestFiles, RequestData


class ApiClient:
    """Синхронный фасад над :class:`httpx.Client`.

    Предоставляет упрощённый типизированный интерфейс для выполнения
    базовых HTTP-запросов (GET, POST, PATCH, DELETE), делегируя всю работу
    переданному экземпляру ``httpx.Client``.
    """

    def __init__(self, client: Client) -> None:
        """Инициализирует фасад.

        :param client: сконфигурированный синхронный клиент httpx.
        """
        self.client: Client = client

    def get(
        self,
        url: URL | str,
        params: QueryParamTypes | None = None,
    ) -> Response:
        """Выполняет GET-запрос.

        :param url: абсолютный или относительный адрес запроса.
        :param params: query-параметры URL.
        :return: объект ответа httpx.
        """
        return self.client.get(url=url, params=params)

    def post(
        self,
        url: URL | str,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: Any | None = None,
    ) -> Response:
        """Выполняет POST-запрос.

        :param url: адрес запроса.
        :param data: тело запроса в виде form-urlencoded или байтов.
        :param files: файлы для ``multipart/form-data``.
        :param json: тело запроса в формате JSON.
        :return: объект ответа httpx.
        """
        return self.client.post(url=url, data=data, files=files, json=json)

    def patch(
        self,
        url: URL | str,
        json: Any | None = None,
    ) -> Response:
        """Выполняет PATCH-запрос.

        :param url: адрес запроса.
        :param json: тело PATCH-запроса в формате JSON.
        :return: объект ответа httpx.
        """
        return self.client.patch(url=url, json=json)

    def delete(
        self,
        url: URL | str,
    ) -> Response:
        """Выполняет DELETE-запрос.

        :param url: адрес запроса.
        :return: объект ответа httpx.
        """
        return self.client.delete(url=url)