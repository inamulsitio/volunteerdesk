# === Stage 35: Add active user switching and user-specific records ===
# Project: VolunteerDesk
"""VolunteerDesk – User management and active-user switching.

Adds a User model, a session store, and helper functions for:
- creating users with a password hash
- recording sign-ups, shift work, and thank-you notes per user
- switching the 'active' user and returning their records
"""

import hashlib
from datetime import datetime


# ---------- User model ----------
class User:
    """A volunteer identified by name and email."""

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self._hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return hashlib.sha256(password.encode()).hexdigest() == self._hash

    def __repr__(self):
        return f"<User {self.name}>"


# ---------- Session store ----------
class Session:
    """Holds the current active user and per-user records."""

    def __init__(self):
        self.active_user: User | None = None
        self.users: dict[str, User] = {}
        self.signups: dict[str, list[dict]] = {}
        self.shifts: dict[str, list[dict]] = {}
        self.thanks: dict[str, list[dict]] = {}

    def register(self, user: User) -> None:
        self.users[user.email] = user
        self.signups[user.email] = []
        self.shifts[user.email] = []
        self.thanks[user.email] = []

    def login(self, email: str, password: str) -> User | None:
        user = self.users.get(email)
        if user and user.check_password(password):
            self.active_user = user
            return user
        return None

    def signup(self, note: str) -> None:
        if self.active_user:
            self.signups[self.active_user.email].append({
                "note": note,
                "time": datetime.now().isoformat(),
            })

    def log_shift(self, hours: float, note: str = "") -> None:
        if self.active_user:
            self.shifts[self.active_user.email].append({
                "hours": hours,
                "note": note,
                "time": datetime.now().isoformat(),
            })

    def thank(self, note: str) -> None:
        if self.active_user:
            self.thanks[self.active_user.email].append({
                "note": note,
                "time": datetime.now().isoformat(),
            })

    def records(self) -> dict:
        """Return a compact summary for the active user."""
        if not self.active_user:
            return {"error": "No active user"}
        return {
            "name": self.active_user.name,
            "emails": self.active_user.email,
            "signups": len(self.signups[self.active_user.email]),
            "shifts": len(self.shifts[self.active_user.email]),
            "hours": sum(s["hours"] for s in self.shifts[self.active_user.email]),
            "thanks": len(self.thanks[self.active_user.email]),
        }
