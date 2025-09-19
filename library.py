"""
TASK: Create a Library class.

Requirements:
1. The class should track available books (list).
2. Provide a method to add new books to the library.
3. Provide a method for users to borrow books.
   - Remove the borrowed book from available list.
   - Store borrowed books with user info.
4. Provide a method for returning borrowed books.
5. Provide a method to show all available books.

Example Usage:
    lib = Library()
    lib.add_book("Python 101")
    lib.add_book("Data Science Handbook")
    lib.borrow_book("Alice", "Python 101")
    print(lib.show_available_books())  # ["Data Science Handbook"]
    lib.return_book("Alice")
    print(lib.show_available_books())  # ["Data Science Handbook", "Python 101"]
"""

class Library:
    def __init__(self):
       self.available_books = []
       self.borrowed_books = {}

    def add_book(self, book):
        if book not in self.available_books:
            self.available_books.append(book)

    def borrow_book(self, name, book):
        if book in self.available_books:
            if name in self.borrowed_books:
                if not isinstance(self.borrowed_books[name], list):
                    self.borrowed_books[name] = [self.borrowed_books[name]]
                self.borrowed_books[name].append(book)
            else:
                self.borrowed_books.update({name: book})

            self.available_books.remove(book)
        else:
            print("Book is not available")

    def return_book(self, name, book = None):
        if name not in self.borrowed_books:
            print(f"{name} not in possession of any book")
            return
        
        if book == None:
            if isinstance(self.borrowed_books[name], list):
                for book in self.borrowed_books[name]:
                    self.add_book(book)
            else:
                self.add_book(self.borrowed_books[name])
            self.borrowed_books.pop(name)
            return
            
        if book in self.borrowed_books[name]:
            if isinstance(self.borrowed_books[name], list):
                self.add_book(book)
                self.borrowed_books[name].remove(book)
                if not self.borrowed_books[name]:
                    self.borrowed_books.pop(name)
            else:
                self.add_book(self.borrowed_books[name])
                self.borrowed_books.pop(name)
        else:      
             print(f"Book not in {name}'s posession")

    def show_available_books(self):
        return self.available_books
            
lib = Library()
lib.add_book("Python 101")
lib.add_book("Data Science Handbook")
lib.borrow_book("Alice", "Python 101")
lib.borrow_book("Alice", "Data Science Handbook")

print(lib.show_available_books()) 
lib.return_book("Alice")
print(lib.show_available_books())  
