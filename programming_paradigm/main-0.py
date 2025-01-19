# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Create a bank account with a custom initial balance (for example, $100).
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Example argument might be "deposit:50" or "withdraw:20" or "display"
    parts = sys.argv[1].split(':')
    command = parts[0]  # e.g., "deposit", "withdraw", or "display"
    amount = float(parts[1]) if len(parts) > 1 else None  # e.g., 50.0

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
