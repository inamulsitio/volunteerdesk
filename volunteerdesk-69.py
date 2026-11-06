# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: VolunteerDesk
def reset_demo_data(db):
    db["shifts"].clear()
    db["signups"].clear()
    db["hours"].clear()
    db["notes"].clear()
    orgs = {
        "Community Garden": {"address": "12 Green St", "email": "garden@example.com", "phone": "555-0101"},
        "Food Bank": {"address": "90 Harvest Ave", "email": "foodbank@example.com", "phone": "555-0102"},
    }
    for name, info in orgs.items():
        db["organizations"].append({"name": name, **info})
    db["volunteers"].append({"name": "Alex Kim", "email": "alex@example.com", "phone": "555-0201"})
    db["volunteers"].append({"name": "Sam Rivera", "email": "sam@example.com", "phone": "555-0202"})
    shifts = [
        {"date": "2024-06-01", "start": "09:00", "end": "12:00", "organization": "Community Garden", "role": "Planting", "volunteers": 3},
        {"date": "2024-06-08", "start": "10:00", "end": "13:00", "organization": "Food Bank", "role": "Sorting", "volunteers": 2},
    ]
    for s in shifts:
        db["shifts"].append(s)
    db["signups"].append({"volunteer": "Alex Kim", "shift": shifts[0]["date"], "role": "Planting"})
    db["signups"].append({"volunteer": "Sam Rivera", "shift": shifts[1]["date"], "role": "Sorting"})
    db["hours"].append({"volunteer": "Alex Kim", "shift": shifts[0]["date"], "hours": 3.0})
    db["hours"].append({"volunteer": "Sam Rivera", "shift": shifts[1]["date"], "hours": 3.0})
    db["notes"].append({"volunteer": "Alex Kim", "message": "Great work at the garden this weekend!"})
    db["notes"].append({"volunteer": "Sam Rivera", "message": "Thank you for sorting donations!"})
