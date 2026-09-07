# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: VolunteerDesk
def delete_record(record_id, confirm=False):
    """Delete a record by ID with optional confirmation flag."""
    records = load_records()
    if not records:
        print("No records to delete.")
        return
    for r in records:
        if r["id"] == record_id:
            if not confirm:
                print(f"Record {record_id} deleted (unconfirmed).")
            else:
                print(f"Record {record_id} deleted (confirmed).")
            records.remove(r)
            save_records(records)
            return
    print(f"Record {record_id} not found.")
