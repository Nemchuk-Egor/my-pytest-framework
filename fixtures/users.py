import pytest
from pydantic import BaseModel

from client.private_http_builder import AuthenticationSchema
from client.user.private_user_client import PrivateUserClient, get_private_user_client
from client.user.public_user_client import PublicUserClient, get_public_user_client
from client.user.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixtures(BaseModel):
    """Контейнер с данными пользователя, созданного в рамках теста.

    Объединяет исходный запрос на создание пользователя и ответ API,
    а также предоставляет удобные свойства для доступа к email, паролю
    и готовой схеме авторизации.
    """

    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> str:
        """Email созданного пользователя.

        :return: email из исходного запроса на создание.
        """
        return self.request.email

    @property
    def password(self) -> str:
        """Пароль созданного пользователя.

        :return: пароль из исходного запроса на создание.
        """
        return self.request.password

    @property
    def authentication(self) -> AuthenticationSchema:
        """Учётные данные для авторизации.

        :return: схема с email и паролем созданного пользователя.
        """
        return AuthenticationSchema(email=self.email, password=self.password)


@pytest.fixture
def public_user_client() -> PublicUserClient:
    """Фикстура публичного клиента пользователей.

    :return: экземпляр :class:`PublicUserClient` без авторизации.
    """
    return get_public_user_client()


@pytest.fixture
def function_user(public_user_client: PublicUserClient) -> UserFixtures:
    """Фикстура пользователя, созданного на время теста.

    Регистрирует нового пользователя через публичный клиент и возвращает
    контейнер с исходным запросом, ответом API и удобными свойствами
    для доступа к учётным данным.

    Область жизни — ``function``: пользователь создаётся заново для
    каждого теста.

    :param public_user_client: клиент публичных эндпоинтов пользователей.
    :return: контейнер :class:`UserFixtures` с данными пользователя.
    """
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return UserFixtures(request=request, response=response)


@pytest.fixture
def private_user_client(function_user: UserFixtures) -> PrivateUserClient:
    """Фикстура авторизованного клиента пользователя.

    Берёт учётные данные только что созданного пользователя
    (через :func:`function_user`) и возвращает приватный клиент
    с уже подставленным access-токеном.

    :param function_user: данные созданного пользователя.
    :return: экземпляр :class:`PrivateUserClient` с авторизацией.
    """
    return get_private_user_client(function_user.authentication)
