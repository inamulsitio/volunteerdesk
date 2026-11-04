# === Stage 63: Add relationships between records where useful ===
# Project: VolunteerDesk
class Volunteer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Volunteer({self.name!r}, {self.email!r})"


class Shift:
    def __init__(self, date, start, end, event):
        self.date = date
        self.start = start
        self.end = end
        self.event = event

    def __repr__(self):
        return f"Shift({self.date!r}, {self.start!r}-{self.end!r}, {self.event!r})"


class SignUp:
    def __init__(self, volunteer, shift):
        self.volunteer = volunteer
        self.shift = shift

    def __repr__(self):
        return f"SignUp({self.volunteer!r}, {self.shift!r})"


class HourLog:
    def __init__(self, volunteer, minutes, shift):
        self.volunteer = volunteer
        self.minutes = minutes
        self.shift = shift

    def __repr__(self):
        return f"HourLog({self.volunteer!r}, {self.minutes}m, {self.shift!r})"


class ThankYouNote:
    def __init__(self, volunteer, shift, message):
        self.volunteer = volunteer
        self.shift = shift
        self.message = message

    def __repr__(self):
        return f"ThankYouNote({self.volunteer!r}, {self.shift!r}, {self.message!r})"
