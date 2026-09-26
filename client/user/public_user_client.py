"""Публичный клиент для работы с пользователями.

Модуль содержит класс :class:`PublicUserClient` — специализированный
клиент для вызовов эндпоинтов пользователей, доступных без авторизации,
а также фабричную функцию :func:`get_public_user_client`.
"""

from httpx import Response

from client.api_client import ApiClient
from client.public_http_builder import get_public_http_client
from client.user.user_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)


class PublicUserClient(ApiClient):
    """Клиент публичных эндпоинтов пользователей.

    Наследует базовые HTTP-методы от :class:`ApiClient` и добавляет
    методы для конкретных сценариев работы с пользователями.
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """Отправляет запрос на создание пользователя.

        Низкоуровневый метод: возвращает «сырой» ответ httpx без валидации.

        :param request: данные нового пользователя.
        :return: объект ответа httpx.
        """
        return self.client.post(
            url="/api/v1/users",
            json=request.model_dump(by_alias=True),
        )

    def create_user(
        self,
        request: CreateUserRequestSchema,
    ) -> CreateUserResponseSchema:
        """Создаёт пользователя и возвращает валидированный ответ.

        :param request: данные нового пользователя.
        :return: провалидированная схема ответа с созданным пользователем.
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_user_client() -> PublicUserClient:
    """Создаёт публичный клиент пользователей.

    :return: экземпляр :class:`PublicUserClient` с настроенным
        HTTP-клиентом для публичного API.
    """
    return PublicUserClient(get_public_http_client())