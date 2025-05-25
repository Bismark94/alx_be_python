# shopping_list_manager.py

def display_menu():
    """
    Displays the menu options to the user.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function that continuously shows the menu,
    processes user input, and manages the shopping list.
    """
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)
            print(f"'{item_to_add}' has been added to the shopping list.\n")

        elif choice == '2':
            # Remove an item
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the shopping list.\n")
            else:
                print(f"'{item_to_remove}' is not in the shopping list.\n")

        elif choice == '3':
            # View the current shopping list
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                print()
            else:
                print("Your shopping list is currently empty.\n")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
