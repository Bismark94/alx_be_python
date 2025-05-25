#bank_account.py

class BankAccount:
    """
    A simple BankAccount class to demonstrate basic OOP concepts.
    """

    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional starting balance.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount if sufficient funds exist.
        Returns True if withdrawal succeeds, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
