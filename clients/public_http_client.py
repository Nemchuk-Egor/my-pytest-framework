import httpx
from httpx import Client


def get_public_http_client(base_url: str) -> Client:
    """

    :param base_url: Базовый Url адрес
    :return: Возвращает настроенный клиент для выполнения запросов на заданный url адрес
    """
    return httpx.Client(timeout=100, base_url=base_url)
