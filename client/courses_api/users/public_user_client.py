from httpx import Response

from client.api_client import ApiClient
from client.courses_api.public_http_builder import get_public_http_client
from client.courses_api.users.user_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)


class PublicUserClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        return self.client.post(
            url="/api/v1/users", json=request.model_dump(by_alias=True)
        )

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_user_client() -> PublicUserClient:
    return PublicUserClient(get_public_http_client())