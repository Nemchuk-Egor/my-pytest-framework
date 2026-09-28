"""Фабрика публичного HTTP-клиента.

Модуль содержит функцию :func:`get_public_http_client`, которая
возвращает ``httpx.Client`` без авторизации — для вызовов публичных
эндпоинтов API.
"""

from httpx import Client


def get_public_http_client() -> Client:
    """Создаёт публичный ``httpx.Client`` без авторизации.

    :return: экземпляр ``httpx.Client`` с настроенным базовым URL
        и таймаутом.
    """
    return Client(timeout=100, base_url="http://localhost:8000")
