# === Stage 64: Add validation for relationship references ===
# Project: VolunteerDesk
def validate_references(data):
    errors = []
    if not isinstance(data, dict):
        return errors, "Root must be a dictionary."
    if 'volunteers' in data and not isinstance(data['volunteers'], list):
        errors.append("'volunteers' must be a list.")
    if 'events' in data and not isinstance(data['events'], list):
        errors.append("'events' must be a list.")
    if 'shifts' in data and not isinstance(data['shifts'], list):
        errors.append("'shifts' must be a list.")
    if 'thank_you_notes' in data and not isinstance(data['thank_you_notes'], list):
        errors.append("'thank_you_notes' must be a list.")
    valid_volunteer_ids = {v.get('id') for v in data.get('volunteers', [])}
    valid_event_ids = {e.get('id') for e in data.get('events', [])}
    for shift in data.get('shifts', []):
        if shift.get('volunteer_id') not in valid_volunteer_ids:
            errors.append(f"Shift {shift.get('id')} references unknown volunteer_id.")
        if shift.get('event_id') not in valid_event_ids:
            errors.append(f"Shift {shift.get('id')} references unknown event_id.")
    for note in data.get('thank_you_notes', []):
        if note.get('volunteer_id') not in valid_volunteer_ids:
            errors.append(f"Thank-you note {note.get('id')} references unknown volunteer_id.")
    return errors, "" if not errors else "\n".join(errors)
