"""Доменные ассерты для ответов с ошибками API.

Модуль проверяет, что тело ошибочного ответа соответствует ожидаемой
схеме и конкретному сообщению (например, ``Invalid or expired token``).
"""

from client.errors_schema import InternalErrorsResponseSchema
from tools.assertion.base import assert_equal


def assert_internal_errors_response(
    actual: InternalErrorsResponseSchema, expected: InternalErrorsResponseSchema
) -> None:
    """Сравнивает два ответа с ошибкой по полю ``details``.

    :param actual: фактический ответ API с ошибкой.
    :param expected: ожидаемый ответ с ошибкой.
    :raises AssertionError: если поле ``details`` не совпадает.
    """
    assert_equal(actual.details, expected.details, name="details")


def assert_invalid_or_expired_token(response: InternalErrorsResponseSchema) -> None:
    """Проверяет, что ответ сообщает о невалидном или просроченном токене.

    Ожидаемое сообщение: ``Invalid or expired token``.

    :param response: провалидированный ответ API с ошибкой.
    :raises AssertionError: если текст ошибки не совпадает с ожидаемым.
    """
    expected = InternalErrorsResponseSchema(detail="Invalid or expired token")

    assert_internal_errors_response(response, expected)
