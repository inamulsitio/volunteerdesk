# === Stage 83: Add regression tests for the final demo workflow ===
# Project: VolunteerDesk
def run_demo_workflow():
    from volunteerdesk import VolunteerDesk, Shift, Volunteer, ThankYouNote
    desk = VolunteerDesk()
    desk.add_volunteer(Volunteer("Ada", "ada@example.com"))
    desk.add_shift(Shift("2026-01-05", "10:00", "13:00", "Greeter", "Ada"))
    desk.register("Ada", "2026-01-05")
    desk.log_hours("Ada", 3.0)
    desk.write_thank_you("Ada", "Great work greeting everyone today!")
    shifts = desk.get_shifts()
    assert len(shifts) == 1 and shifts[0].title == "Greeter"
    signed = desk.get_signed_up("2026-01-05")
    assert len(signed) == 1 and signed[0] == "Ada"
    hours = desk.get_hours("Ada")
    assert hours == 3.0
    notes = desk.get_thank_you_notes("Ada")
    assert len(notes) == 1 and "Great work" in notes[0].body
    return True

if __name__ == "__main__":
    assert run_demo_workflow()
