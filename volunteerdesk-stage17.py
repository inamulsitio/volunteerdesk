# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: VolunteerDesk
import sys

def dry_run_guard(action, target, dry_run=False):
    if dry_run:
        print(f"[DRY-RUN] Would {action} {target}")
        return None
    return execute(action, target)
