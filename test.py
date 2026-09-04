from time import time

from tools.assertions.schema import validate_json_schema
from clients.api_courses.private_http_builder import AuthenticationScheme
from clients.api_courses.users.private_http_client import get_private_users_client
from clients.api_courses.users.public_http_client import create_public_user_client
from clients.api_courses.users.users_scheme import CreateUserRequestScheme, CreateUserResponseScheme, \
    GetUserResponseSchema

data_user = CreateUserRequestScheme(
    email=f"user{time()}@example.com",
    password="string",
    lastName="string",
    firstName="string",
    middleName="string",
)

public_user_client = create_public_user_client()
create_user_response = public_user_client.create_user(data_user)
create_user_response_schema = CreateUserResponseScheme.model_json_schema()

print(create_user_response.status_code)
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)

user = AuthenticationScheme(
    email=data_user.email,
    password=data_user.password,
)

private_user_client = get_private_users_client(user)
get_user_response = private_user_client.get_user_me_api()
get_user_response_scheme = GetUserResponseSchema.model_json_schema()

print(get_user_response.status_code)
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_scheme)
