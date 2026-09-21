# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: VolunteerDesk
import unittest

from volunteer_desk.shift import Shift
from volunteer_desk.sign_up import SignUp
from volunteer_desk.hours import HoursLog
from volunteer_desk.note import ThankYouNote

class TestHelpers(unittest.TestCase):

    def test_shift_creation(self):
        s = Shift("Monday", "9:00-12:00", "Front Desk")
        self.assertEqual(s.title, "Monday")
        self.assertEqual(s.time_range, "9:00-12:00")

    def test_shift_validation(self):
        s = Shift("Monday", "9:00-12:00")
        self.assertEqual(s.is_valid(), True)
        s_bad = Shift("", "9:00-12:00")
        self.assertEqual(s_bad.is_valid(), False)

    def test_sign_up_creation(self):
        su = SignUp("Alice", "alice@example.com", "Monday", "9:00-12:00")
        self.assertEqual(su.volunteer, "Alice")
        self.assertEqual(su.email, "alice@example.com")

    def test_hours_log_creation(self):
        hl = HoursLog("Monday", "9:00-12:00", 3.0)
        self.assertEqual(hl.date, "Monday")
        self.assertEqual(hl.hours, 3.0)

    def test_thank_you_note_creation(self):
        note = ThankYouNote("Alice", "30.5")
        self.assertEqual(note.name, "Alice")
        self.assertEqual(note.hours, "30.5")

    def test_note_validation(self):
        note = ThankYouNote("Alice", "30.5")
        self.assertEqual(note.is_valid(), True)
        note_bad = ThankYouNote("", "abc")
        self.assertEqual(note_bad.is_valid(), False)

if __name__ == "__main__":
    unittest.main()
