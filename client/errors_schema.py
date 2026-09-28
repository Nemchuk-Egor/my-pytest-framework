"""Pydantic-схемы ответов с ошибками API.

Модуль описывает контракты ошибочных ответов сервера.
Поля в camelCase (по контракту API) маппятся на snake_case через
``alias``, что позволяет использовать привычные имена в Python-коде.
"""

from pydantic import BaseModel, ConfigDict, Field


class InternalErrorsResponseSchema(BaseModel):
    """Схема ответа API с внутренней / авторизационной ошибкой.

    Используется, когда сервер возвращает тело вида
    ``{"detail": "..."}`` (например, при невалидном или просроченном
    токене).
    """

    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias="detail")
