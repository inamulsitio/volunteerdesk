# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: VolunteerDesk
def format_shift_entry(shift: dict) -> str:
    """Return a human-readable summary of a single shift."""
    return (
        f"Shift: {shift.get('title', 'Untitled')}\n"
        f"  Date: {shift.get('date', 'N/A')}\n"
        f"  Duration: {shift.get('duration', 'N/A')}\n"
        f"  Volunteer: {shift.get('volunteer', 'Unknown')}"
    )


def format_volunteer_profile(volunteer: dict) -> str:
    """Return a human-readable summary of a volunteer."""
    return (
        f"Name: {volunteer.get('name', 'Unknown')}\n"
        f"  Email: {volunteer.get('email', 'N/A')}\n"
        f"  Total Hours: {volunteer.get('hours', 0)}\n"
        f"  Status: {volunteer.get('status', 'Unknown')}"
    )


def format_thank_you_note(note: dict, volunteer_name: str) -> str:
    """Return a formatted thank-you note addressed to the volunteer."""
    return (
        f"Dear {volunteer_name},\n\n"
        f"Thank you for your volunteer contribution!\n"
        f"Note: {note.get('message', 'Your support means a lot to us.')}\n\n"
        f"Sincerely, VolunteerDesk Team"
    )
