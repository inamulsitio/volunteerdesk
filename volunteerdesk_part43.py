# === Stage 43: Add CSV import for the primary record type ===
# Project: VolunteerDesk
def import_shifts(csv_path):
    """Import shifts from a CSV file.
    
    Expected columns: volunteer_id, event_id, start, end, note
    
    Args:
        csv_path (str): Path to the CSV file.
    
    Returns:
        list: List of Shift objects.
    """
    shifts = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            start = datetime.strptime(row['start'], '%Y-%m-%d %H:%M')
            end = datetime.strptime(row['end'], '%Y-%m-%d %H:%M')
            shift = Shift(
                volunteer_id=int(row['volunteer_id']),
                event_id=int(row['event_id']),
                start=start,
                end=end,
                note=row.get('note', '')
            )
            shifts.append(shift)
    return shifts
