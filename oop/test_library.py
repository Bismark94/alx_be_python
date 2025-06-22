# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_book = EBook("Snow Crash", "Neal Stephenson", 1.5)
    paper_book   = PrintBook("The Catcher in the Rye", "J.D. Salinger", 224)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_book)
    my_library.add_book(paper_book)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
