"""Проверка JSON-ответов по JSON Schema.

Модуль оборачивает ``jsonschema.validate`` и добавляет проверку форматов
(``format_checker``) через ``Draft202012Validator``. Используется в тестах
для валидации структуры ответа API по схеме.
"""

from typing import Any

from jsonschema import validate, Draft202012Validator


def validation_json_schema(instance: Any, schema: dict) -> None:
    """Валидирует JSON-объект по JSON Schema.

    Использует ``Draft 2020-12`` с включённой проверкой форматов
    (например, ``email``, ``date-time`` и т.п.).

    :param instance: проверяемый JSON-объект (например, ``response.json()``).
    :param schema: JSON Schema, которой должен соответствовать объект
        (обычно ``Model.model_json_schema()``).
    :raises jsonschema.exceptions.ValidationError: если объект не
        соответствует схеме.
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
