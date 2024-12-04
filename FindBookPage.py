from tkinter import *

from ChooseBookPage import check_book_exists, create_book_list


def find_book_page(screen):
    name_book = StringVar()  #String для букв, а не чисел
    entry = Entry(screen, font=("Courier", 30), textvariable=name_book)  # поле для вводу
    entry.pack()
    def check_book():
        check, booklist = check_book_exists(name_book)
        if check:
            entry.destroy()
            btn3.destroy()
            create_book_list(screen,booklist)
    btn3 = Button(screen, text="Шукати книгу", bg="blue", activebackground="green", fg="white",
                  activeforeground="red", font=("Courier", 30),
                  relief=FLAT, overrelief=GROOVE, command=check_book)
    btn3.pack()
