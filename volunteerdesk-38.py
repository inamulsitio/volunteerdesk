# === Stage 38: Add data integrity checks for broken references ===
# Project: VolunteerDesk
def check_integrity(data):
    """Validate that all foreign references point to existing primary keys."""
    errors = []
    if "volunteers" in data and "shifts" in data:
        shift_ids = {s["id"] for s in data["shifts"]}
        for v in data["volunteers"]:
            if v.get("current_shift_id") and v["current_shift_id"] not in shift_ids:
                errors.append(f"Volunteer {v['id']} references non-existent shift {v['current_shift_id']}")
            for s in v.get("shift_history", []):
                if s["shift_id"] not in shift_ids:
                    errors.append(f"Volunteer {v['id']} history references non-existent shift {s['shift_id']}")
    if "volunteers" in data and "notes" in data:
        volunteer_ids = {v["id"] for v in data["volunteers"]}
        for n in data["notes"]:
            if n.get("volunteer_id") and n["volunteer_id"] not in volunteer_ids:
                errors.append(f"Note {n['id']} references non-existent volunteer {n['volunteer_id']}")
            if n.get("recipient_id") and n["recipient_id"] not in volunteer_ids:
                errors.append(f"Note {n['id']} references non-existent recipient {n['recipient_id']}")
    if errors:
        print("Data integrity errors found:")
        for e in errors:
            print(f"  - {e}")
        return False
    print("All references are valid.")
    return True
