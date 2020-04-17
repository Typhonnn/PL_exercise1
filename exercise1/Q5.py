import unittest
import logging

"""Author :Tal Balelty - 312270291"""
logging.basicConfig(filename="Q5Debug.log", level=logging.DEBUG,
                    format="%(asctime)s:%(lineno)d:%(levelname)s:%(message)s",
                    filemode="w")

"""This module implements a toy library of books. Clients can add, checkout and return books
to the library. Clients can also iterate over all the available books.
The library can contain multiple copies of the same book. The library identifies a book by its title and author.
It keeps a list of all the library owned books, and also knows how many of them are available to check out at any time.

The required classes and tests are provided
Please implement the methods that are only implemented with the "raise NotImplementedError" statement """


# EXERCISE NOTE - this class is complete, there's no need to add code to it  except loggers to file
class Book:
    """This class represents a book
    Attributes:
        title (string)
        author (string)
        genre (string)
        n_pages(int)
    """

    def __init__(self, title, author, genre, n_pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.n_pages = n_pages
        logging.debug("Book created: {} {}".format(self.title, self.author, self.genre, self.n_pages))

    def __repr__(self):
        return "Book(%s)" % self.__dict__

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other


class BookKey:
    """This class represents the main way the library identifies a book - its title and author"""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        logging.debug("BookKey created: {} {}".format(self.title, self.author))

    @classmethod
    def from_book(cls, book):
        """A factory method that constructs a key from a book"""
        return cls(book.title, book.author)

    def __eq__(self, other):
        if isinstance(other, BookKey):
            return (self.title, self.author) == (other.title, other.author)

    def __ne__(self, other):
        if isinstance(other, BookKey):
            return (self.title, self.author) != (other.title, other.author)

    def __hash__(self):
        h = hash((self.title, self.author))
        logging.debug("BookKey Hash created: {}".format(h))
        return h


class LibraryBook:
    """This class implements a book within the library.

    Book copies that are checked out are included in qty but not in available qty
    Attributes:
        book (Book): The book in the library
        qty (int): The number of copies of this book in the library
        available_qty (int): The number of copies available in the library.
    """

    def __init__(self, book, qty, available_qty):
        self.book = book
        self.qty = qty
        self.available_qty = available_qty
        logging.debug("LibraryBook created: {} {} {}".format(self.book, self.qty, self.available_qty))

    def __repr__(self):
        return "LibraryBook(%s)" % self.__dict__

    def inc(self):
        """Add another copy to an existing LibraryBook"""
        self.qty += 1
        self.available_qty += 1


class LibraryBookIter:
    """Iterator class for the library
    It iterates over the available books, skipping over books whose copies were all checked out"""

    def __init__(self, library):
        self.iter = iter(library.library_books)

    def __next__(self):
        current = next(self.iter)
        while current.available_qty == 0:
            current = next(self.iter)
        return current


class Library:
    """A library of books that can have multiple copies for the same book

    Attributes:
        library_books (list of LibraryBook): The list of library books
        index (dict of (title, author) to LibraryBook): An index to speed up lookups by (title, author)
    """

    def __init__(self):
        self.library_books = []
        self.index = {}
        logging.debug("Library created: {} {}".format(self.library_books, self.index))

    def add_book(self, book):
        """Adds a book to the library
        Note that this should wrap the Book in a LibraryBook"""
        library_book = self.get_book(book.title, book.author)
        if library_book is None:
            library_book = LibraryBook(book, 1, 1)
            self.library_books.append(library_book)
            self.index[BookKey(book.title, book.author).__hash__()] = library_book
            logging.debug("add_book NEW BOOK: {}\n{}".format(self.library_books, self.index))
        else:
            self.index[BookKey(book.title, book.author).__hash__()].inc()
            logging.debug("add_book INCREASE: {}\n{}".format(self.library_books, self.index))

    def get_book(self, title, author):
        """Returns a LibraryBook given a title and author"""
        # Note that this should use the index to get O(1) average case behavior
        library_book = self.index.get(BookKey(title, author).__hash__())
        logging.debug("get_book: {}".format(library_book))
        if library_book is None:
            return None
        else:
            return library_book

    def checkout(self, title, author):
        """checks out a book from the library

        Returns:
            Book:    If the book is found and has copies available, return the book.
                        Otherwise returns Null
        If the book has no availability or does not exists, returns None"""
        library_book = self.get_book(title, author)
        logging.debug("checkout: {}".format(library_book))
        if library_book is None:
            return None
        elif library_book.available_qty > 0:
            library_book.available_qty -= 1
            return library_book.book
        else:
            return None

    def return_book(self, book):
        """Return a book to the library."""
        library_book = self.get_book(book.title, book.author)
        logging.debug("return_book: {}".format(library_book))
        if library_book is None:
            return None
        else:
            library_book.available_qty += 1

    def __iter__(self):
        """An iterator that iterates over the books available to check out"""
        return LibraryBookIter(self)


class TestLibrary(unittest.TestCase):
    test_books = [
        Book("LOTR", "Tolkien", "Fantasy", 1000),
        Book("Lord of Light", "Roger Zelazny", "Fantasy", 400),
        Book("Sherlock", "Conan-Doyle", "Crime", 200),
        Book("Olilver Twist", "Dickens", "Fiction", 800),
    ]

    def test_book(self):
        b = Book("LOTR", "Tolkien", "Fantasy", 1000)
        self.assertEqual(b.title, "LOTR")
        self.assertEqual(b.author, "Tolkien")
        self.assertEqual(b.n_pages, 1000)
        self.assertEqual(b.genre, "Fantasy")
        self.assertEqual(TestLibrary.test_books[0], b)

    def test_add_books(self):
        lib = Library()
        b = TestLibrary.test_books[0]
        lib.add_book(b)
        library_book = lib.get_book(b.title, b.author)
        self.assertTrue(library_book is not None)
        self.assertEqual(library_book.qty, 1)
        self.assertEqual(library_book.available_qty, 1)
        lib.add_book(b)
        library_book = lib.get_book(b.title, b.author)
        self.assertTrue(library_book is not None)
        self.assertEqual(library_book.qty, 2)
        self.assertEqual(library_book.available_qty, 2)

    def test_checkout(self):
        lib = Library()
        b = TestLibrary.test_books[0]
        lib.add_book(b)
        checked_out = lib.checkout(b.title, b.author)
        self.assertTrue(isinstance(checked_out, Book))
        failed_checkout = lib.checkout(b.title, b.author)
        self.assertEqual(failed_checkout, None)
        lib.return_book(checked_out)
        checked_out = lib.checkout(b.title, b.author)
        self.assertTrue(isinstance(checked_out, Book))
        self.assertTrue(isinstance(checked_out, Book))

    def test_library_iter(self):
        """This test is not valid for the requirements of the exercise. When a NEW book already EXISTS in the
        library, I go to the existing LibraryBook and call inc() to increase the new book count by one. The original
        test assumed I make duplicate LibraryBook's for the same book in the library_books list."""
        lib = Library()
        for book in TestLibrary.test_books:
            lib.add_book(book)
        self.assertEqual(len(list(lib)), 4)
        for book in TestLibrary.test_books:
            lib.add_book(book)
        self.assertEqual(len(list(lib)), 4)
        test_titles_dup = [book.title for book in TestLibrary.test_books]
        iter_titles = [lb.book.title for lb in lib]
        self.assertEqual(iter_titles, test_titles_dup)

    def test_library_iter_skip_unavailable(self):
        lib = Library()
        for book in TestLibrary.test_books:
            lib.add_book(book)
        book = TestLibrary.test_books[0]
        lib.checkout(book.title, book.author)
        self.assertEqual(len(list(lib)), 3)


if __name__ == "__main__":
    unittest.main()
