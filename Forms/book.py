class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def __repr__(self):
        return f'Книга "{self.title}" - {self.author}'
