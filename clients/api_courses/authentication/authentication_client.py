from httpx import Response


from clients.api_client import ApiClient
from clients.api_courses.authentication.authentication_scheme import (
    LoginRequestScheme,
    RefreshRequestScheme,
    LoginResponseScheme,
)
from clients.api_courses.public_http_builder import get_public_http_client


class AuthenticationClient(ApiClient):
    def login_api(self, request: LoginRequestScheme) -> Response:
        return self.client.post(
            url="/api/v1/authentication/login", json=request.model_dump()
        )

    def refresh_token(self, request: RefreshRequestScheme) -> Response:
        return self.client.post(
            url="/api/v1/authentication/refresh", json=request.model_dump()
        )

    def login(self, request: LoginRequestScheme) -> LoginResponseScheme:
        response = self.login_api(request)
        return LoginResponseScheme.model_validate_json(response.text)


def create_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())
