# tests/test_article_extended.py
# tests/test_article_extended.py
import unittest
from models.article import Article

class TestArticleExtended(unittest.TestCase):
    def test_article_long_content(self):
        content = "This is a test content that is very long to test the summarization feature of the Article class." * 10
        article = Article(2, "Long Content Title", content, 2, 2)
        self.assertEqual(article.summarize(), content[:100] + "...")

    def test_article_author_id(self):
        article = Article(3, "Another Test Title", "Some content", 2, 3)
        self.assertEqual(article.author_id, 2)

if __name__ == "__main__":
    unittest.main()
