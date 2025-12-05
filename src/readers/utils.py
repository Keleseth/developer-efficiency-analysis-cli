from typing import Any


def safe_int(value: Any) -> int:
    """
    Если возможно, преобразует value в int, иначе возвращает 0.
    Пропуск строк с пропущенными или некорректными int значениями не
    требуется для вычисления performance отчета.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def safe_float(value: Any) -> float | None:
    """
    Если возможно, преобразует value в float, иначе возвращает None,
    чтобы пропустить строки с пропущенными или некорректными float значениями.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
