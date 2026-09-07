# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: VolunteerDesk
def format_shift(shift):
    """Return a compact one-line summary for a shift."""
    return (
        f"Shift: {shift['title']} | "
        f"Date: {shift['date']} | "
        f"Volunteer: {shift['volunteer']['name']} | "
        f"Hours: {shift['hours']}"
    )


def format_volunteer(volunteer):
    """Return a compact one-line summary for a volunteer."""
    return (
        f"Volunteer: {volunteer['name']} | "
        f"Email: {volunteer['email']} | "
        f"Total Hours: {volunteer['total_hours']}"
    )


def format_thank_you(note):
    """Return a compact one-line summary for a thank-you note."""
    return (
        f"Note to: {note['volunteer']['name']} | "
        f"Message: {note['message'][:50]}..."
    )


def format_sign_up(sign_up):
    """Return a compact one-line summary for a sign-up."""
    return (
        f"Sign-up: {sign_up['volunteer']['name']} | "
        f"Shift: {sign_up['shift']['title']} | "
        f"Date: {sign_up['shift']['date']}"
    )
