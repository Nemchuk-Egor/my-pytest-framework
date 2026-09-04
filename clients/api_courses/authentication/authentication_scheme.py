from pydantic import BaseModel, Field

from tools.faker import fake


class TokenScheme(BaseModel):
    token_type: str = Field(alias="tokenType", )
    access_token: str = Field(alias="accessToken")
    refreshToken: str = Field(alias="refreshToken")


class LoginRequestScheme(BaseModel):
    email: str = Field(default_factory=fake.email())
    password: str = Field(default_factory=fake.password())


class LoginResponseScheme(BaseModel):
    token: TokenScheme


class RefreshRequestScheme(BaseModel):
    refreshToken: str = Field(alias="refreshToken")


class RefreshResponseScheme(BaseModel):
    token: TokenScheme
