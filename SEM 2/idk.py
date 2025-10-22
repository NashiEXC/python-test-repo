class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author

book= Book("1984", "George Orwell")

book.total_books += 1