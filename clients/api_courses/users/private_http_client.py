from httpx import Response

from clients.api_client import ApiClient
from clients.api_courses.private_http_builder import (
    AuthenticationScheme,
    get_private_http_client,
)
from clients.api_courses.users.users_scheme import UpdateUserRequestScheme


class PrivateUserClient(ApiClient):
    def get_user_me_api(self) -> Response:
        return self.client.get(url="/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        return self.client.get(url=f"/api/v1/users/{user_id}")

    def update_user_api(
        self, user_id: str, request: UpdateUserRequestScheme
    ) -> Response:
        return self.client.patch(
            url=f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True)
        )

    def delete_user_api(self, user_id: str) -> Response:
        return self.client.delete(url=f"/api/v1/users/{user_id}")


def get_private_users_client(user: AuthenticationScheme) -> PrivateUserClient:
    return PrivateUserClient(get_private_http_client(user=user))
