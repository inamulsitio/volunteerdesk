# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: VolunteerDesk
def safe_int(value, default=0):
    try:
        if value is None or str(value).strip() == "":
            return default
        return int(str(value).strip())
    except (ValueError, TypeError):
        return default


def safe_float(value, default=0.0):
    try:
        if value is None or str(value).strip() == "":
            return default
        return float(str(value).strip())
    except (ValueError, TypeError):
        return default


def safe_str(value, default=""):
    if value is None:
        return default
    return str(value).strip()


def safe_bool(value, default=False):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("yes", "y", "true", "t", "1")


def safe_email(value, default=""):
    return safe_str(value, default)


def parse_optional_field(raw, default=None):
    if raw is None:
        return default
    cleaned = safe_str(raw)
    if cleaned == "":
        return default
    return cleaned
