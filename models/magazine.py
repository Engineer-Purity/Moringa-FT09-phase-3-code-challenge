# models/magazine.py
class Magazine:
    def __init__(self, id, title, category, frequency):
        if not title:
            raise ValueError("Title cannot be empty.")
        if not category:
            raise ValueError("Category cannot be empty.")
        
        self.id = id
        self.title = title
        self.category = category
        self.frequency = frequency

    def get_magazine_info(self):
        return f"{self.title} ({self.category} - {self.frequency})"

