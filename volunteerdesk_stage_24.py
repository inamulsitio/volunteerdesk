# === Stage 24: Add grouped summaries by category or status ===
# Project: VolunteerDesk
def summarize_desk(desk):
    """Return a compact grouped summary dict: {category: count, status: count}."""
    summary = {}
    for record in desk.records:
        if record.category not in summary:
            summary[record.category] = 0
        if record.status not in summary:
            summary[record.status] = 0
        summary[record.category] += 1
        summary[record.status] += 1
    return summary
