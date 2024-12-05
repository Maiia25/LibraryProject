from Library import Library
from tkinter import *

from User import User

library = Library(name="Бібліотека", address="Київ", country="Україна", email="library@gmail.com")
library.register_book(title="Гарі Потер", author="Роулінг", year_published=2010, genre="фентезі")
library.register_book(title="Книга1", author="Автор1", year_published=2022, genre="історія")
library.register_book(title="Книга2", author="Автор2", year_published=2022, genre="фентезі")
library.register_book(title="Книга1", author="Автор2", year_published=2015, genre="історія")


def check_book_exists(name_book):
    booklist = library.findbook(name_book.get()) # назва, яку ввів користувач
    if len(booklist) != 0:
        return True, booklist
    else:
        return False,booklist

def create_book_list(screen,booklist):
    listbox = Listbox(bg="white", font=('Arial', 30), height=5)
    listbox.pack()
    for book in booklist:
        listbox.insert(END, book.information())
    # User login and take a book
    def takebook(): #обрати книгу з наявних
        selected_list = listbox.curselection()
        if len(selected_list) != 0:
            cur_num = selected_list[0]
            current_book = booklist[cur_num]
            library.register_user("John","124343254","john@gmail.com",1980)
            library.reserve("John","124343254",current_book)
            library.history_journal("John","124343254")
            listbox.destroy()
            btn4.destroy()
    btn4 = Button(screen, text="Обрати книгу", bg="blue", activebackground="green", fg="white",
                  activeforeground="red", font=("Courier", 30),
                  relief=FLAT, overrelief=GROOVE,command=takebook)
    btn4.pack()