"""Фабрика авторизованного HTTP-клиента.

Модуль содержит функцию :func:`get_private_http_client`, которая
выполняет вход через :class:`AuthenticationClient` и возвращает
``httpx.Client`` с уже установленным заголовком ``Authorization``
на основе полученного access-токена.
"""

import functools
from httpx import Client
from pydantic import BaseModel, ConfigDict

from client.authentication.authentication_client import get_authentication_client
from client.authentication.authentication_schema import LoginRequestSchema


class AuthenticationSchema(BaseModel):
    """Учётные данные пользователя для авторизации.

    Используются для получения access-токена через сервис
    аутентификации.
    """

    model_config = ConfigDict(frozen=True)

    email: str
    password: str


@functools.lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationSchema) -> Client:
    """Создаёт авторизованный ``httpx.Client``.

    Выполняет вход через :func:`get_authentication_client`, извлекает
    access-токен из ответа и подставляет его в заголовок
    ``Authorization`` итогового клиента.

    :param user: учётные данные пользователя.
    :return: экземпляр ``httpx.Client`` с заголовком авторизации
        и настроенным базовым URL.
    """
    authentication_client = get_authentication_client()
    request = LoginRequestSchema(email=user.email, password=user.password)
    response = authentication_client.login(request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {response.token.access_token}"},
    )
