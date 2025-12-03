def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.00