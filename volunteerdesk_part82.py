# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: VolunteerDesk
def demo_end_to_end():
    desk = VolunteerDesk("Community Food Bank")
    desk.add_shift("Saturday", "9:00", "12:00", "Sorting & Packing")
    desk.add_shift("Sunday", "10:00", "13:00", "Meal Prep")

    desk.register_volunteer("Ana", "ana@example.com")
    desk.register_volunteer("Ben", "ben@example.com")
    desk.assign("Ana", "Saturday", "Sorting & Packing")
    desk.assign("Ben", "Sunday", "Meal Prep")

    desk.log_hours("Ana", 3.5)
    desk.log_hours("Ben", 2.0)

    desk.write_thank_you("Ana", "For your dedication sorting food every weekend!")

    desk.print_overview()
    desk.print_volunteer("Ana")
    desk.print_shifts_for("Saturday")
    desk.print_recent_thank_you()

    print("VolunteerDesk demo complete.")

demo_end_to_end()
