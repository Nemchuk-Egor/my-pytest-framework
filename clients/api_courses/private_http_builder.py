from httpx import Client
from pydantic import BaseModel

from clients.api_courses.authentication.authentication_client import (
    create_authentication_client,
)
from clients.api_courses.authentication.authentication_scheme import LoginRequestScheme


class AuthenticationScheme(BaseModel, frozen=True):
    email: str
    password: str


def get_private_http_client(user: AuthenticationScheme) -> Client:
    authentication_client = create_authentication_client()
    request = LoginRequestScheme(email=user.email, password=user.password)
    response = authentication_client.login(request)
    return Client(
        base_url="http://localhost:8000",
        timeout=100,
        headers={"Authorization": f"Bearer {response.token.access_token}"},
    )
