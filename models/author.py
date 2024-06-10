# models/author.py
class Author:
    def __init__(self, id, name, email):
        if not name:
            raise ValueError("Name cannot be empty.")
        if "@" not in email:
            raise ValueError("Invalid email format.")
        
        self.id = id
        self.name = name
        self.email = email

    def get_contact_info(self):
        return f"{self.name} <{self.email}>"

