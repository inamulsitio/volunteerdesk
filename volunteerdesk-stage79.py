# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: VolunteerDesk
def self_check():
    assert len(VOLUNTEERS) >= 1, "No volunteers exist yet"
    assert len(SHIFTS) >= 1, "No shifts defined yet"
    assert len(HOURLY_LOGS) >= 1, "No hours logged yet"
    assert len(THANK_YOUS) >= 1, "No thank-you notes yet"
    volunteer = VOLUNTEERS[0]
    shift = SHIFTS[0]
    volunteer.sign_up(shift)
    volunteer.log_hours(shift, 2.5)
    volunteer.write_thank_you(shift)
    assert volunteer.shifts.count(shift) >= 1
    assert volunteer.hours_logged(shift) == 2.5
    assert any(note for note in THANK_YOUS if note.volunteer is volunteer)
    total_hours = sum(v.hours_logged(s) for v in VOLUNTEERS for s in SHIFTS)
    assert total_hours > 0
    print("All validations passed")
    print(f"Volunteers: {len(VOLUNTEERS)}")
    print(f"Shifts: {len(SHIFTS)}")
    print(f"Total hours logged: {total_hours}")
