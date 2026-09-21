# === Stage 50: Add unit tests for import and export behavior ===
# Project: VolunteerDesk
import pytest
from volunteerdesk.core.exporter import export_shifts_csv, export_volunteers_csv

def test_export_shifts_csv(tmp_path):
    shifts = [
        {"id": 1, "title": "Morning Shift", "start": "2024-01-01T09:00", "end": "2024-01-01T17:00", "volunteer_id": 10, "status": "confirmed"},
        {"id": 2, "title": "Afternoon Shift", "start": "2024-01-01T13:00", "end": "2024-01-01T21:00", "volunteer_id": 20, "status": "pending"},
    ]
    out_path = tmp_path / "shifts.csv"
    export_shifts_csv(shifts, str(out_path))
    content = out_path.read_text()
    assert "id,title,start,end,volunteer_id,status" in content
    assert "1,Morning Shift,2024-01-01T09:00,2024-01-01T17:00,10,confirmed" in content

def test_export_volunteers_csv(tmp_path):
    volunteers = [
        {"id": 10, "name": "Alice", "email": "alice@example.com", "phone": "555-0100", "hours": 42, "notes": "Great worker"},
        {"id": 20, "name": "Bob", "email": "bob@example.com", "phone": "555-0200", "hours": 15, "notes": ""},
    ]
    out_path = tmp_path / "volunteers.csv"
    export_volunteers_csv(volunteers, str(out_path))
    content = out_path.read_text()
    assert "id,name,email,phone,hours,notes" in content
    assert "10,Alice,alice@example.com,555-0100,42,Great worker" in content
