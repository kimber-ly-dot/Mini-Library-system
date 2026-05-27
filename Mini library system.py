from datetime import datetime

# ---------------------- CUSTOM EXCEPTIONS ----------------------
class BookNotFoundError(Exception):
    pass

class MemberNotFoundError(Exception):
    pass

class BookAlreadyBorrowedError(Exception):
    pass


# ---------------------- CLASSES ----------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True  # Default: Available


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email


class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.issue_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.is_active = True  # Default: Active Loan


# ---------------------- LIBRARY SERVICE ----------------------
class LibraryService:
    def __init__(self):
        self.books = {}       # Store books: {book_id : Book Object}
        self.members = {}     # Store members: {member_id : Member Object}
        self.loans = {}       # Store loans: {loan_id : Loan Object}
        self.next_loan_id = 1

    # 1. ADD BOOK
    def add_book(self):
        print("\n--- ADD NEW BOOK ---")
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")

        new_book = Book(book_id, title, author)
        self.books[book_id] = new_book
        print(f"Success: Book added -> {title}")

    # 2. REGISTER MEMBER
    def register_member(self):
        print("\n--- REGISTER NEW MEMBER ---")
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        email = input("Enter Member Email: ")

        new_member = Member(member_id, name, email)
        self.members[member_id] = new_member
        print(f"Success: Member registered -> {name}")

    # 3. BORROW BOOK
    def borrow_book(self):
        print("\n--- BORROW BOOK ---")
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        try:
            if book_id not in self.books:
                raise BookNotFoundError

            if member_id not in self.members:
                raise MemberNotFoundError

            selected_book = self.books[book_id]
            selected_member = self.members[member_id]

            if not selected_book.available:
                raise BookAlreadyBorrowedError

            # Process loan
            new_loan = Loan(self.next_loan_id, selected_book, selected_member)
            self.loans[self.next_loan_id] = new_loan
            self.next_loan_id += 1
            selected_book.available = False

            print(f"Success: {selected_member.name} borrowed '{selected_book.title}'")

        except BookNotFoundError:
            print("Error: Book not found.")
        except MemberNotFoundError:
            print("Error: Member not found.")
        except BookAlreadyBorrowedError:
            print("Error: Book is already borrowed.")

    # 5. VIEW BOOKS
    def view_books(self):
        print("\n--- LIBRARY BOOKS ---")
        if not self.books:
            print("No books found in the library.")
            return

        print("List of Books:")
        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"
            print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | Status: {status}")

    # 6. VIEW MEMBERS
    def view_members(self):
        print("\n--- REGISTERED MEMBERS ---")
        if not self.members:
            print("No members registered yet.")
            return

        print("List of Members:")
        for member in self.members.values():
            print(f"ID: {member.member_id} | Name: {member.name} | Email: {member.email}")

    # 7. VIEW LOANS
    def view_loans(self):
        print("\n--- LOAN RECORDS ---")
        if not self.loans:
            print("No loan records found.")
            return

        print("List of Loans:")
        for loan in self.loans.values():
            status = "Active" if loan.is_active else "Returned"
            print(f"Loan ID: {loan.loan_id} | Book: {loan.book.title} | Borrower: {loan.member.name} | Date: {loan.issue_date} | Status: {status}")


# ---------------------- MAIN PROGRAM ----------------------
def main():
    library = LibraryService()

    while True:
        print("\n===== MINI LIBRARY SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Exit")
        print("================================")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.register_member()
        elif choice == "3":
            library.borrow_book()
        elif choice == "5":
            library.view_books()
        elif choice == "6":
            library.view_members()
        elif choice == "7":
            library.view_loans()
        elif choice == "8":
            print("Program closed. Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-8.")


if __name__ == "__main__":
    main()
