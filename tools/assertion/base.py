"""Базовые ассерты для тестов.

Модуль содержит универсальные проверки, не привязанные к конкретному
домену: сравнение произвольных значений и проверку HTTP-статус-кода.
Используются остальными модулями пакета ``tools.assertion`` для
построения доменных ассертов.
"""

from typing import Any


def assert_equal(actual: Any, expected: Any, name: str) -> None:
    """Проверяет, что ``actual`` равен ``expected``.

    :param actual: фактическое значение.
    :param expected: ожидаемое значение.
    :param name: человекочитаемое имя проверяемого поля — попадает
        в сообщение об ошибке, чтобы было понятно, что именно упало.
    :raises AssertionError: если значения не равны.
    """
    assert actual == expected, (f"actual {actual} ,expected {expected} name {name}",)


def assert_status_code(actual: int, expected: int) -> None:
    """Проверяет, что HTTP-статус-код ответа совпадает с ожидаемым.

    :param actual: фактический статус-код ответа.
    :param expected: ожидаемый статус-код (например, из ``http.HTTPStatus``).
    :raises AssertionError: если коды не совпадают.
    """
    assert actual == expected, (
        f"actual status code {actual} expected status code {expected}",
    )
