# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: VolunteerDesk
def seed_demo_data(store):
    store['shifts'] = [
        {'id': 1, 'event': 'Community Cleanup', 'role': 'Sorting', 'start': '2025-01-10T09:00:00', 'end': '2025-01-10T12:00:00'},
        {'id': 2, 'event': 'Community Cleanup', 'role': 'Bagging', 'start': '2025-01-10T09:00:00', 'end': '2025-01-10T12:00:00'},
        {'id': 3, 'event': 'Food Drive', 'role': 'Greeter', 'start': '2025-01-11T10:00:00', 'end': '2025-01-11T13:00:00'},
    ]
    store['volunteers'] = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    ]
    store['signups'] = [
        {'id': 1, 'volunteer_id': 1, 'shift_id': 1, 'status': 'confirmed'},
        {'id': 2, 'volunteer_id': 2, 'shift_id': 2, 'status': 'confirmed'},
        {'id': 3, 'volunteer_id': 1, 'shift_id': 3, 'status': 'pending'},
    ]
    store['hours'] = [
        {'id': 1, 'volunteer_id': 1, 'shift_id': 1, 'hours': 3},
        {'id': 2, 'volunteer_id': 2, 'shift_id': 2, 'hours': 2.5},
    ]
    store['thank_you_notes'] = [
        {'id': 1, 'volunteer_id': 1, 'message': 'Thanks for sorting the donations, Alice!', 'sent': True},
        {'id': 2, 'volunteer_id': 2, 'message': 'Bob, appreciate your help at the food drive.', 'sent': False},
    ]
