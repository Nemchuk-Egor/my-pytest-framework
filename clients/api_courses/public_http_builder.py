from httpx import Client


def get_public_http_client() -> Client:
    return Client(base_url="http://localhost:8000", timeout=100)
