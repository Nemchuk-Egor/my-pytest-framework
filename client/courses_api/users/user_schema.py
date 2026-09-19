from tools.faker import faker
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    id: str
    email: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    email: str = Field(default_factory=faker.email)
    password: str = Field(default_factory=faker.password)
    last_name: str = Field(default_factory=faker.last_name)
    first_name: str = Field(default_factory=faker.first_name)
    middle_name: str = Field(default_factory=faker.middle_name)


class CreateUserResponseSchema(BaseModel):
    user: UserSchema

class GetUsersMeResponseSchema(BaseModel):
    user: UserSchema
