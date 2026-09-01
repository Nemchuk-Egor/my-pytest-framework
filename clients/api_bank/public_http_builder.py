from httpx import Client


def get_public_http_builder(base_url: str) -> Client:
    return Client(base_url=base_url, timeout=100)
