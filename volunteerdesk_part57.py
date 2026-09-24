# === Stage 57: Add structured result objects for command handlers ===
# Project: VolunteerDesk
from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class CommandResult:
    success: bool
    message: str
    data: Optional[Any] = None

    def to_dict(self) -> dict:
        result = {"success": self.success, "message": self.message}
        if self.data is not None:
            result["data"] = self.data
        return result

@dataclass
class ShiftResult:
    success: bool
    shift_id: Optional[int] = None
    volunteer_id: Optional[int] = None
    shift_date: Optional[str] = None
    message: str = ""

    def to_dict(self) -> dict:
        result = {"success": self.success, "message": self.message}
        if self.shift_id is not None:
            result["shift_id"] = self.shift_id
        if self.volunteer_id is not None:
            result["volunteer_id"] = self.volunteer_id
        if self.shift_date is not None:
            result["shift_date"] = self.shift_date
        return result

@dataclass
class HoursResult:
    success: bool
    volunteer_id: Optional[int] = None
    hours: Optional[float] = None
    date: Optional[str] = None
    message: str = ""

    def to_dict(self) -> dict:
        result = {"success": self.success, "message": self.message}
        if self.volunteer_id is not None:
            result["volunteer_id"] = self.volunteer_id
        if self.hours is not None:
            result["hours"] = self.hours
        if self.date is not None:
            result["date"] = self.date
        return result

@dataclass
class NoteResult:
    success: bool
    note_id: Optional[int] = None
    volunteer_id: Optional[int] = None
    message: str = ""

    def to_dict(self) -> dict:
        result = {"success": self.success, "message": self.message}
        if self.note_id is not None:
            result["note_id"] = self.note_id
        if self.volunteer_id is not None:
            result["volunteer_id"] = self.volunteer_id
        return result
