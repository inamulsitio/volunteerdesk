# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: VolunteerDesk
# Step 33: Add settings dictionary and update functions to VolunteerDesk.py

class VolunteerDeskSettings:
    def __init__(self):
        self.settings = {
            "app_name": "VolunteerDesk",
            "version": "1.0",
            "max_shifts_per_volunteer": 5,
            "min_hours_for_badge": 50,
            "thank_you_note_enabled": True,
            "shift_reminder_days_before": 1,
            "default_shift_duration_hours": 4,
            "working_hours_start": "08:00",
            "working_hours_end": "20:00",
            "contact_email": "volunteer@example.com",
            "contact_phone": "555-0123",
            "social_media_link": "https://volunteerdesk.example.com",
            "dark_mode": False,
        }

    def update_setting(self, key, value):
        if key in self.settings:
            self.settings[key] = value
            return True
        return False

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def toggle_dark_mode(self):
        self.settings["dark_mode"] = not self.settings["dark_mode"]
        return self.settings["dark_mode"]

    def to_dict(self):
        return dict(self.settings)

    def from_dict(self, data):
        for key, value in data.items():
            self.settings[key] = value

# Example usage
settings = VolunteerDeskSettings()
settings.update_setting("dark_mode", True)
print(settings.get_setting("dark_mode"))  # True
settings.toggle_dark_mode()
print(settings.get_setting("dark_mode"))  # False
print(settings.to_dict())
