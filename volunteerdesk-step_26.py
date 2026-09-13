# === Stage 26: Add weekly summary calculations ===
# Project: VolunteerDesk
from datetime import date

def weekly_summary(hours_log):
    """Compute weekly totals grouped by day of week."""
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    summary = {d: 0.0 for d in days}
    for entry in hours_log:
        d = entry["date"]
        summary[days[d.weekday()]] += entry["hours"]
    return summary

def generate_report(volunteer, weekly_summary):
    """Print a compact weekly report for a volunteer."""
    print(f"Volunteer: {volunteer['name']}, ID: {volunteer['id']}")
    print(f"Total hours: {volunteer['total_hours']:.1f}")
    print(f"Weekly breakdown:")
    for day, hours in weekly_summary.items():
        print(f"  {day}: {hours:.1f} hrs")
