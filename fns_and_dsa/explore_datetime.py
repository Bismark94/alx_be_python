# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Fetches the current date and time, stores in current_date variable,
    and prints it in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    # Format example: 2024-03-25 15:30:45
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    """
    Prompts the user for a number of days (integer),
    calculates the future date from the current date,
    stores in future_date variable, and prints it in 'YYYY-MM-DD' format.
    """
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Format example: 2024-04-04
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
