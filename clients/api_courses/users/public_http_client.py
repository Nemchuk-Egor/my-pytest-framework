from httpx import Response, Client

from clients.api_client import ApiClient
from clients.api_courses.public_http_builder import get_public_http_client
from clients.api_courses.users.users_scheme import CreateUserRequestScheme


class PublicUserClient(ApiClient):
    def create_user(self, request: CreateUserRequestScheme) -> Response:
        return self.client.post(
            url="/api/v1/users", json=request.model_dump(by_alias=True)
        )


def create_public_user_client() -> PublicUserClient:
    return PublicUserClient(client=get_public_http_client())
