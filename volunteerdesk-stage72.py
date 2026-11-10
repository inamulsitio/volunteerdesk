# === Stage 72: Add Markdown report export ===
# Project: VolunteerDesk
def export_markdown_report(path, shifts=None, signups=None, hours=None, notes=None):
    if shifts is None: shifts = []
    if signups is None: signups = []
    if hours is None: hours = []
    if notes is None: notes = []

    with open(path, "w", encoding="utf-8") as f:
        f.write("# VolunteerDesk Report\n\n")
        f.write("## Shifts\n\n")
        if shifts:
            for s in shifts:
                f.write(f"- {s.get('event','?')} on {s.get('date','?')} ({len(s.get('volunteers',[]))} volunteers)\n")
        else:
            f.write("_No shifts._\n")

        f.write("## Sign-ups\n\n")
        if signups:
            for u in signups:
                f.write(f"- {u.get('name','?')} signed up for {u.get('shift','?')}\n")
        else:
            f.write("_No sign-ups._\n")

        f.write("## Hours Logged\n\n")
        if hours:
            total = 0
            for h in hours:
                total += h.get("hours", 0)
                f.write(f"- {h.get('volunteer','?')}: {h.get('hours',0)}h\n")
            f.write(f"\n**Total hours: {total}**\n")
        else:
            f.write("_No hours logged._\n")

        f.write("## Thank-you Notes\n\n")
        if notes:
            for n in notes:
                f.write(f"- {n.get('volunteer','?')}: {n.get('message','')} \n")
        else:
            f.write("_No thank-you notes._\n")
