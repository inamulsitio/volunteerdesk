# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: VolunteerDesk
import json, os

BASE = os.path.join(os.path.dirname(__file__) or '.', 'volunteer_desk')
os.makedirs(BASE, exist_ok=True)

state = {
    "users": [
        {"id": 1, "name": "Alice Chen", "email": "alice@example.com", "role": "admin"},
        {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "role": "volunteer"},
        {"id": 3, "name": "Carol Park", "email": "carol@example.com", "role": "volunteer"},
        {"id": 4, "name": "Dan Lee", "email": "dan@example.com", "role": "volunteer"},
    ],
    "shifts": [
        {"id": 1, "title": "Front Desk", "date": "2026-05-10", "duration_hours": 4, "slots": 3, "signed_up": [1]},
        {"id": 2, "title": "Data Entry", "date": "2026-05-11", "duration_hours": 3, "slots": 2, "signed_up": [2, 3]},
        {"id": 3, "title": "Community Outreach", "date": "2026-05-12", "duration_hours": 5, "slots": 4, "signed_up": []},
    ],
    "hours": [
        {"user_id": 1, "shift_id": 1, "hours": 4},
        {"user_id": 2, "shift_id": 2, "hours": 3},
        {"user_id": 3, "shift_id": 2, "hours": 3},
    ],
    "notes": [
        {"user_id": 1, "to_user_id": 2, "text": "Great work at the front desk!", "date": "2026-05-10"},
        {"user_id": 1, "to_user_id": 3, "text": "Thank you for your dedication.", "date": "2026-05-11"},
    ]
}

def save():
    with open(os.path.join(BASE, 'state.json'), 'w') as f:
        json.dump(state, f, indent=2)

save()
print(f"VolunteerDesk initialized with {len(state['users'])} users, {len(state['shifts'])} shifts, {len(state['hours'])} hours records, {len(state['notes'])} notes.")
