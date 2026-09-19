from http import HTTPStatus

import pytest

from client.courses_api.users.private_user_client import PrivateUserClient
from client.courses_api.users.public_user_client import PublicUserClient
from client.courses_api.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, \
    GetUsersMeResponseSchema
from fixtures.courses_api.user import UserFixture
from tools.assertion.base import assert_status_code
from tools.assertion.user import assert_create_user, assert_get_user_response
from tools.assertion.validation_json_schema import validation_json_schema


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_user_client: PublicUserClient):
    request = CreateUserRequestSchema()
    response = public_user_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_create_user(actual=response_data, expected=request)
    validation_json_schema(instance=response_data, schema=response.json())

@pytest.mark.users
@pytest.mark.regression
def test_get_users_me(user_function: UserFixture, private_user_client: PrivateUserClient):
    response = private_user_client.get_users_me_api()
    response_data = GetUsersMeResponseSchema.model_validate_json(response.text)
    create_user_response = user_function.response

    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_get_user_response(get_user_response=response_data, create_user_response=create_user_response)

    validation_json_schema(instance=response.json(), schema=response_data.model_json_schema())


