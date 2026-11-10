# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: VolunteerDesk
def compare_snapshots(before, after):
    """Compare two snapshots and report what changed."""
    changes = {}
    for key, before_value in before.items():
        after_value = after.get(key, None)
        if before_value != after_value:
            changes[key] = {"before": before_value, "after": after_value}
    return changes


def print_snapshot_comparison(before, after):
    """Print a readable before/after comparison of two snapshots."""
    changes = compare_snapshots(before, after)
    if not changes:
        print("No changes detected between snapshots.")
        return
    print("Snapshot comparison (before -> after):")
    for key, entry in changes.items():
        before_value = entry["before"]
        after_value = entry["after"]
        print(f"  {key}: {before_value!r} -> {after_value!r}")
