# Library Management System in Python

class Book:
    """
    Represents a book with a title, author, and availability status.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        """Marks the book as borrowed if available."""
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        """Marks the book as available again."""
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    """
    Represents a library that holds a collection of books.
    """
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Adds a new book to the library collection."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title: str):
        """Removes a book from the library based on its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def search_book(self, title: str):
        """Searches for a book by title and returns it if found."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        """Displays all books in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            print("Library Collection:")
            for book in self.books:
                print(book)


# Main Function to Demonstrate Library Management System
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(title, author))
        
        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        
        elif choice == "3":
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                print("Book found:", book)
            else:
                print("Book not found.")
        
        elif choice == "4":
            library.display_books()
        
        elif choice == "5":
            title = input("Enter book title to borrow: ")
            book = library.search_book(title)
            if book and book.borrow():
                print(f"You have borrowed '{book.title}'.")
            else:
                print("Book is either not available or does not exist.")
        
        elif choice == "6":
            title = input("Enter book title to return: ")
            book = library.search_book(title)
            if book:
                book.return_book()
                print(f"You have returned '{book.title}'.")
            else:
                print("Book not found in the library.")
        
        elif choice == "7":
            print("Exiting the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")


# Run the program
if __name__ == "__main__":
    main()
