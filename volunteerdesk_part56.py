# === Stage 56: Add compact error classes for domain failures ===
# Project: VolunteerDesk
class VolunteerError(Exception):
    """Base error for all volunteer-desk failures."""


class ShiftNotFoundError(VolunteerError):
    """Raised when a requested shift does not exist."""


class VolunteerSignupError(VolunteerError):
    """Raised when a volunteer cannot complete a sign-up."""


class HoursLoggingError(VolunteerError):
    """Raised when hour tracking fails (e.g. negative hours)."""


class ThankYouNoteError(VolunteerError):
    """Raised when a thank-you note cannot be created or sent."""


class VolunteerConflictError(VolunteerError):
    """Raised when a volunteer is double-booked on overlapping shifts."""


class DatabaseError(VolunteerError):
    """Raised for unexpected database or persistence failures."""
