"""Клиент эндпоинтов аутентификации.

Модуль содержит класс :class:`AuthenticationClient` — специализированный
клиент для вызовов публичных эндпоинтов аутентификации (login,
refresh), а также фабричную функцию :func:`get_authentication_client`.
"""

from httpx import Response

from client.api_client import ApiClient
from client.authentication.authentication_schema import (
    LoginResponseSchema,
    LoginRequestSchema,
    RefreshTokenRequestSchema,
)
from client.public_http_builder import get_public_http_client


class AuthenticationClient(ApiClient):
    """Клиент публичных эндпоинтов аутентификации.

    Наследует базовые HTTP-методы от :class:`ApiClient` и добавляет
    методы для конкретных сценариев входа и обновления токена.
    """

    def login_api(self, request: LoginRequestSchema) -> Response:
        """Отправляет запрос на вход в систему.

        Низкоуровневый метод: возвращает «сырой» ответ httpx без валидации.

        :param request: учётные данные пользователя.
        :return: объект ответа httpx.
        """
        return self.client.post(
            url="/api/v1/authentication/login",
            json=request.model_dump(by_alias=True),
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """Выполняет вход и возвращает валидированный ответ.

        :param request: учётные данные пользователя.
        :return: схема ответа с парой токенов.
        """
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

    def refresh_token_api(self, request: RefreshTokenRequestSchema) -> Response:
        """Отправляет запрос на обновление access-токена.

        :param request: refresh-токен.
        :return: объект ответа httpx.
        """
        return self.client.post(
            url="/api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True),
        )


def get_authentication_client() -> AuthenticationClient:
    """Создаёт клиент аутентификации.

    :return: экземпляр :class:`AuthenticationClient` с настроенным
        HTTP-клиентом для публичного API.
    """
    return AuthenticationClient(get_public_http_client())
