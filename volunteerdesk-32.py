# === Stage 32: Add pagination helpers for long console output ===
# Project: VolunteerDesk
def paginate(lines, max_per_page=25):
    """Yield consecutive chunks of the given list of strings."""
    for i in range(0, len(lines), max_per_page):
        yield lines[i:i + max_per_page]
