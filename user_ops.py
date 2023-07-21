from utils import create_user_file


class UserManagement:
    def __init__(self, first_name, last_name, email, current_balance=100):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.current_balance = current_balance
        self.bank_account = ""
        self.card_number = ""
        self.bank_account_initial_no = "145"
        self.bank_branch = "001"
        self.card_reference = "999"

    def create_account(self):
        self.bank_account = self.create_bank_account()
        self.card_number = self.create_card_number()
        user_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "bank_account": self.bank_account,
            "card_number": self.card_number,
            "current_balance": self.current_balance,
        }

        create_user_file(f"{self.card_number}.txt", user_data)

    def create_bank_account(self):
        bank_account_no = f"{self.bank_account_initial_no}{self.bank_branch}001"
        return bank_account_no

    def create_card_number(self):
        card_no = f"{self.bank_account_initial_no}{self.bank_branch}{self.card_reference}001"
        return card_no