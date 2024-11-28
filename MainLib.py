from Library import * #* підтягує всі функції, інакше вказуємо, що хочемо імпортувати
from Search import *
library = Library(name="BookYe", address="Kyiv", country="Ukraine", email="bookye@gmail.com")
search = Search(library)
print("Welcome to our library. \n1 - Register new user. \n2 - Check list of all books. \n3 - Book search. "
      "\n4 - Add book. \n5 - Rent book. \n6. Return book. \n7. Exit.")
while True:
    user_input = int(input("You are in the main menu. Enter your choice"))
    if user_input == 1:
        name = input("Enter the name")
        telephone = input("Enter a telephone")
        email = input("Enter an email")
        year = input("Enter a year")
        library.register_user(name, telephone, email, year)
    elif user_input == 2:
        library.list_books()
    elif user_input == 3:
       title = input("Enter title")
       author = input("Enter author")
       year_published = input("Enter year_published")
       genre = input("Enter genre")
       if title != "":
           search.search_by_title(title)
       elif author != "":
           search.search_by_author(author)
       elif year_published != "":
           search.search_by_year_published(year_published)
       elif genre != "":
           search.search_by_genre(genre)
       else:
           print("You didn`t enter any parameter.")
    elif user_input == 4:
        quantity = int(input("Enter the quantity of books"))
        while quantity < 1 or quantity > 100:
            print("Enter quantity again")
            quantity = int(input("Enter quantity: "))
        for i in range (quantity):
            title = input("Enter title for new book")
            author = input("Enter author for new book")
            year_published = input("Enter year_published for new book")
            genre = input("Enter genre for new book")
            library.register_book(title, author, year_published, genre)
    elif user_input == 5:
        name = input("Enter your name")
        telephone = input("Enter your telephone")
        title = input("Enter the title of rent book")
        library.reserve(name, telephone, title)
    elif user_input ==6:
        name = input("Enter your name")
        telephone = input("Enter your telephone")
        title = input("Enter the title of return book")
        library.return_book(name, telephone, title)
    elif user_input == 7:
        break
    else:
        print("Enter correct number.")