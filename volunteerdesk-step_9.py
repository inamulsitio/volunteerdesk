# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: VolunteerDesk
from datetime import datetime

def _sort_key(item):
    return (item.get('priority', 0), item.get('last_updated', datetime.min), item.get('title', ''), item.get('date', datetime.min))

def sort_volunteers(sort_by='title', reverse=False):
    sort_map = {
        'title': ('title', True),
        'date': ('date', False),
        'priority': ('priority', False),
        'last_update': ('last_updated', False),
    }
    if sort_by not in sort_map:
        sort_by = 'title'
    key, reverse = sort_map[sort_by]
    return sorted(volunteers, key=lambda v: v.get(key, datetime.min) if key != 'title' else v.get(key, ''), reverse=reverse)
