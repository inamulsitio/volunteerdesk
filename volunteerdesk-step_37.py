# === Stage 37: Add recommendations for the next useful action ===
# Project: VolunteerDesk
def generate_shift_stats(attendance, shifts):
    """Generate simple statistics about shift attendance."""
    total_attendance = sum(len(s["attendees"]) for s in shifts)
    total_slots = len(shifts) * 3
    attendance_rate = (total_attendance / total_slots) * 100 if total_slots else 0
    print(f"Average attendance rate: {attendance_rate:.1f}%")
    print(f"Total attendance: {total_attendance} out of {total_slots} slots")

def calculate_volunteer_score(hours):
    """Calculate a simple score based on total hours worked."""
    score = 0
    if hours >= 10:
        score += 10
    elif hours >= 5:
        score += 5
    print(f"Volunteer score based on hours: {score}")
    return score
