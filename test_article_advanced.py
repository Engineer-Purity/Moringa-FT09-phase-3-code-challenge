# tests/test_article_advanced.py
import unittest
from models.article import Article

class TestArticleAdvanced(unittest.TestCase):
    def test_article_summary_length(self):
        content = "This content is specifically long enough to test whether the summarization function correctly limits the length of the summary." * 2
        article = Article(1, "Long Content Article", content, 1, 1)
        self.assertTrue(len(article.summarize()) <= 103)  # 100 characters + '...'

    def test_article_empty_content(self):
        with self.assertRaises(ValueError):
            Article(2, "Empty Content Article", "", 1, 1)

if __name__ == "__main__":
    unittest.main()
