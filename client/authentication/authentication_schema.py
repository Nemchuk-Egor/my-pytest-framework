from pydantic import BaseModel, ConfigDict, Field

from tools.fake import fake


class TokenSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    token: TokenSchema


class RefreshTokenRequestSchema(BaseModel):
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.uuid4)


class RefreshTokenResponseSchema(BaseModel):
    token: TokenSchema
