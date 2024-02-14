#Library Management System
class Library:
  def __init__(self):
    #Opens books.txt and uses it in read/write mode
    self.file = open("books.txt", "a+", encoding="utf-8")
  
  def __del__(self):
    self.file.close()

  def list_books(self):
    self.file.seek(0)
    books = self.file.readlines()
    if not books:
      print("There are no books in the library")
    else:
      for book in books:
        book_info = book.split(",")
        print(f"Book Title: {book_info[0]} Author: {book_info[1]}")

  def add_books(self):
    book_title = input("Enter the book title:")
    book_author = input("Enter the book author:")
    book_release_year = input("Enter the book release:")
    book_num_pages = input("Enter the book pages:")
    book_info = f"{book_title}, {book_author}, {book_release_year}, {book_num_pages}\n"
    self.file.write(book_info)
    print("Book added !")

  def remove_books(self):
    book_title = input("Enter the title of the book you will remove: ")
    self.file.seek(0)
    books = self.file.readlines()
    new_books = [book for book in books if not book.startswith(book_title)]
    self.file.seek(0)
    self.file.truncate()
    self.file.writelines(new_books)
    print("Book removed !")
  
lib = Library()

while True:
  print("*** MENU ***")
  print("1) List Books")
  print("2) Add Book")
  print("3) Remove Book")
  print("q) Quit")

  choice = input("Select the choice: ")
  if choice == "1":
    lib.list_books()
  elif choice == "2":
    lib.add_books()
  elif choice == "3":
    lib.remove_books()
  elif choice == "q":
    print("Exiting the library system...")
    break
  else:
    print("You have selected an invalid transaction. Please choose the correct action..")

