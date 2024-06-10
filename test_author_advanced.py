# tests/test_author_advanced.py
import unittest
from models.author import Author

class TestAuthorAdvanced(unittest.TestCase):
    def test_author_full_name(self):
        author = Author(1, "John Doe", "john@example.com")
        self.assertEqual(author.name, "John Doe")
        self.assertEqual(author.email, "john@example.com")

    def test_author_invalid_email(self):
        with self.assertRaises(ValueError):
            Author(2, "Jane Doe", "janeexample.com")

if __name__ == "__main__":
    unittest.main()
