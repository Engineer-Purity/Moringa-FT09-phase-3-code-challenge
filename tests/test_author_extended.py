# tests/test_author_extended.py
# tests/test_author_extended.py
import unittest
from models.author import Author

class TestAuthorExtended(unittest.TestCase):
    def test_author_with_middle_name(self):
        author = Author(2, "Jane Mary Doe", "jane@example.com")
        self.assertEqual(author.name, "Jane Mary Doe")

    def test_author_email_change(self):
        author = Author(3, "John Smith", "john.smith@example.com")
        author.email = "john.new@example.com"
        self.assertEqual(author.email, "john.new@example.com")

if __name__ == "__main__":
    unittest.main()
