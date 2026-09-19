from client.courses_api.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUsersMeResponseSchema
from tools.assertion.base import assert_equal


def assert_create_user(actual: CreateUserResponseSchema, expected: CreateUserRequestSchema):
    assert_equal(actual.user.email, expected.email, "email")
    assert_equal(actual.user.first_name, expected.first_name, "first_name")
    assert_equal(actual.user.last_name, expected.last_name, "last_name")
    assert_equal(actual.user.middle_name, expected.middle_name, "middle_name")

def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

def assert_get_user_response(get_user_response: GetUsersMeResponseSchema, create_user_response: CreateUserResponseSchema):
    assert_user(actual=get_user_response.user, expected=create_user_response.user)