# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: VolunteerDesk
def describe_volunteer(name, hours):
    if hours >= 100:
        return f"Thank you, {name}. Your {hours} hours of service are truly inspiring."
    elif hours >= 50:
        return f"Thank you, {name}. Your {hours} hours of dedication make a real difference."
    elif hours >= 20:
        return f"Thank you, {name}. Your {hours} hours of volunteer work are warmly appreciated."
    else:
        return f"Thank you, {name}. Your {hours} hours of volunteer time are much valued."


def greet_volunteer(name):
    return f"Welcome back, {name}. We look forward to seeing you at your next shift."


def farewell_volunteer(name):
    return f"Goodbye, {name}. Your contributions will not be forgotten."


def confirm_sign_up(volunteer_name, shift_name, date):
    return f"Confirmed: {volunteer_name} signed up for the {shift_name} shift on {date}."


def reject_sign_up(volunteer_name, reason):
    return f"Sorry, {volunteer_name}. Your sign-up could not be completed because {reason}."


def thank_you_note(volunteer_name, hours, event_name):
    return (
        f"Dear {volunteer_name},\n\n"
        f"Thank you for your generous {hours} hours of volunteer service at the {event_name}.\n\n"
        f"Your dedication and kindness made this event possible. We are truly grateful for all you do.\n\n"
        f"With appreciation,\n"
        f"The VolunteerDesk Team"
    )


def monthly_report_header(month, year):
    return f"VolunteerDesk Monthly Report - {month} {year}"
