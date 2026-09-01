from pydantic import BaseModel, Field, ConfigDict


class UserScheme(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_Number: str = Field(alias="phoneNumber")


class CreateUserRequestScheme(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_Number: str = Field(alias="phoneNumber")


class CreateUserResponseScheme(BaseModel):
    user: UserScheme
