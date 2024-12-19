from Library import *
from tkinter import *
library = Library(name="Бібліотека", address="Київ", country="Україна", email="library@gmail.com")
library.register_book(title="Гарі Потер", author="Роулінг", year_published=2010, genre="фентезі")
library.register_book(title="Книга1", author="Автор1", year_published=2022, genre="історія")
library.register_book(title="Книга2", author="Автор2", year_published=2022, genre="фентезі")
library.register_book(title="Книга1", author="Автор2", year_published=2015, genre="історія")
library.register_user(name="Іван Читун", telephone="4338066", email="test@mail.com", year=1991)
library.reserve(name="Іван Читун", telephone="4338066", book=library.findbook("Книга2")[0])
def return_userbook(screen, user_book, user_name, user_phone):
    result=library.return_book(name=user_name.get(), telephone=user_phone.get(), title=user_book.get())
    if result==True:
        label=Label(screen, text="Книгу повернено", font=("Courier", 24))
        label.pack()
    else:
        label = Label(screen, text="Книгу  не повернено", font=("Courier", 24))
        label.pack()