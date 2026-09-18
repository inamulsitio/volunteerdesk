# === Stage 41: Add plain text import for a simple line-based format ===
# Project: VolunteerDesk
def load_lines(path):
    """Read a file line-by-line, skipping blanks and comments."""
    with open(path, "r") as f:
        data = []
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            data.append(line)
    return data

def save_lines(path, lines):
    """Write a list of strings to a file, one per line."""
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")
