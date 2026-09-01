from httpx import Response

from clients.api_bank.public_http_builder import get_public_http_builder
from clients.api_bank.users.users_scheme import CreateUserRequestScheme
from clients.api_client import ApiClient


class UserClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestScheme) -> Response:
        return self.client.post(
            url="/api/v1/users", json=request.model_dump(by_alias=True)
        )

    def get_user_api(self, user_id: str) -> Response:
        return self.client.get(url=f"/api/v1/users/{user_id}")


def get_user_http_client() -> UserClient:
    return UserClient(get_public_http_builder(base_url="http://192.168.1.135:8001"))
