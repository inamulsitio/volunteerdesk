# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: VolunteerDesk
def validate_required(value, field_name):
    if not value:
        raise ValueError(f"{field_name} is required")
    return value

def validate_identifier(value, field_name):
    if not value or not value.isalnum():
        raise ValueError(f"{field_name} must be alphanumeric")
    return value

def validate_short_text(value, max_length=50, field_name="Text"):
    if not value:
        raise ValueError(f"{field_name} is required")
    if len(value) > max_length:
        raise ValueError(f"{field_name} must be {max_length} characters or fewer")
    return value.strip()
