import json
import os

DATA_FILE = "books.json"


def load_books():
    """Load books from JSON file."""
    try:
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except json.JSONDecodeError:
        print("Error: books.json contains invalid data.")
        return []

    except OSError as error:
        print(f"Error reading book data: {error}")
        return []


def save_books(books):
    """Save books to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(books, file, indent=4)

        return True

    except OSError as error:
        print(f"Error saving book data: {error}")
        return False


def add_book():
    """Add a new book to the library."""
    books = load_books()

    print("\n========== ADD BOOK ==========")

    book_id = input("Enter Book ID: ").strip()

    if not book_id:
        print("Error: Book ID cannot be empty.")
        return

    # Check duplicate ID
    for book in books:
        if book["id"].lower() == book_id.lower():
            print("Error: A book with this ID already exists.")
            return

    title = input("Enter Book Title: ").strip()

    if not title:
        print("Error: Book title cannot be empty.")
        return

    author = input("Enter Author Name: ").strip()

    if not author:
        print("Error: Author name cannot be empty.")
        return

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(new_book)

    if save_books(books):
        print("\nBook added successfully!")


def search_book():
    """Search for a book using ID or title."""
    books = load_books()

    print("\n========== SEARCH BOOK ==========")

    keyword = input("Enter Book ID or Title: ").strip().lower()

    if not keyword:
        print("Error: Search value cannot be empty.")
        return

    found = False

    for book in books:
        if (
            keyword in book["id"].lower()
            or keyword in book["title"].lower()
        ):
            print("\nBook Found")
            print(f"Book ID : {book['id']}")
            print(f"Title   : {book['title']}")
            print(f"Author  : {book['author']}")
            print(f"Status  : {book['status']}")
            found = True

    if not found:
        print("No matching book found.")


def issue_book():
    """Issue an available book."""
    books = load_books()

    print("\n========== ISSUE BOOK ==========")

    book_id = input("Enter Book ID: ").strip()

    if not book_id:
        print("Error: Book ID cannot be empty.")
        return

    for book in books:
        if book["id"].lower() == book_id.lower():

            if book["status"] == "Issued":
                print("Error: This book is already issued.")
                return

            book["status"] = "Issued"

            if save_books(books):
                print(f"Book '{book['title']}' issued successfully.")

            return

    print("Error: Book ID not found.")


def return_book():
    """Return an issued book."""
    books = load_books()

    print("\n========== RETURN BOOK ==========")

    book_id = input("Enter Book ID: ").strip()

    if not book_id:
        print("Error: Book ID cannot be empty.")
        return

    for book in books:
        if book["id"].lower() == book_id.lower():

            if book["status"] == "Available":
                print("Error: This book is already available.")
                return

            book["status"] = "Available"

            if save_books(books):
                print(f"Book '{book['title']}' returned successfully.")

            return

    print("Error: Book ID not found.")


def display_books():
    """Display all books."""
    books = load_books()

    print("\n========== ALL BOOKS ==========")

    if not books:
        print("No books are currently available in the library.")
        return

    print("-" * 70)
    print(f"{'ID':<10}{'TITLE':<25}{'AUTHOR':<20}{'STATUS':<12}")
    print("-" * 70)

    for book in books:
        print(
            f"{book['id']:<10}"
            f"{book['title'][:23]:<25}"
            f"{book['author'][:18]:<20}"
            f"{book['status']:<12}"
        )

    print("-" * 70)