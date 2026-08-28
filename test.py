from clients.bank.clients.users.users_client import (
    create_user_client,
)
from time import time

from clients.bank.clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)

payload_data = CreateUserRequestSchema(
    email=f"user{time()}@example.com",
    lastName="string",
    firstName="string",
    middleName="string",
    phoneNumber="string",
)

user_client = create_user_client()
create_user_response = user_client.create_user(payload_data)

print(create_user_response.status_code)
print(CreateUserResponseSchema.model_validate_json(create_user_response.text))

user_data = create_user_response.json()
user_id = user_data["user"]["id"]
get_user_response = user_client.get_user(user_id)

print(get_user_response.status_code)
print(get_user_response.json())
