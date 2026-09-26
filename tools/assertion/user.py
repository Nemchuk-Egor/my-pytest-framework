from client.user.user_schema import (
    UserSchema,
    CreateUserResponseSchema,
    CreateUserRequestSchema,
)
from tools.assertion.base import assert_equal


def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.email, expected.email, name="email")
    assert_equal(actual.first_name, expected.first_name, name="first_name")
    assert_equal(actual.last_name, expected.last_name, name="last_name")
    assert_equal(actual.middle_name, expected.middle_name, name="middle_name")


def assert_create_user_response(
    response: CreateUserResponseSchema, request: CreateUserRequestSchema
):
    assert_equal(response.user.email, request.email, name="email")
    assert_equal(response.user.first_name, request.first_name, name="first_name")
    assert_equal(response.user.last_name, request.last_name, name="last_name")
    assert_equal(response.user.middle_name, request.middle_name, name="middle_name")
