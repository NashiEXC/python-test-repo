class Book:
# class attribute
    total_books = 0

    def __init__(self, title, author):
# instance attribute
        self.title = title
        self.author = author
        Book.total_books += 1
# book is the instance name
book = Book("1984", "George Orwell")
book2 = Book("Animal Farm", "George Orwell")
# Book is the class name
print(f"Title: {book.title}, Author: {book.author}")
print(f"Total books {Book.total_books}")