from httpx import Response

from client.api_client import ApiClient
from client.courses_api.private_http_builder import AuthenticationSchema, get_private_http_client


class PrivateUserClient(ApiClient):
    def get_users_me_api(self) -> Response:
        return self.client.get(url="/api/v1/users/me")


def get_private_user_client(user: AuthenticationSchema) -> PrivateUserClient:
    return PrivateUserClient(get_private_http_client(user=user))