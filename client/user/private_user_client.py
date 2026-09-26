from client.api_client import ApiClient
from httpx import Response

from client.private_http_builder import AuthenticationSchema, get_private_http_client
from client.user.user_schema import UpdateUserRequestSchema


class PrivateUserClient(ApiClient):
    def get_user_me_api(self) -> Response:
        return self.client.get(url="/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        return self.client.get(url=f"/api/v1/users/{user_id}")

    def update_user_api(self, request: UpdateUserRequestSchema, user_id: str) -> Response:
        return self.client.patch(url=f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True, exclude_none=True))

    def delete_api(self, user_id: str) -> Response:
        return self.client.delete(url=f"/api/v1/users/{user_id}")

def get_private_user_client(user: AuthenticationSchema) -> PrivateUserClient:
    return PrivateUserClient(get_private_http_client(user))