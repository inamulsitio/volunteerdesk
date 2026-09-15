# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: VolunteerDesk
import re

def parse_date(date_str):
    """Parse date strings in common formats and return a datetime.date object.
    
    Supported formats:
    - YYYY-MM-DD
    - DD/MM/YYYY
    - DD Month YYYY (e.g., 15 March 2024)
    - Month DD, YYYY (e.g., March 15, 2024)
    
    Raises ValueError with a clear message if the date cannot be parsed.
    """
    date_str = date_str.strip()

    # Try YYYY-MM-DD
    try:
        return datetime.date.fromisoformat(date_str)
    except (ValueError, AttributeError):
        pass

    # Try DD/MM/YYYY
    try:
        parts = date_str.split('/')
        if len(parts) == 3:
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            return datetime.date(year, month, day)
    except (ValueError, AttributeError):
        pass

    # Try DD Month YYYY
    month_names = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    try:
        parts = date_str.split()
        if len(parts) == 3 and parts[1].lower() in month_names:
            day = int(parts[0])
            month = month_names[parts[1].lower()]
            year = int(parts[2])
            return datetime.date(year, month, day)
    except (ValueError, AttributeError):
        pass

    # Try Month DD, YYYY
    try:
        parts = date_str.split(',')
        if len(parts) == 2:
            month_str = parts[0].strip().lower()
            day_str = parts[1].strip()
            if month_str in month_names:
                day = int(day_str.split()[0])
                year = int(day_str.split()[-1])
                month = month_names[month_str]
                return datetime.date(year, month, day)
    except (ValueError, AttributeError):
        pass

    raise ValueError(f"Unable to parse date: '{date_str}'")

from datetime import datetime
