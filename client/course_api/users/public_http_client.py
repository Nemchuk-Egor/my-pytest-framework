from httpx import Response

from client.api_client import ApiClient
from client.course_api.public_http_client_builder import get_public_http_client
from client.course_api.users.user_schema import CreateUserRequestSchema


class PublicUserClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        return self.client.post(url="/api/v1/users", json=request.model_dump(by_alias=True))


def public_user_client() -> PublicUserClient:
    return PublicUserClient(client=get_public_http_client())