from time import time

from clients.api_courses.private_http_builder import AuthenticationScheme
from clients.api_courses.users.private_http_client import get_private_users_client
from clients.api_courses.users.public_http_client import create_public_user_client
from clients.api_courses.users.users_scheme import CreateUserRequestScheme

data_user = CreateUserRequestScheme(
    email=f"user{time()}@example.com",
    password="string",
    lastName="string",
    firstName="string",
    middleName="string",
)

public_user_client = create_public_user_client()
create_user_response = public_user_client.create_user(data_user)
print(create_user_response.status_code)
print(create_user_response.json())

user = AuthenticationScheme(
    email=data_user.email,
    password=data_user.password,
)

private_user_client = get_private_users_client(user)
get_user_response = private_user_client.get_user()
print(get_user_response.status_code)
print(get_user_response.json())
