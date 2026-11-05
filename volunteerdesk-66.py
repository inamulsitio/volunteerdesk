# === Stage 66: Add export of a short status dashboard ===
# Project: VolunteerDesk
def print_status_dashboard(events):
    total_shifts = sum(len(e["shifts"]) for e in events)
    total_hours = round(sum(e["hours"] for e in events), 1)
    total_notes = sum(len(e["notes"]) for e in events)
    print("=" * 30)
    print(" VolunteerDesk Status ")
    print("=" * 30)
    print(f" Shifts scheduled : {total_shifts}")
    print(f" Hours logged     : {total_hours}")
    print(f" Thank-you notes  : {total_notes}")
    print("=" * 30)
