# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: VolunteerDesk
def test_delete_volunteer():
    volunteer = Volunteer(name="Alice", email="alice@example.com")
    volunteer_id = volunteer.generate_id()
    volunteer_db.insert(volunteer_id, volunteer)
    assert volunteer_db.find(volunteer_id) is not None
    assert volunteer_db.delete(volunteer_id) == 1
    assert volunteer_db.find(volunteer_id) is None

def test_update_nonexistent():
    volunteer_db.delete_all()
    assert volunteer_db.update("nonexistent_id", name="Bob") == 0

def test_delete_shift():
    volunteer = Volunteer(name="Charlie", email="charlie@example.com")
    shift = Shift(volunteer_id=volunteer.generate_id(), date="2024-06-15", hours=3)
    shift_id = shift.generate_id()
    volunteer_db.insert(volunteer.generate_id(), volunteer)
    shift_db.insert(shift_id, shift)
    assert shift_db.delete(shift_id) == 1
    assert shift_db.find(shift_id) is None

def test_update_shift_date():
    volunteer = Volunteer(name="Diana", email="diana@example.com")
    shift = Shift(volunteer_id=volunteer.generate_id(), date="2024-06-15", hours=2)
    shift_id = shift.generate_id()
    volunteer_db.insert(volunteer.generate_id(), volunteer)
    shift_db.insert(shift_id, shift)
    shift_db.update(shift_id, date="2024-06-20")
    updated = shift_db.find(shift_id)
    assert updated.date == "2024-06-20"
    assert updated.hours == 2
