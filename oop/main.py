# main.py

from book_class import Book

def main():
    # 1) construct
    my_book = Book("1984", "George Orwell", 1949)
    # 2) __str__
    print(my_book)
    # 3) __repr__
    print(repr(my_book))
    # 4) __del__
    del my_book

if __name__ == "__main__":
    main()
