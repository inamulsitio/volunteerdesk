# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: VolunteerDesk
def add_tag(note):
    note["tags"] = note.get("tags", [])
    if "thank-you" not in note["tags"]:
        note["tags"].append("thank-you")
        note["created_at"] = note.get("created_at", "now")
        return note

def remove_tag(note, tag_name):
    if tag_name in note.get("tags", []):
        note["tags"].remove(tag_name)
        return note
    return note

def tag_summary(note):
    tags = note.get("tags", [])
    return {
        "status": "Thank You" if "thank-you" in tags else "Pending",
        "tags": tags,
        "created_at": note.get("created_at", "unknown")
    }
