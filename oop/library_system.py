 # library_system.py

class Book:
    def __init__(self, title: str, author: str):
        self.title  = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"


class Ebook(Book):
    def __init__(self, title: str, author: str, file_size: float):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, File size: {self.file_size}MB"

    def __repr__(self):
        return f"Ebook({self.title!r}, {self.author!r}, {self.file_size})"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook({self.title!r}, {self.author!r}, {self.page_count})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
