Library Management System 
A comprehensive Python-based library management system with an interactive menu-driven interface. This system allows users to manage books, members, loans, and borrowing operations efficiently.

Features

1. Add Book
- Add new books to the library database
- Each book has a unique ID, title, and author
- Books are marked as available by default
- Follows workflow: Input details → Create record → Store data
- Flowchart:  _01_add_book.svg 
 
2. Register Member
- Register new library members with their personal information
- Each member has a unique ID, full name, and email address
- Data is stored securely for future transactions
- Flowchart:  _02_register_member.svg 
 
3. Borrow Book
- Process book borrowing transactions
- Automatic validation:
✔️ Check if Book ID exists
✔️ Check if Member ID exists
✔️ Check if book is available
- Creates loan record and marks book as borrowed
- Shows clear error messages for invalid actions
- Flowchart:
-  _03_borrow_book.svg 
 
5. View Books 
- Display complete list of all books in the library

- Shows ID, title, author, and current status
- Message shown if library has no books yet
- Flowchart:  _05_view_book.svg 
 
6. View Members
 
- Display all registered members' information
- Shows ID, name, and email address
- Message shown if no members are registered
- Flowchart:  _06_view_member.svg 
 
7. View Loans
- Display all loan records and history
- Shows Loan ID, book title, borrower name, date issued, and status
- Status marked as Active or Closed
- Message shown if no loans exist
- Flowchart:  _07_view_loan.svg 
 
8. Exit
- Safely terminate the program
- Ends execution and returns to system
- Flowchart:  _08_exit.svg 
 
 
📂 Project Structure
Library-Management-System/
├── book.py              # Book class definition
├── member.py            # Member class definition
├── loan.py              # Loan class definition
├── exceptions.py        # Custom error handling
├── library_service.py   # Core system logic
├── main.py              # Main program & menu
└── README.md            # Project documentation
