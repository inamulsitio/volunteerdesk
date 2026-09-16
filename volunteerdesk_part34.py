# === Stage 34: Add support for multiple local user profiles ===
# Project: VolunteerDesk
import os, json

def load_profiles(path="profiles.json"):
    """Load user profiles from a JSON file. Create an empty file if missing."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump([], f)
    with open(path) as f:
        return json.load(f)

def save_profiles(profiles, path="profiles.json"):
    """Save user profiles to a JSON file."""
    with open(path, "w") as f:
        json.dump(profiles, f, indent=2)

def add_profile(name, email, phone="", role="volunteer"):
    """Add a new profile and return it."""
    profiles = load_profiles()
    profiles.append({"name": name, "email": email, "phone": phone, "role": role})
    save_profiles(profiles)
    return profiles[-1]

def get_profile(name):
    """Look up a profile by name."""
    profiles = load_profiles()
    for p in profiles:
        if p["name"].lower() == name.lower():
            return p
    return None
