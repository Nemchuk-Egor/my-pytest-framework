import pytest
from pydantic import BaseModel

from client.courses_api.private_http_builder import AuthenticationSchema
from client.courses_api.users.private_user_client import PrivateUserClient, get_private_user_client
from client.courses_api.users.public_user_client import get_public_user_client, PublicUserClient
from client.courses_api.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> str:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    def authorization(self) -> AuthenticationSchema:
        return AuthenticationSchema(email=self.email, password=self.password)


@pytest.fixture
def user_function(public_user_client:PublicUserClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def public_user_client() -> PublicUserClient:
    return get_public_user_client()

@pytest.fixture
def private_user_client(user_function: UserFixture) -> PrivateUserClient:
    user = user_function.authorization()
    return get_private_user_client(user=user)

