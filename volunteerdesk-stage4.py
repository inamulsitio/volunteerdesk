# === Stage 4: Implement create operations for the primary records ===
# Project: VolunteerDesk
def add_volunteer(name, email):
    """Register a new volunteer."""
    volunteers.append({"id": len(volunteers) + 1, "name": name, "email": email})
    return volunteers[-1]

def add_shift(day, start, end, role):
    """Schedule a new shift."""
    shifts.append({"id": len(shifts) + 1, "day": day, "start": start, "end": end, "role": role})
    return shifts[-1]

def sign_up(volunteer_id, shift_id):
    """Sign a volunteer up for a shift."""
    signups.append({"id": len(signups) + 1, "volunteer_id": volunteer_id, "shift_id": shift_id})
    return signups[-1]

def log_hours(volunteer_id, hours):
    """Log hours worked by a volunteer."""
    hours_log.append({"id": len(hours_log) + 1, "volunteer_id": volunteer_id, "hours": hours})
    return hours_log[-1]

def write_thank_you(volunteer_id, message):
    """Write a thank-you note for a volunteer."""
    notes.append({"id": len(notes) + 1, "volunteer_id": volunteer_id, "message": message})
    return notes[-1]
