"""Pydantic-схемы для работы с пользователями.

Модуль содержит схемы запросов и ответов API пользователей.
Поля в camelCase (по контракту API) маппятся на snake_case через
``alias``, что позволяет использовать привычные имена в Python-коде.

Значения по умолчанию у полей запросов генерируются через ``fake``,
что удобно для тестов и быстрого прототипирования.
"""

from pydantic import BaseModel, ConfigDict, Field

from tools.fake import fake


class UserSchema(BaseModel):
    """Модель пользователя, возвращаемая API."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Тело запроса на создание пользователя.

    Все поля опциональны и по умолчанию заполняются случайными
    значениями через ``fake`` — удобно для тестов.
    """

    model_config = ConfigDict(populate_by_name=True)

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """Ответ API на создание пользователя."""

    user: UserSchema


class GetUserMeResponseSchema(BaseModel):
    """Ответ API с данными текущего аутентифицированного пользователя."""

    user: UserSchema


class GetUsersResponseSchema(BaseModel):
    """Ответ API со списком пользователей."""

    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """Тело запроса на обновление пользователя.

    Все поля опциональны и по умолчанию заполняются случайными
    значениями через ``fake``.
    """

    email: str | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(
        alias="middleName", default_factory=fake.middle_name
    )


class UpdateUserResponseSchema(BaseModel):
    """Ответ API на обновление пользователя."""

    user: UserSchema
