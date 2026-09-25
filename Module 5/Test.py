class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"Confirmation: '{self.title}' has been successfully borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(f"Confirmation: '{self.title}' has been returnrd successfully.")

book1 = Book("Powerless","Lauren Roberts")
book2 = Book("Caraval","Stephanie Garber")
book3 = Book("The Inheritance Games", "Jennifer Lynn Barnes")

print("...")
book1.borrow()
book2.borrow()
book1.return_book()
book3.borrow()