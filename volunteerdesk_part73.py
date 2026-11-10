# === Stage 73: Add a lightweight HTML report export ===
# Project: VolunteerDesk
def export_report(path, volunteers, shifts, signups, thank_you):
    with open(path, "w") as f:
        f.write("VolunteerDesk Report\n")
        f.write("=" * 30 + "\n")
        for v in volunteers:
            hours = sum(s.hours for s in shifts if s.volunteer_id == v["id"])
            f.write(f"Volunteer {v['name']} - {hours} hours\n")
        for s in shifts:
            f.write(f"Shift: {s.title} on {s.date} ({s.count} volunteers)\n")
        for s in signups:
            f.write(f"Signed up {s.volunteer_name} for {s.shift} on {s.date}\n")
        for t in thank_you:
            f.write(f"Thank you note to {t.volunteer_name}: {t.message}\n")
