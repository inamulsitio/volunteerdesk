# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: VolunteerDesk
from typing import Dict, Optional, Tuple


def update_shift(
    shifts: Dict[str, Dict],
    volunteer_id: str,
    shift_id: str,
    new_hours: Optional[float] = None,
    new_status: Optional[str] = None,
    new_notes: Optional[str] = None,
) -> Tuple[bool, str]:
    if shift_id not in shifts:
        return False, f"Shift {shift_id} not found"
    shift = shifts[shift_id]
    if shift["volunteer_id"] != volunteer_id:
        return False, "Unauthorized"
    if new_hours is not None:
        shift["hours"] = new_hours
    if new_status is not None:
        shift["status"] = new_status
    if new_notes is not None:
        shift["notes"] = new_notes
    return True, "Updated"


def update_volunteer(
    volunteers: Dict[str, Dict],
    volunteer_id: str,
    new_name: Optional[str] = None,
    new_email: Optional[str] = None,
    new_phone: Optional[str] = None,
) -> Tuple[bool, str]:
    if volunteer_id not in volunteers:
        return False, f"Volunteer {volunteer_id} not found"
    v = volunteers[volunteer_id]
    if new_name is not None:
        v["name"] = new_name
    if new_email is not None:
        v["email"] = new_email
    if new_phone is not None:
        v["phone"] = new_phone
    return True, "Updated"


def update_note(
    notes: Dict[str, Dict],
    note_id: str,
    new_text: Optional[str] = None,
    new_sent: Optional[bool] = None,
) -> Tuple[bool, str]:
    if note_id not in notes:
        return False, f"Note {note_id} not found"
    n = notes[note_id]
    if new_text is not None:
        n["text"] = new_text
    if new_sent is not None:
        n["sent"] = new_sent
    return True, "Updated"
