# === Stage 55: Add a setting to disable colorized output ===
# Project: VolunteerDesk
import sys

def disable_color():
    """Disable colorized output when running in non-TTY environments."""
    if not sys.stdout.isatty():
        os.environ['NO_COLOR'] = '1'
        os.environ['FORCE_COLOR'] = '0'
