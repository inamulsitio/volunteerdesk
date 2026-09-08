# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: VolunteerDesk
def case_insensitive_search(records, query):
    """Search volunteer records case-insensitively across name, email, and notes."""
    query = query.strip().lower()
    results = []
    for r in records:
        if query in r.get("name", "").lower() or \
           query in r.get("email", "").lower() or \
           query in r.get("notes", "").lower():
            results.append(r)
    return results
