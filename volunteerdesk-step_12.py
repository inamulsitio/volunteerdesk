# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: VolunteerDesk
import json

def load_volunteer_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{filepath}': {e}")
        return None
