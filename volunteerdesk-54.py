# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: VolunteerDesk
def color(text: str, code: int) -> str:
    return f"\033[{code}m{text}\033[0m"

def print_header():
    print(color("╔══════════════════════════╗", 36))
    print(color("║  VolunteerDesk App       ║", 36))
    print(color("╚══════════════════════════╝", 36))

def print_menu():
    print(color("  1. Show shifts", 32))
    print(color("  2. Add shift", 32))
    print(color("  3. Sign up", 32))
    print(color("  4. Log hours", 32))
    print(color("  5. Thank-you notes", 32))
    print(color("  0. Exit", 31))

def print_success(msg):
    print(color(f"  ✓ {msg}", 32))

def print_error(msg):
    print(color(f"  ✗ {msg}", 31))

def print_info(msg):
    print(color(f"  i {msg}", 36))
