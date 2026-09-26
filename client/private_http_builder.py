from httpx import Client
from pydantic import BaseModel

from client.authentication.authentication_client import get_authentication_client
from client.authentication.authentication_schema import LoginRequestSchema


class AuthenticationSchema(BaseModel):
    email: str
    password: str


def get_private_http_client(user: AuthenticationSchema) -> Client:
    authentication_client = get_authentication_client()
    request = LoginRequestSchema(email=user.email, password=user.password)
    response = authentication_client.login(request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {response.token.access_token}"},
    )
