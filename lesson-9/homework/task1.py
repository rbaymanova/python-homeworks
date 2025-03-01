class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', borrowed={self.is_borrowed})"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
        else:
            raise BookNotFoundException(f"'{book.title}' is not borrowed by this member.")
    
    def __repr__(self):
        return f"Member(name='{self.name}', borrowed_books={[book.title for book in self.borrowed_books]})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in library.")
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        
        member.borrow_book(book)
    
    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in library.")
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        
        member.return_book(book)
    
    def __repr__(self):
        return f"Library(books={self.books}, members={self.members})"

# Testing the system
library = Library()

# Adding books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Adding members
member1 = Member("Ali")
member2 = Member("Bobur")
library.add_member(member1)
library.add_member(member2)

# Borrowing books
library.borrow_book("Ali", "1984")
library.borrow_book("Bobur", "The Great Gatsby")

# Handling exceptions
try:
    library.borrow_book("Ali", "1984")  # Already borrowed
except Exception as e:
    print(e)

try:
    library.borrow_book("Ali", "Unknown Book")  # Book not found
except Exception as e:
    print(e)

try:
    library.borrow_book("Bobur", "To Kill a Mockingbird")
    library.borrow_book("Bobur", "1984")
    library.borrow_book("Bobur", "The Great Gatsby")  # Exceeds limit
except Exception as e:
    print(e)

# Returning books
library.return_book("Ali", "1984")
