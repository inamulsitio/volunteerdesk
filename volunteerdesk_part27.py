# === Stage 27: Add monthly summary calculations ===
# Project: VolunteerDesk
def monthly_summary(data):
    """Return a dict with total hours, sign-ups, and thank-you notes per month."""
    from collections import defaultdict
    months = defaultdict(lambda: {"hours": 0, "signups": 0, "notes": 0})
    for entry in data:
        m = entry.get("month", "")
        if m:
            months[m]["hours"] += entry.get("hours", 0)
            if entry.get("type") == "signup":
                months[m]["signups"] += 1
            elif entry.get("type") == "note":
                months[m]["notes"] += 1
    return dict(months)
