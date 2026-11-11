# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: VolunteerDesk
def format_date(value):
    """Return an ISO date string or empty string for falsy input."""
    if not value:
        return ""
    return str(value)[:10]


def parse_date(value):
    """Return a datetime.date from a string, or None if invalid."""
    if not value:
        return None
    try:
        return datetime.date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def hours_from_minutes(minutes):
    """Convert a minute count into a decimal hours string."""
    return f"{(int(minutes) / 60):.2f}"


def initials_from_name(name):
    """Return uppercase initials for a full name, or the name itself."""
    if not name:
        return ""
    parts = [p.strip() for p in name.split()]
    return "".join(p[0].upper() for p in parts if p)


def today_iso():
    """Return the current date as an ISO string."""
    return datetime.date.today().isoformat()
