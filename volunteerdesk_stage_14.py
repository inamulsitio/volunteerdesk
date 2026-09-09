# === Stage 14: Add file load support with fallback demo data ===
# Project: VolunteerDesk
def load_data(path=None):
    """Load volunteer data from a JSON file, falling back to demo data."""
    if path is None:
        path = "volunteer_data.json"
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return _demo_data()

def _demo_data():
    return {
        "volunteers": [
            {"id": 1, "name": "Alice", "email": "alice@example.com", "hours": 15.0, "notes": "Great at reception"},
            {"id": 2, "name": "Bob", "email": "bob@example.com", "hours": 8.5, "notes": "Helpful with logistics"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com", "hours": 20.0, "notes": "Excellent communication"},
        ],
        "shifts": [
            {"id": 1, "title": "Morning Reception", "date": "2024-06-01", "volunteer_id": 1},
            {"id": 2, "title": "Afternoon Logistics", "date": "2024-06-01", "volunteer_id": 2},
        ],
        "thank_you_notes": [
            {"id": 1, "volunteer_id": 1, "message": "Thank you for your dedication!", "date": "2024-06-15"},
        ],
        "settings": {
            "org_name": "VolunteerDesk Demo",
            "contact_email": "info@volunteerdesk.demo",
        },
    }
