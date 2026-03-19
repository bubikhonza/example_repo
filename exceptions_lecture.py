#
# while True:
#     try:
#         user_input_num1 = int(input("Zadej cislo = delenec \n"))
#         user_input_num2 = int(input("Zadej cislo = delitel \n"))
#
#         result = user_input_num1 / user_input_num2
#
#         print(result)
#     except ZeroDivisionError as e:
#         print(f"Pozor nemuzes delit 0 {e}")
#     except ValueError as e:
#         print(f"Zadane cislo neni platne!! {e}")
#     except Exception as e:
#         print(f"Neco necekaneho se stalo, {e}")

class BookNotFoundError(Exception):
    pass

class Book:
    def __init__(self, id: int):
        self.id = id

class Library:
    def __init__(self, books: list):
        self.books = books

    def find_book(self, id: int):
        for book in self.books:
            if book.id == id:
                return book
        raise BookNotFoundError()

book1 = Book(1)
book2 = Book(2)
book3 = Book(3)
library = Library([book1, book2, book3])
found_book = library.find_book(4)

try:
    found_book = library.find_book(4)
except BookNotFoundError:
    print("Book not found")
