# === Stage 81: Add final README text as a module string with usage examples ===
# Project: VolunteerDesk
def demo():
    from volunteerdesk import VolunteerDesk

    desk = VolunteerDesk("Sunrise Shelter")

    desk.add_shift(
        title="Morning Meal Prep",
        date="2024-06-01",
        start="07:00",
        end="09:00",
        location="Main Kitchen",
    )

    desk.add_signup(
        shift_title="Morning Meal Prep",
        date="2024-06-01",
        name="Alex Rivera",
        email="alex@example.com",
    )

    desk.add_signup(
        shift_title="Morning Meal Prep",
        date="2024-06-01",
        name="Sam Chen",
        email="sam@example.com",
    )

    desk.log_hours(
        name="Alex Rivera",
        date="2024-06-01",
        hours=2.0,
    )

    desk.thank_you("Alex Rivera", "Great work prepping meals this morning!")

    print("Schedule for 2024-06-01:")
    for shift in desk.get_shifts(date="2024-06-01"):
        signups = desk.get_signups(shift_title=shift["title"], date=shift["date"])
        print(f'  {shift["title"]} ({shift["start"]}-{shift["end"]}) - '
              f'{", ".join(s["name"] for s in signups)}')

    print("\nHours logged for Sam Chen:")
    for entry in desk.get_hours(name="Sam Chen"):
        print(f'  {entry["date"]}: {entry["hours"]} hours')

    print("\nThank-you notes:")
    for note in desk.get_thank_you():
        print(f'  To {note["name"]}: {note["message"]}')

    summary = desk.summary()
    print(f'\nSummary: {summary["total_shifts"]} shifts, '
          f'{summary["total_signups"]} signups, '
          f'{summary["total_hours"]} volunteer hours logged.')

if __name__ == "__main__":
    demo()
