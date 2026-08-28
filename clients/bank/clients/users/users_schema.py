from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    """
    Данные пользователя
    """

    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """
    Данные для создания пользователя
    """

    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Данные о пользователе которые возвращаются с API
    """

    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Данные о пользователе которые возвращаются с API
    """

    user: UserSchema
