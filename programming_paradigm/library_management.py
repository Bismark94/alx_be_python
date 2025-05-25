# library_management.py

class Book:
    """
    Represents a single book in the library with a title, author,
    and a private attribute for tracking checkout status.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Mark this book as checked out if it is currently available.
        Returns True if the checkout was successful,
        or False if it was already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Mark this book as returned if it is currently checked out.
        Returns True if the return was successful,
        or False if it was not checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Indicate whether the book is available (not checked out).
        """
        return not self._is_checked_out

class Library:
    """
    Manages a collection of Book objects.
    Allows adding books, checking them out, returning them,
    and listing all available titles.
    """

    def __init__(self):
        self._books = []  # Private list to hold Book instances

    def add_book(self, book):
        """
        Add a new Book instance to the library.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title if available. If found and available,
        it marks the book as checked out.
        """
        for book in self._books:
            if book.title == title:
                # Attempt to check out
                return book.check_out()
        return False  # Book not found or not available

    def return_book(self, title):
        """
        Return a book by its title if it is currently checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found

    def list_available_books(self):
        """
        Print all books that are not checked out,
        in the format: "<title> by <author>".
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
