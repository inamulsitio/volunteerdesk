# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: VolunteerDesk
# VolunteerDesk – demo scenario exercising the main workflow
# Usage:  python volunteer_desk_demo.py

from volunteer_desk import (
    VolunteerDesk, Volunteer, Shift, ShiftType,
)

desk = VolunteerDesk()

# --- 1. Create volunteers ---------------------------------------------------
vol1 = Volunteer(name="Alice", email="alice@example.com")
vol2 = Volunteer(name="Bob", email="bob@example.com")
vol3 = Volunteer(name="Charlie", email="charlie@example.com")
desk.add_volunteer(vol1)
desk.add_volunteer(vol2)
desk.add_volunteer(vol3)

# --- 2. Create shifts -------------------------------------------------------
morning = Shift("Morning", start="09:00", end="13:00", type=ShiftType.MORNING)
afternoon = Shift("Afternoon", start="14:00", end="18:00", type=ShiftType.AFTERNOON)
desk.add_shift(morning)
desk.add_shift(afternoon)

# --- 3. Sign up volunteers for shifts ----------------------------------------
desk.sign_up(vol1, morning)
desk.sign_up(vol2, afternoon)
desk.sign_up(vol3, morning)

# --- 4. Log hours worked ----------------------------------------------------
desk.log_hours(vol1, morning, 3.5)
desk.log_hours(vol2, afternoon, 2.0)
desk.log_hours(vol3, morning, 2.5)

# --- 5. Write thank-you notes -----------------------------------------------
desk.write_thank_you_note(vol1, "Great work today!")
desk.write_thank_you_note(vol2, "Thank you for your help.")
desk.write_thank_you_note(vol3, "You're a rockstar!")

# --- 6. Print summary -------------------------------------------------------
desk.print_summary()
