from http import HTTPStatus

import pytest

from client.user.public_user_client import PublicUserClient
from client.user.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertion.base import assert_status_code
from tools.assertion.user import assert_create_user_response
from tools.assertion.json_schema import validation_json_schema


@pytest.mark.user
@pytest.mark.regression
class TestUser:
    def test_create_user(self, public_user_client: PublicUserClient) -> None:
        request = CreateUserRequestSchema()
        response = public_user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(response_data, request)
        validation_json_schema(response.json(), response_data.model_json_schema())
