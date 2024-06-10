# tests/test_magazine_extended.py
# tests/test_magazine_extended.py
import unittest
from models.magazine import Magazine

class TestMagazineExtended(unittest.TestCase):
    def test_magazine_biweekly_frequency(self):
        magazine = Magazine(4, "Biweekly Tech", "Technology", "Biweekly")
        self.assertEqual(magazine.frequency, "Biweekly")

    def test_magazine_change_frequency(self):
        magazine = Magazine(5, "Monthly Science", "Science", "Monthly")
        magazine.frequency = "Weekly"
        self.assertEqual(magazine.frequency, "Weekly")

if __name__ == "__main__":
    unittest.main()

