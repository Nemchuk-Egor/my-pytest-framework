from client.course_api.users.public_http_client import public_user_client
from client.course_api.users.user_schema import CreateUserRequestSchema
from tools.assertion.validation_json_schema import validation_json_schema

request = CreateUserRequestSchema()

public_user_client = public_user_client()

response = public_user_client.create_user_api(request)
print(response.status_code)
print(response.json())
validation_json_schema(instance=request.model_json_schema(), schema=response.json())
