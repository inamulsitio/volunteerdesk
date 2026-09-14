# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: VolunteerDesk
def upcoming_shifts(shifts, days=7):
    from datetime import datetime, timedelta
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    upcoming = []
    for s in sorted(shifts, key=lambda x: x['start'], reverse=True):
        start = datetime.combine(s['start'].date(), s['start'].time())
        end = datetime.combine(s['end'].date(), s['end'].time())
        if start.date() >= tomorrow and end.date() <= today + timedelta(days=days):
            upcoming.append({
                'volunteer': s['volunteer'],
                'role': s['role'],
                'start': s['start'],
                'end': s['end'],
                'location': s['location'],
            })
    return upcoming

def upcoming_tasks(tasks, days=7):
    from datetime import datetime, timedelta
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    upcoming = []
    for t in sorted(tasks, key=lambda x: x['due'], reverse=True):
        due = datetime.combine(t['due'].date(), t.get('created', t['due']).time())
        if due.date() >= tomorrow and due.date() <= today + timedelta(days=days):
            upcoming.append({
                'task': t['task'],
                'due': t['due'],
                'assigned': t['assigned'],
                'priority': t['priority'],
            })
    return upcoming
