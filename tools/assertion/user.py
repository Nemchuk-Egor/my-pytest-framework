"""Доменные ассерты для пользователей.

Модуль проверяет соответствие возвращённых API данных ожидаемым:
сравнивает поля модели пользователя и валидирует, что ответ на
создание пользователя отражает данные исходного запроса.
"""

from client.user.user_schema import (
    UserSchema,
    CreateUserResponseSchema,
    CreateUserRequestSchema,
)
from tools.assertion.base import assert_equal


def assert_user(actual: UserSchema, expected: UserSchema) -> None:
    """Сравнивает два объекта пользователя по всем значимым полям.

    :param actual: пользователь, полученный от API.
    :param expected: ожидаемый пользователь.
    :raises AssertionError: если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.email, expected.email, name="email")
    assert_equal(actual.first_name, expected.first_name, name="first_name")
    assert_equal(actual.last_name, expected.last_name, name="last_name")
    assert_equal(actual.middle_name, expected.middle_name, name="middle_name")


def assert_create_user_response(
    response: CreateUserResponseSchema,
    request: CreateUserRequestSchema,
) -> None:
    """Проверяет, что ответ на создание пользователя соответствует запросу.

    Сравнивает поля пользователя из ответа API с полями исходного запроса
    (email, имя, фамилия, отчество).

    :param response: провалидированный ответ API на создание пользователя.
    :param request: исходный запрос на создание пользователя.
    :raises AssertionError: если данные в ответе не совпадают с запросом.
    """
    assert_equal(response.user.email, request.email, name="email")
    assert_equal(response.user.first_name, request.first_name, name="first_name")
    assert_equal(response.user.last_name, request.last_name, name="last_name")
    assert_equal(response.user.middle_name, request.middle_name, name="middle_name")
