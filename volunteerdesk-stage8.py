# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: VolunteerDesk
def filter_records(records, filters=None):
    """Filter volunteer records by status, category, owner, or tag.

    Args:
        records: A list of record dicts (each with keys like 'status',
                 'category', 'owner', 'tag').
        filters: An optional dict specifying which keys to filter on and
                 the expected values. Keys: 'status', 'category', 'owner', 'tag'.

    Returns:
        A list of records matching all provided filter criteria.
    """
    if filters is None:
        return records
    result = []
    for record in records:
        match = True
        for key, expected in filters.items():
            if record.get(key) != expected:
                match = False
                break
        if match:
            result.append(record)
    return result
