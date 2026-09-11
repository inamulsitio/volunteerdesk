# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: VolunteerDesk
def archive_records(records, cutoff_hours=365):
    """Move records older than cutoff_hours to an archive list, return the updated records."""
    now = time.time()
    active = [r for r in records if (now - r.get('logged_at', now)) < cutoff_hours]
    archived = [r for r in records if (now - r.get('logged_at', now)) >= cutoff_hours]
    return active, archived
