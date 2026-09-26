from typing import Any

from jsonschema import validate, Draft202012Validator


def validation_json_schema(instance: Any, schema: dict):
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
