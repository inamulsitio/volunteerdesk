# === Stage 67: Add a function that returns key project metrics ===
# Project: VolunteerDesk
def project_metrics(volunteers, shifts, thank_you_notes):
    total_volunteers = len(volunteers)
    total_shifts = len(shifts)
    total_hours = 0.0
    for shift in shifts:
        total_hours += shift.get("hours", 0.0)
    volunteers_with_shifts = sum(1 for s in shifts for v in s.get("volunteers", []) if v in volunteers)
    volunteers_with_hours = set()
    for shift in shifts:
        for v in shift.get("volunteers", []):
            volunteers_with_hours.add(v)
    total_thank_you = len(thank_you_notes)
    thanked_volunteers = set()
    for note in thank_you_notes:
        thanked_volunteers.add(note.get("volunteer_id"))
    avg_hours = (total_hours / total_volunteers_with_hours) if total_volunteers_with_hours else 0.0
    coverage = (volunteers_with_shifts / total_volunteers) if total_volunteers else 0.0
    thank_you_rate = (len(thanked_volunteers) / total_volunteers_with_hours) if total_volunteers_with_hours else 0.0
    return {
        "total_volunteers": total_volunteers,
        "total_shifts": total_shifts,
        "total_hours": round(total_hours, 1),
        "volunteers_active": len(volunteers_with_hours),
        "thank_you_notes": total_thank_you,
        "volunteers_thanked": len(thanked_volunteers),
        "avg_hours_per_volunteer": round(avg_hours, 1),
        "volunteer_coverage": round(coverage, 2),
        "thank_you_rate": round(thank_you_rate, 2),
    }
