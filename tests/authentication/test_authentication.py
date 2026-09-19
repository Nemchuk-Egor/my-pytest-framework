from http import HTTPStatus

import pytest

from client.courses_api.authentication.authentication_client import AuthenticationClient
from client.courses_api.authentication.authentication_shema import LoginRequestSchema, LoginResponseSchema
from fixtures.courses_api.user import UserFixture
from tools.assertion.authentication import assert_login_response
from tools.assertion.validation_json_schema import validation_json_schema
from tools.assertion.base import assert_status_code


@pytest.mark.authentication
@pytest.mark.regression
def test_login(user_function: UserFixture, authentication_client: AuthenticationClient):
    request = LoginRequestSchema(email=user_function.email, password=user_function.password)
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_login_response(response=response_data)
    validation_json_schema(instance=response.json(),schema=LoginResponseSchema.model_json_schema())
