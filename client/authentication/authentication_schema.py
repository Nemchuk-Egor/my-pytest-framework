"""Pydantic-схемы для аутентификации.

Модуль описывает контракты эндпоинтов аутентификации: вход по email
и паролю, обновление access-токена по refresh-токену, а также модель
самого токена. Поля в camelCase (по контракту API) маппятся на
snake_case через ``alias``.

Значения по умолчанию у полей запросов генерируются через ``fake``,
что удобно для тестов.
"""

from pydantic import BaseModel, ConfigDict, Field

from tools.fake import fake


class TokenSchema(BaseModel):
    """Пара токенов, возвращаемая API аутентификации."""

    model_config = ConfigDict(populate_by_name=True)

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """Тело запроса на вход в систему.

    Поля по умолчанию заполняются случайными значениями через ``fake`` —
    удобно для тестов.
    """

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    """Ответ API на успешный вход — содержит пару токенов."""

    token: TokenSchema


class RefreshTokenRequestSchema(BaseModel):
    """Тело запроса на обновление access-токена.

    Содержит refresh-токен; по умолчанию подставляется случайный UUID4
    (для тестовых сценариев).
    """

    refresh_token: str = Field(alias="refreshToken", default_factory=fake.uuid4)


class RefreshTokenResponseSchema(BaseModel):
    """Ответ API на обновление токена — новая пара токенов."""

    token: TokenSchema
