# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: VolunteerDesk
def generate_changelog(log_entries):
    """Generate a compact changelog from activity log entries."""
    grouped = {}
    for entry in log_entries:
        date, message = entry.split(": ", 1)
        grouped.setdefault(date, []).append(message)

    lines = ["CHANGELOG", "=" * 40]
    for date in sorted(grouped):
        lines.append(f"\n[{date}]")
        for message in grouped[date]:
            lines.append(f"  - {message}")
    return "\n".join(lines)
