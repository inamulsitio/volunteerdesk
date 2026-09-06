# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: VolunteerDesk
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Optional


@dataclass
class Volunteer:
    name: str
    email: str
    phone: str
    date_joined: date


@dataclass
class Shift:
    title: str
    date: date
    start_time: str
    end_time: str
    location: str
    max_volunteers: int
    assigned: list[Volunteer] = field(default_factory=list)


@dataclass
class Signup:
    volunteer: Volunteer
    shift: Shift
    signed_up_at: datetime = field(default_factory=datetime.now)


@dataclass
class HoursLog:
    volunteer: Volunteer
    date: date
    hours_worked: float


@dataclass
class ThankYouNote:
    volunteer: Volunteer
    message: str
    date: datetime = field(default_factory=datetime.now)
