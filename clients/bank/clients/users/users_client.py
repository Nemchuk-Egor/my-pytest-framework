from httpx import Response

from clients.api_client import ApiClient
from clients.bank.clients.users.users_schema import CreateUserRequestSchema
from clients.public_http_client import get_public_http_client


class UsersClient(ApiClient):
    def create_user(self, request: CreateUserRequestSchema) -> Response:
        """
        Отправляет POST запрос на создание пользователя
        :param request: Данные пользователя ввиде словаря
        :return: Возвращается ответ от сервера ввиде объекта Response
        """
        return self.client.post("/api/v1/users", json=request.model_dump(by_alias=True))

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
    return UsersClient(client=get_public_http_client(base_url))
