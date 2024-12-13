from tkinter import *
def show_journal(screen, user_name, current_book):
    label_name = Label(screen, text= f"{user_name}, ви обрали книгу {current_book.get_title()}", font=("Courier", 24))
    label_name.pack()
