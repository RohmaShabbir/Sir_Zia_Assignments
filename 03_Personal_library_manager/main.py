import json

class BookCollection:
    """A class to manage a collection of books with persistent storage in a JSON file."""

    def __init__(self):
        """Initialize the book collection and load existing data."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load books from JSON file, creating a new file if none exists."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Save the current book collection to the JSON file."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection with input validation."""
        print("\nAdd a New Book")
        book_title = input("Enter book title: ").strip()
        book_author = input("Enter author: ").strip()

        # Check for existing book
        if any(b for b in self.book_list 
               if b['title'].lower() == book_title.lower() 
               and b['author'].lower() == book_author.lower()):
            print("\n⚠️ A book with this title and author already exists!")
            if input("Add anyway? (yes/no): ").lower() != 'yes':
                print("Book not added.\n")
                input("Press Enter to continue...")
                return

        # Validate publication year
        while True:
            publication_year = input("Enter publication year (YYYY): ").strip()
            if len(publication_year) == 4 and publication_year.isdigit():
                break
            print("Invalid year. Please enter a 4-digit year.")

        book_genre = input("Enter genre: ").strip()
        
        # Validate reading status
        while True:
            is_book_read = input("Have you read this book? (yes/no): ").strip().lower()
            if is_book_read in ('yes', 'no'):
                break
            print("Please answer 'yes' or 'no'.")

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read == "yes",
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("\n✅ Book added successfully!")
        input("Press Enter to continue...")

    def delete_book(self):
        """Remove a book with confirmation and handling of multiple matches."""
        print("\nRemove a Book")
        search_term = input("Enter book title to remove: ").strip().lower()
        matches = [b for b in self.book_list if b['title'].lower() == search_term]

        if not matches:
            print("\n❌ No books found with that title.")
            input("Press Enter to continue...")
            return

        if len(matches) > 1:
            print("\nMultiple matches found:")
            for i, book in enumerate(matches, 1):
                print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
            while True:
                try:
                    choice = int(input("Enter number to delete: "))
                    if 1 <= choice <= len(matches):
                        book_to_delete = matches[choice-1]
                        break
                    print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            book_to_delete = matches[0]

        confirm = input(f"Delete '{book_to_delete['title']}' by {book_to_delete['author']}? (yes/no): ").lower()
        if confirm == "yes":
            self.book_list.remove(book_to_delete)
            self.save_to_file()
            print("\n✅ Book removed successfully!")
        else:
            print("\nDeletion cancelled.")
        input("Press Enter to continue...")

    def find_book(self):
        """Search books with multiple criteria and proper result formatting."""
        print("\nSearch Books")
        print("1. By Title\n2. By Author\n3. By Genre\n4. By Year")
        search_type = input("Choose search type (1-4): ").strip()
        search_term = input("Enter search term: ").strip().lower()

        results = []
        if search_type == "1":
            results = [b for b in self.book_list if search_term in b['title'].lower()]
        elif search_type == "2":
            results = [b for b in self.book_list if search_term in b['author'].lower()]
        elif search_type == "3":
            results = [b for b in self.book_list if search_term in b['genre'].lower()]
        elif search_type == "4":
            results = [b for b in self.book_list if search_term in b['year']]
        else:
            print("Invalid choice. Showing all books.")
            results = self.book_list.copy()

        if results:
            print("\n📖 Search Results:")
            for i, book in enumerate(sorted(results, key=lambda x: x['title'].lower()), 1):
                status = "✔️ Read" if book['read'] else "📖 Unread"
                print(f"{i}. {book['title']} by {book['author']}")
                print(f"   Published: {book['year']} | Genre: {book['genre']} | Status: {status}\n")
        else:
            print("\nNo matching books found.")
        input("Press Enter to continue...")

    def update_book(self):
        """Modify book details with proper input validation and feedback."""
        print("\nUpdate Book Details")
        search_term = input("Enter book title to update: ").strip().lower()
        matches = [b for b in self.book_list if b['title'].lower() == search_term]

        if not matches:
            print("\n❌ No books found with that title.")
            input("Press Enter to continue...")
            return

        book = matches[0] if len(matches) == 1 else self._handle_multiple_matches(matches)
        if not book:
            return

        print("\nLeave fields blank to keep current values.")
        book['title'] = input(f"New title ({book['title']}): ").strip() or book['title']
        book['author'] = input(f"New author ({book['author']}): ").strip() or book['author']
        
        # Year validation
        new_year = input(f"New year ({book['year']}): ").strip()
        if new_year:
            if len(new_year) == 4 and new_year.isdigit():
                book['year'] = new_year
            else:
                print("⚠️ Invalid year format. Keeping existing value.")

        book['genre'] = input(f"New genre ({book['genre']}): ").strip() or book['genre']
        
        # Reading status validation
        current_status = 'yes' if book['read'] else 'no'
        new_status = input(f"Have you read it? (yes/no) [Current: {current_status}]: ").strip().lower()
        if new_status in ('yes', 'no'):
            book['read'] = new_status == 'yes'
        elif new_status:
            print("⚠️ Invalid input. Keeping current status.")

        self.save_to_file()
        print("\n✅ Book updated successfully!")
        input("Press Enter to continue...")

    def _handle_multiple_matches(self, matches):
        """Helper method to handle multiple matches during update."""
        print("\nMultiple matches found:")
        for i, book in enumerate(matches, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
        while True:
            try:
                choice = int(input("Enter number to update: "))
                if 1 <= choice <= len(matches):
                    return matches[choice-1]
                print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

    def show_all_books(self):
        """Display all books with sorting and proper formatting."""
        if not self.book_list:
            print("\nYour collection is empty!\n")
            input("Press Enter to continue...")
            return

        print("\n📚 Your Complete Collection:")
        sorted_books = sorted(self.book_list, key=lambda x: x['title'].lower())
        for i, book in enumerate(sorted_books, 1):
            status = "✔️ Read" if book['read'] else "📖 Unread"
            print(f"{i}. {book['title']} by {book['author']}")
            print(f"   Published: {book['year']} | Genre: {book['genre']} | Status: {status}\n")
        input("Press Enter to continue...")

    def show_reading_progress(self):
        """Display reading statistics with visual feedback."""
        total = len(self.book_list)
        if not total:
            print("\nNo books in collection to track progress!\n")
            input("Press Enter to continue...")
            return

        read = sum(1 for b in self.book_list if b['read'])
        progress = read/total * 100
        print(f"\n📊 Reading Progress:")
        print(f"Total Books: {total}")
        print(f"Books Read: {read} ({progress:.1f}%)")
        print(f"Unread Books: {total - read}")
        input("\nPress Enter to continue...")

    def start_application(self):
        """Main application loop with improved user interface."""
        while True:
            print("\n" + "="*50)
            print("📚 Book Collection Manager".center(50))
            print("="*50)
            print("1. Add New Book")
            print("2. Remove Book")
            print("3. Search Books")
            print("4. Update Book Details")
            print("5. View All Books")
            print("6. View Reading Progress")
            print("7. Exit")
            choice = input("\nEnter your choice (1-7): ").strip()

            actions = {
                "1": self.create_new_book,
                "2": self.delete_book,
                "3": self.find_book,
                "4": self.update_book,
                "5": self.show_all_books,
                "6": self.show_reading_progress,
                "7": lambda: (print("\nThank you for using Book Collection Manager! Goodbye! 👋"), exit())
            }

            if action := actions.get(choice):
                action()
            else:
                print("\n⚠️ Invalid choice. Please enter a number between 1-7.")
                input("Press Enter to continue...")


if __name__ == "__main__":
    BookCollection().start_application()