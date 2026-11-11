# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: VolunteerDesk
def main():
    try:
        while True:
            cmd = input("volunteerdesk> ").strip()
            if not cmd:
                continue
            parts = cmd.split(maxsplit=1)
            action = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""
            if action in ("quit", "exit", "q"):
                print("Goodbye!")
                break
            elif action in ("help", "?"):
                print("Commands: shifts, signups, hours, thank-you, list, quit")
            else:
                print("Unknown command:", action)
    except (KeyboardInterrupt, EOFError):
        print()
        print("Interrupted. Exiting VolunteerDesk.")
        sys.exit(0)


if __name__ == "__main__":
    main()
