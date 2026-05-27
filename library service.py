# Library Service Logic
from book import Book
from member import Member
from loan import Loan
from exceptions import *


class LibraryService:
    def __init__(self):
        self.books = {}       # Stores books: {book_id : Book Object}
        self.members = {}     # Stores members: {member_id : Member Object}
        self.loans = {}       # Stores loans: {loan_id : Loan Object}
        self.next_loan_id = 1 # Auto increment loan ID

    # 1. Add New Book
    def add_book(self):
        print("\n--- ADD NEW BOOK ---")
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")

        new_book = Book(book_id, title, author)
        self.books[book_id] = new_book
        print(f"Success: Book added -> {title}")

    # 2. Register New Member
    def register_member(self):
        print("\n--- REGISTER NEW MEMBER ---")
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        email = input("Enter Member Email: ")

        new_member = Member(member_id, name, email)
        self.members[member_id] = new_member
        print(f"Success: Member registered -> {name}")

    # 3. Borrow Book
    def borrow_book(self):
        print("\n--- BORROW BOOK ---")
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        try:
            # Check if book exists
            if book_id not in self.books:
                raise BookNotFoundError

            # Check if member exists
            if member_id not in self.members:
                raise MemberNotFoundError

            selected_book = self.books[book_id]
            selected_member = self.members[member_id]

            # Check availability
            if not selected_book.available:
                raise BookAlreadyBorrowedError

            # Process loan
            new_loan = Loan(self.next_loan_id, selected_book, selected_member)
            self.loans[self.next_loan_id] = new_loan
            self.next_loan_id += 1
            selected_book.available = False  # Mark as borrowed

            print(f"Success: {selected_member.name} borrowed '{selected_book.title}'")

        except (BookNotFoundError, MemberNotFoundError, BookAlreadyBorrowedError) as e:
            print(e)

    # 5. View All Books
    def view_books(self):
        print("\n--- LIBRARY BOOKS ---")
        if not self.books:
            print("No books found in the library.")
            return

        print("List of Books:")
        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"
            print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | Status: {status}")

    # 6. View All Members
    def view_members(self):
        print("\n--- REGISTERED MEMBERS ---")
        if not self.members:
            print("No members registered yet.")
            return

        print("List of Members:")
        for member in self.members.values():
            print(f"ID: {member.member_id} | Name: {member.name} | Email: {member.email}")

    # 7. View All Loans
    def view_loans(self):
        print("\n--- LOAN RECORDS ---")
        if not self.loans:
            print("No loan records found.")
            return

        print("List of Loans:")
        for loan in self.loans.values():
            status = "Active" if loan.is_active else "Returned"
            print(f"Loan ID: {loan.loan_id} | Book: {loan.book.title} | Borrower: {loan.member.name} | Date: {loan.issue_date} | Status: {status}")
