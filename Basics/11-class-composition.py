class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."
    
class Book:
    def __init__(self, name) -> None:
        self.name = name
        
    def __str__(self) -> str:
        return f"Book {self.name}"
    

book1 = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book1, book2)

print(shelf)