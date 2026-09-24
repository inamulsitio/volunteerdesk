# === Stage 58: Add bulk update behavior for selected records ===
# Project: VolunteerDesk
def bulk_update_records(self, updates):
    """Apply a list of (record_type, identifier, new_values) tuples."""
    for record_type, identifier, new_values in updates:
        if record_type == 'volunteer':
            self._volunteers[identifier].update(new_values)
        elif record_type == 'shift':
            self._shifts[identifier].update(new_values)
        elif record_type == 'signup':
            self._signups[identifier].update(new_values)
        elif record_type == 'note':
            self._notes[identifier].update(new_values)
        elif record_type == 'hour':
            self._hours[identifier].update(new_values)
        else:
            raise ValueError(f'Unknown record type: {record_type}')
