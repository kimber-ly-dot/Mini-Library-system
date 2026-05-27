# Main Program
from library_service import LibraryService


def main():
    library = LibraryService()

    while True:
        print("\n===== MINI LIBRARY SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("5. View All Books")
        print("6. View All Members")
        print("7. View Loan Records")
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
