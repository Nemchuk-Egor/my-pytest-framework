from httpx import Response

from client.api_client import ApiClient
from client.courses_api.authentication.authentication_shema import LoginRequestSchema, LoginResponseSchema, \
    RefreshTokenRequestSchema
from client.courses_api.public_http_builder import get_public_http_client


class AuthenticationClient(ApiClient):

    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.client.post(url="/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

    def refresh_api(self, request: RefreshTokenRequestSchema) -> Response:
        return self.client.post(url="/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))


def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(get_public_http_client())