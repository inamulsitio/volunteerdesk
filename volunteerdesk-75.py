# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: VolunteerDesk
def validate_desk(desk):
    warnings = []
    errors = []
    for shift in desk["shifts"].values():
        if shift.get("start") >= shift.get("end"):
            errors.append(f"Shift {shift['id']} has end before or equal to start")
        for signup in shift.get("signups", []):
            if signup.get("hours") > shift.get("duration", 0):
                warnings.append(f"Signup {signup['id']} logged more hours than shift duration")
    for person in desk["people"].values():
        if person.get("email") and "@" not in person["email"]:
            errors.append(f"Person {person['id']} has invalid email {person['email']}")
        if person.get("phone") and not person["phone"].isdigit():
            warnings.append(f"Person {person['id']} has non-numeric phone {person['phone']}")
    for note in desk.get("thank_you_notes", []):
        if not note.get("message"):
            warnings.append(f"Thank-you note {note['id']} has empty message")
    if desk.get("settings", {}).get("require_confirmation") and not desk.get("confirmation_enabled"):
        warnings.append("Confirmation required but confirmation is not enabled")
    return {"warnings": warnings, "errors": errors}
