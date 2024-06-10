import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe", "john@example.com")
        self.assertEqual(author.name, "John Doe")
        self.assertEqual(author.email, "john@example.com")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology", "Weekly")
        self.assertEqual(magazine.title, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertEqual(magazine.frequency, "Weekly")

if __name__ == "__main__":
    unittest.main()

