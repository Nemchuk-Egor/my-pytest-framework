from httpx import Response

from clients.api_client import ApiClient
from clients.api_courses.private_http_builder import (
    AuthenticationScheme,
    get_private_http_client,
)


class PrivateUserClient(ApiClient):
    def get_user(self) -> Response:
        return self.client.get(url="/api/v1/users/me")


def get_private_users_client(user: AuthenticationScheme) -> PrivateUserClient:
    return PrivateUserClient(get_private_http_client(user=user))
