from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from tools.faker import faker


class TokenSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    token_type: str
    access_token: str
    refresh_token: str

class LoginRequestSchema(BaseModel):
    email: str = Field(default_factory=faker.email)
    password: str = Field(default_factory=faker.password)

class LoginResponseSchema(BaseModel):
    token: TokenSchema

class RefreshTokenRequestSchema(BaseModel):
    refresh_token: str = Field(default_factory=faker.uuid)

class RefreshTokenResponseSchema(BaseModel):
    token: TokenSchema