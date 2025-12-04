from typing import Any


def safe_int(value: Any) -> int:
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def safe_float(value: Any) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.00
