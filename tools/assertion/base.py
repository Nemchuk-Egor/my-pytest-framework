from typing import Any


def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f"actual {actual}",
        f"expected {expected}",
        f"name {name}",
    )


def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        f"actual status code {actual}",
        f"expected status code {expected}",
    )
