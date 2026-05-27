# Loan Class
from datetime import datetime

class Loan:
    def __init__(self, loan_id: int, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.issue_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.is_active = True  # Default status: Active Loan
