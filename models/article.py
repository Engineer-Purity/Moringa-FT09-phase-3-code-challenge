# models/article.py
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if id <= 0:
            raise ValueError("ID must be a positive integer.")
        if not content:
            raise ValueError("Content cannot be empty.")
        
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def summarize(self):
        return self.content[:100] + '...'

