# === Stage 40: Add plain text report export ===
# Project: VolunteerDesk
def export_report(shifts, signups, hours, notes):
    with open("volunteer_desk_report.txt", "w") as f:
        f.write("VolunteerDesk Report\n")
        f.write("=" * 40 + "\n")
        f.write(f"Total shifts: {len(shifts)}\n")
        f.write(f"Total sign-ups: {len(signups)}\n")
        total_hours = sum(h["hours"] for h in hours.values())
        f.write(f"Total hours logged: {total_hours}\n")
        f.write(f"Thank-you notes: {len(notes)}\n")
        f.write("\n--- Shifts ---\n")
        for s in shifts:
            f.write(f"  {s['role']} - {s['date']} - {s['time']} hrs\n")
        f.write("\n--- Sign-ups ---\n")
        for name, count in signups.items():
            f.write(f"  {name}: {count} shift(s)\n")
        f.write("\n--- Thank-you notes ---\n")
        for name, note in notes.items():
            f.write(f"  {name}: {note}\n")
    return "Report saved to volunteer_desk_report.txt"
