import library


def display_menu():
    """Display the main menu."""
    print("\n")
    print("=" * 45)
    print("       LIBRARY AUTOMATION TOOL")
    print("=" * 45)
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. Exit")
    print("=" * 45)


def get_choice():
    """Get and validate menu choice."""
    while True:
        choice = input("Enter your choice (1-6): ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice

        print("Invalid choice. Please enter a number from 1 to 6.")


def main():
    """Run the Library Automation Tool."""

    print("\nWelcome to the Library Automation Tool!")

    while True:
        display_menu()
        choice = get_choice()

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.search_book()

        elif choice == "3":
            library.issue_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            print("\nThank you for using the Library Automation Tool!")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()