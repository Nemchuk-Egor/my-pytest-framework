from typing import Any


def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f"{actual}",
        f"{expected}",
        f"{name}"
    )

def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        f"{actual}",
        f"{expected}",
    )

def assert_is_true(actual: Any, name: str):
    assert actual, (
        f"{actual}",
        f"{name}"
    )