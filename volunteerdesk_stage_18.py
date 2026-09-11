# === Stage 18: Add an activity log with timestamps and action names ===
# Project: VolunteerDesk
import time

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, actor, timestamp=None):
        if timestamp is None:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.entries.append({"action": action, "actor": actor, "timestamp": timestamp})

    def get_log(self):
        return self.entries

    def clear_log(self):
        self.entries.clear()

    def __str__(self):
        return "\n".join(f"{e['timestamp']} | {e['actor']} | {e['action']}" for e in self.entries)
