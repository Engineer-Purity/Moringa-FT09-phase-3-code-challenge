# tests/test_magazine_advanced.py
import unittest
from models.magazine import Magazine

class TestMagazineAdvanced(unittest.TestCase):
    def test_magazine_bimonthly(self):
        magazine = Magazine(1, "Tech Monthly", "Technology", "Monthly")
        self.assertEqual(magazine.frequency, "Monthly")

    def test_magazine_invalid_category(self):
        with self.assertRaises(ValueError):
            Magazine(2, "Random Magazine", "", "Weekly")

if __name__ == "__main__":
    unittest.main()
