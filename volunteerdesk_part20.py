# === Stage 20: Add duplicate detection for newly created records ===
# Project: VolunteerDesk
def find_duplicates(records, key_fn):
    """Return a dict of duplicate-key -> list of matching records."""
    seen = {}
    for r in records:
        k = key_fn(r)
        if k in seen:
            seen.setdefault(k, []).append(r)
        else:
            seen[k] = r
    return {k: v for k, v in seen.items() if isinstance(v, list)}
