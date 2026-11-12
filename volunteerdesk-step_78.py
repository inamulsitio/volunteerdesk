# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: VolunteerDesk
def find_shift_by_id(shifts, shift_id):
    for shift in shifts:
        if shift.get("id") == shift_id:
            return shift
    return None


def find_volunteer_by_id(volunteers, volunteer_id):
    for volunteer in volunteers:
        if volunteer.get("id") == volunteer_id:
            return volunteer
    return None


def add_hours(volunteer_id, hours):
    for volunteer in volunteers:
        if volunteer.get("id") == volunteer_id:
            volunteer["hours_logged"] = volunteer.get("hours_logged", 0) + hours
            return
    raise ValueError(f"Volunteer {volunteer_id} not found")


def log_thank_you(note):
    thank_you_notes.append(note)


def generate_summary():
    total_volunteers = len(volunteers)
    total_hours = sum(v.get("hours_logged", 0) for v in volunteers)
    total_shifts = len(shifts)
    return {
        "total_volunteers": total_volunteers,
        "total_hours": total_hours,
        "total_shifts": total_shifts,
        "thank_you_count": len(thank_you_notes),
    }
