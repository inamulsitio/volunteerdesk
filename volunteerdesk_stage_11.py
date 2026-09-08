# === Stage 11: Add JSON export for the current application state ===
# Project: VolunteerDesk
def export_state():
    """Export the entire VolunteerDesk state to a JSON file."""
    import json
    with open("volunteer_desk_state.json", "w") as f:
        json.dump({
            "shifts": shifts,
            "signups": signups,
            "hours_logged": hours_logged,
            "thank_you_notes": thank_you_notes
        }, f, indent=2)
    print("State exported to volunteer_desk_state.json")
