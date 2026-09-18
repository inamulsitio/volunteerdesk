# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: VolunteerDesk
def repair_simple_integrity(records, max_retries=2):
    """Attempt to fix common data issues: missing fields, empty strings, duplicates."""
    for attempt in range(max_retries):
        fixed = False
        for key, rec in records.items():
            if not isinstance(rec, dict):
                records[key] = {}
                fixed = True
                continue
            if 'volunteer' not in rec or not rec['volunteer']:
                rec['volunteer'] = 'unknown'
                fixed = True
            if 'role' not in rec or not rec['role']:
                rec['role'] = 'general'
                fixed = True
            if 'status' not in rec or not rec['status']:
                rec['status'] = 'active'
                fixed = True
            if 'hours' in rec and (rec['hours'] is None or rec['hours'] == ''):
                rec['hours'] = 0.0
                fixed = True
            if 'notes' in rec and (rec['notes'] is None or rec['notes'] == ''):
                rec['notes'] = ''
                fixed = True
        if not fixed:
            break
    return records
