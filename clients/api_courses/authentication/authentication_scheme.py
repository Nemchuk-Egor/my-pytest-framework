from pydantic import BaseModel, Field


class TokenScheme(BaseModel):
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refreshToken: str = Field(alias="refreshToken")


class LoginRequestScheme(BaseModel):
    email: str
    password: str


class LoginResponseScheme(BaseModel):
    token: TokenScheme


class RefreshRequestScheme(BaseModel):
    refreshToken: str = Field(alias="refreshToken")


class RefreshResponseScheme(BaseModel):
    token: TokenScheme
