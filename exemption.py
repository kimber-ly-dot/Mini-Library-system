# Custom Exceptions
class BookNotFoundError(Exception):
    def __str__(self):
        return "Error: Book not found in the library!"


class MemberNotFoundError(Exception):
    def __str__(self):
        return "Error: Member is not registered!"


class BookAlreadyBorrowedError(Exception):
    def __str__(self):
        return "Error: This book is already borrowed!"
