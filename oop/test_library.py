# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # 1) make a library
    my_library = Library()

    # 2) create one of each
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_book = EBook("Snow Crash", "Neal Stephenson", 500)   # 500KB
    paper_book   = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # 3) add them
    my_library.add_book(classic_book)
    my_library.add_book(digital_book)
    my_library.add_book(paper_book)

    # 4) list them out
    my_library.list_books()

if __name__ == "__main__":
    main()
