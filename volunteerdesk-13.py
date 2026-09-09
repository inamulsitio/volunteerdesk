# === Stage 13: Add file save support using a configurable path ===
# Project: VolunteerDesk
import json, os

SAVE_PATH = os.environ.get("VOL_DESK_PATH", "volunteer_desk.json")

def save_state():
    with open(SAVE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def load_state():
    if os.path.exists(SAVE_PATH):
        with open(SAVE_PATH, "r") as f:
            return json.load(f)
    return {}
