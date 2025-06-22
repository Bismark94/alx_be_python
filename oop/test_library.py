    class Book:
    def __init__(self, title: str, author: str):
        """
        Initialize a Book with title and author.
        """
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"

    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.author!r})"


class Ebook(Book):
    def __init__(self, title: str, author: str, file_size: float):
        """
        Initialize an Ebook with title, author, and file_size (in MB).
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"Ebook: {self.title} by {self.author}, File size: {self.file_size}MB"

    def __repr__(self) -> str:
        return f"Ebook({self.title!r}, {self.author!r}, {self.file_size})"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a PrintBook with title, author, and page_count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self) -> str:
        return f"PrintBook({self.title!r}, {self.author!r}, {self.page_count})"


class Library:
    def __init__(self):
        """
        Initialize the Library with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book) -> None:
        """
        Add a Book/Ebook/PrintBook instance to the library.
        """
        self.books.append(book)

    def list_books(self) -> None:
        """
        Print details of each book in the library.
        """
        for book in self.books:
            print(book)

