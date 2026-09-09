# === Stage 16: Add argparse support for the most common commands ===
# Project: VolunteerDesk
import argparse
from collections import defaultdict

PARSER = argparse.ArgumentParser(
    description="VolunteerDesk CLI – manage shifts, sign-ups, hours, and notes",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
PARSER.add_argument("--db", "-d", default="vdesk.db", help="Path to SQLite database")
PARSER.add_argument("--format", "-f", choices=["json", "csv"], default="json", help="Output format")


def _parse_shift(args):
    p = PARSER.add_subparsers(dest="command")
    s = p.add_parser("shift", help="Shift management")
    s.add_argument("action", choices=["create", "list", "delete"])
    if args.action == "create":
        s.add_argument("--title", required=True)
        s.add_argument("--start", required=True)
        s.add_argument("--end", required=True)
        s.add_argument("--location", default="")
    elif args.action == "delete":
        s.add_argument("--id", required=True)
    return args


def _parse_signup(args):
    p = PARSER.add_subparsers(dest="command")
    s = p.add_parser("signup", help="Volunteer sign-up")
    s.add_argument("action", choices=["create", "list", "delete"])
    if args.action == "create":
        s.add_argument("--name", required=True)
        s.add_argument("--email", required=True)
        s.add_argument("--phone", default="")
        s.add_argument("--skills", default="")
    elif args.action == "delete":
        s.add_argument("--id", required=True)
    return args


def _parse_hours(args):
    p = PARSER.add_subparsers(dest="command")
    s = p.add_parser("hours", help="Log volunteer hours")
    s.add_argument("action", choices=["create", "list", "delete"])
    if args.action == "create":
        s.add_argument("--volunteer", required=True)
        s.add_argument("--date", required=True)
        s.add_argument("--hours", type=float, required=True)
    elif args.action == "delete":
        s.add_argument("--id", required=True)
    return args


def _parse_note(args):
    p = PARSER.add_subparsers(dest="command")
    s = p.add_parser("note", help="Thank-you notes")
    s.add_argument("action", choices=["create", "list", "delete"])
    if args.action == "create":
        s.add_argument("--volunteer", required=True)
        s.add_argument("--message", required=True)
    elif args.action == "delete":
        s.add_argument("--id", required=True)
    return args


PARSER.add_subparsers(dest="command").add_parser("status", help="Show dashboard status")


def main():
    args = PARSER.parse_args()
    print(f"Command: {args.command or 'help'}")
    print(f"Database: {args.db}")
    print(f"Output: {args.format}")
    return args


if __name__ == "__main__":
    main()
