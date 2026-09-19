from client.courses_api.authentication.authentication_shema import LoginResponseSchema
from tools.assertion.base import assert_equal, assert_is_true


def assert_login_response(response: LoginResponseSchema):
    assert_equal(actual=response.token.token_type, expected="bearer", name="token_type")
    assert_is_true(actual=response.token.access_token, name="access_token")
    assert_is_true(actual=response.token.refresh_token, name="refresh_token")