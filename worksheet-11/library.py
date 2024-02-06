"""
Write a program, library.py, to manage a library system that includes both physical and digital books.
Every book, regardless of its type, has a title, author, and an International Standard Book Number (ISBN). 
Books also have an attribute to indicate whether they are currently available for borrowing.
A digital book has an extra attribute: compatibility, which could be PDF, Kindle or Apple. 

Initially, a digital book is compatible with only one specified format, 
but the user should be able to add additional compatibilities. Digital books are always available for borrowing.
Your program needs to include a Library class that stores a collection of books. 
The user should be able to add a book to a library (making it available) but they could only borrow a book if it is available.
When displaying a library, the titles, and availability statuses of all the books should be shown.

Test your classes, with the following books, using a test function:
Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
Book("1984", "George Orwell", "978-0451524935")
DigitalBook("1984", "George Orwell", "978-0451524935", "Kindle")
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"


class DigitalBook(Book):
    def __init__(self, title, author, isbn, compatibility):
        super().__init__(title, author, isbn)
        self.compatibility = [compatibility]

    def addCompatibility(self, new_compatibility):
        self.compatibility.append(new_compatibility)

    def __str__(self):
        compatibilities = ", ".join(self.compatibility)
        return f"{super().__str__()} - Compatible Formats: {compatibilities}"


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def displayLibrary(self):
        for book in self.books:
            print(book)


def testLibrary():
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    digitalBook = DigitalBook("1984", "George Orwell", "978-0451524935", "Kindle")

    library.addBook(book1)
    library.addBook(book2)
    library.addBook(digitalBook)

    print("Library Contents:")
    library.displayLibrary()


if __name__ == "__main__":
    testLibrary()
