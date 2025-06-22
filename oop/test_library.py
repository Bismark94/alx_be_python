from library_system import Book, Ebook, PrintBook, Library


def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    ebook_one     = Ebook("Snow Crash", "Neal Stephenson", 1.5)
    print_book_one= PrintBook("The Catcher in the Rye", "J.D. Salinger", 224)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(ebook_one)
    my_library.add_book(print_book_one)

    # List all books in the library
    my_library.list_books()


if __name__ == "__main__":
    main()
