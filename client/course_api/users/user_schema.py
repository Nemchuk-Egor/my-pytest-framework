from pydantic import BaseModel, ConfigDict, Field

from tools.faker import fake


class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)

class CreateUserResponseSchema(BaseModel):
    user: UserSchema