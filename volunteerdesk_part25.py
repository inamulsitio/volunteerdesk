# === Stage 25: Add daily summary calculations ===
# Project: VolunteerDesk
def daily_summary(shifts, volunteers):
    """Compute a daily summary dict: hours, paid, volunteers, top_volunteer."""
    day_hours = {}
    day_volunteers = {}
    for shift in shifts:
        d = shift['date']
        day_hours[d] = day_hours.get(d, 0) + shift['hours']
        day_volunteers[d] = day_volunteers.get(d, 0) + 1
    summary = {}
    for d, h in day_hours.items():
        summary[d] = {
            'hours': h,
            'volunteers': day_volunteers[d],
            'paid': h * 15,
            'top_volunteer': None,
        }
    return summary
