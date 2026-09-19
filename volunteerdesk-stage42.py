# === Stage 42: Add CSV export without external dependencies ===
# Project: VolunteerDesk
import csv
import os

def export_to_csv(data, filename="volunteer_desk_export.csv"):
    """Export volunteer desk data to a CSV file."""
    if not data:
        print("No data to export.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Phone", "Age", "Role", "Status", "Hours Logged"])
        for volunteer in data:
            writer.writerow([
                volunteer["name"],
                volunteer["email"],
                volunteer["phone"],
                volunteer["age"],
                volunteer["role"],
                volunteer["status"],
                volunteer["hours_logged"]
            ])
    print(f"Data exported to {filename} ({len(data)} records).")
