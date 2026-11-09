# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: VolunteerDesk
def cmd_clear_state(args, state):
    if not state.get("confirmed"):
        print("Confirm first with: confirm")
        return
    state["shifts"] = []
    state["signups"] = []
    state["hours"] = []
    state["thankyou"] = []
    print("State cleared.")
    state["confirmed"] = False
