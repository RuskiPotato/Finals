class Author:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

class Book:
    def __init__(self, title, author: Author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"{self.title} by {self.author.name} - {self.author.bio}"