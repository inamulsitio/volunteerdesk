# === Stage 51: Add unit tests for search and filter behavior ===
# Project: VolunteerDesk
import unittest
from volunteerdesk.models import Volunteer, Shift, ThankYouNote
from volunteerdesk.service import VolunteerDesk

desk = VolunteerDesk()

class TestSearchAndFilter(unittest.TestCase):

    def setUp(self):
        desk.add_volunteer(Volunteer(id=1, name="Alice", role="Coordinator"))
        desk.add_volunteer(Volunteer(id=2, name="Bob", role="Tutor"))
        desk.add_volunteer(Volunteer(id=3, name="Charlie", role="Tutor"))
        desk.add_shift(Shift(id=1, title="Morning Shift", role="Tutor"))
        desk.add_shift(Shift(id=2, title="Afternoon Shift", role="Coordinator"))
        desk.add_thank_you("Alice", "Bob", "Great work on tutoring!")

    def test_search_by_name(self):
        results = desk.search_volunteers("ali")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Alice")

    def test_search_by_role(self):
        results = desk.search_volunteers(role="Tutor")
        self.assertEqual(len(results), 2)

    def test_search_nonexistent(self):
        results = desk.search_volunteers("zzz")
        self.assertEqual(len(results), 0)

    def test_filter_shifts_by_role(self):
        results = desk.filter_shifts(role="Tutor")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Morning Shift")

    def test_filter_shifts_by_title(self):
        results = desk.filter_shifts(title="Morning")
        self.assertEqual(len(results), 1)

    def test_filter_thank_yous_by_volunteer(self):
        results = desk.filter_thank_yous(volunteer="Bob")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].message, "Great work on tutoring!")

    def test_filter_thank_yous_by_recipient(self):
        results = desk.filter_thank_yous(recipient="Bob")
        self.assertEqual(len(results), 1)

if __name__ == "__main__":
    unittest.main()
