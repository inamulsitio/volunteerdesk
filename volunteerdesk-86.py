# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: VolunteerDesk
def demo_cli():
    """Sample transcripts for the main VolunteerDesk CLI workflows."""
    print("VolunteerDesk CLI demo")
    print("1) Create desk: desk create 'Community Kitchen'")
    print("2) Add shift: shift add 'Saturday Morning' '2025-06-07' '09:00' '12:00'")
    print("3) Sign up: sign-up add 'Ana' 'Saturday Morning'")
    print("4) Log hours: hours log 'Ana' 'Saturday Morning' 2.5")
    print("5) List volunteers: volunteers list")
    print("6) Send thank-you note: note send 'Ana' 'Thanks for your help!')")
    print("7) Summary: summary")
    print("8) Help: help")
    print("Run each command against the VolunteerDesk database.")
