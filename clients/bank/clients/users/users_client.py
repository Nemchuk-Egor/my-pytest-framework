from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient
from clients.public_http_client import get_public_http_client


class CreateUserRequest(TypedDict):
    """
    Данные для создания пользователя
    """

    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UsersClient(ApiClient):
    def create_user(self, request: CreateUserRequest) -> Response:
        """
        Отправляет POST запрос на создание пользователя
        :param request: Данные пользователя ввиде словаря
        :return: Возвращается ответ от сервера ввиде объекта Response
        """
        return self.client.post("/api/v1/users", json=request)

    def get_user(self, user_id: str) -> Response:
        """
        Отправляет Get запрос на создание пользователя
        :param user_id: пользовательский id ввиде uuid
        :return: Возвращается ответ от сервера ввиде объекта Response
        """
        return self.client.get(f"/api/v1/users/{user_id}")


def create_user_client() -> UsersClient:
    """
    Создает готовый клиент для запросов на сервис users
    :return: Возвращает клиент с переданным URL для запросов на сервис users
    """
    base_url = "http://192.168.1.135:8001"
    return UsersClient(get_public_http_client(base_url))
