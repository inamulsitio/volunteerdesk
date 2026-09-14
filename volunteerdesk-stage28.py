# === Stage 28: Add overdue item detection based on due dates ===
# Project: VolunteerDesk
def detect_overdue_items(items, reference_date=None):
    """Identify items with due dates that have passed.

    Args:
        items: list of dicts, each containing a 'due_date' field.
        reference_date: date or datetime to compare against (default: today).

    Returns:
        list of dicts with the same structure plus 'is_overdue' and
        'days_overdue' keys.
    """
    if reference_date is None:
        from datetime import date, datetime
        reference_date = date.today() if isinstance(date.today(), date) else datetime.now().date()

    overdue = []
    for item in items:
        due = item.get('due_date')
        if due is None:
            continue
        due_date = due if isinstance(due, date) else due.replace(hour=0, minute=0, second=0, microsecond=0)
        days_over = (reference_date - due_date).days
        entry = dict(item)
        entry['is_overdue'] = days_over > 0
        entry['days_overdue'] = days_over
        overdue.append(entry)
    return overdue
