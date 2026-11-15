# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: VolunteerDesk
def purge_duplicate_shifts(shifts):
    seen = {}
    for shift in shifts:
        key = (shift["event"], shift["start"], shift["end"])
        if key not in seen:
            seen[key] = shift
    return list(seen.values())

def purge_duplicate_signups(signups):
    seen = {}
    for signup in signups:
        key = (signup["volunteer"], signup["shift"])
        if key not in seen:
            seen[key] = signup
    return list(seen.values())

def purge_duplicate_notes(notes):
    seen = {}
    for note in notes:
        key = (note["volunteer"], note["date"])
        if key not in seen:
            seen[key] = note
    return list(seen.values())

def sanitize_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

def sanitize_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

def normalize_email(email):
    return email.strip().lower() if email else ""

def clamp(value, low=0, high=9999):
    return max(low, min(high, value))
