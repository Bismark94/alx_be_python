class Book:
    def __init__(self, title, author, year):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Return an informal, user-friendly string representation of the Book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Return an official string representation of the Book that can be used to recreate the instance.
        """
        return f"Book({self.title!r}, {self.author!r}, {self.year})"

    def __del__(self):
        """
        Destructor that notifies when the Book instance is being deleted.
        """
        print(f"Deleting {self.title}")
