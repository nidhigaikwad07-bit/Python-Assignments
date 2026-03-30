class Library:
    def __init__(self, book_name, author, available):
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(f"The book '{self.book_name}' has been checked out.")
        else:
            print(f"The book '{self.book_name}' is not available.")

    def return_book(self):
        self.available = True
        print(f"The book '{self.book_name}' has been returned.")

    def display_books(self):
        status = "Available" if self.available else "Not Available"
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)
        print("-----------------------")


# Creating objects
book1 = Library("Python Basics", "Guido van Rossum", True)
book2 = Library("Data Structures", "Mark Allen", False)

# Display books
book1.display_books()
book2.display_books()

# Check out and return operations
book1.check_out()
book1.display_books()

book1.return_book()
book1.display_books()