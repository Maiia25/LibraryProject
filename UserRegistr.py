from tkinter import *

from UserJournal import show_journal


def enter_userinfo(screen, library, current_book):
    user_name = StringVar()  # String для букв, а не чисел
    label_name = Label(screen, text="Введіть ім'я", font=("Courier", 24))
    label_name.pack()
    entry_name = Entry(screen, font=("Courier", 24),
                       textvariable=user_name)  # поле для вводу textvariable- змінна, яку прив'язуємо до entry
    entry_name.pack()
    user_phone = StringVar()
    label_phone = Label(screen, text="Введіть телефон", font=("Courier", 24))
    label_phone.pack()
    entry_phone = Entry(screen, font=("Courier", 24), textvariable=user_phone)  # поле для вводу
    entry_phone.pack()
    user_mail = StringVar()
    label_mail = Label(screen, text="Введіть пошту", font=("Courier", 24))
    label_mail.pack()
    entry_mail = Entry(screen, font=("Courier", 24), textvariable=user_mail)  # поле для вводу
    entry_mail.pack()
    user_year = IntVar()  # числова змінна
    label_year = Label(screen, text="Введіть рік народження", font=("Courier", 24))
    label_year.pack()
    entry_year = Entry(screen, font=("Courier", 24), textvariable=user_year)  # поле для вводу
    entry_year.pack()
    def accept_userinfo():
        library.register_user(user_name.get(), user_phone.get(), user_mail.get(), user_year.get()) #get-функція
        library.reserve(user_name.get(), user_phone.get(), current_book)
        library.history_journal(user_name.get(), user_phone.get())
        show_journal(screen, user_name.get(), current_book)
        entry_year.destroy()
        entry_mail.destroy()
        entry_phone.destroy()
        entry_name.destroy()
        label_year.destroy()
        label_mail.destroy()
        label_phone.destroy()
        label_name.destroy()
        btnsend.destroy()
    btnsend = Button(screen, text="Підтвердити", bg="blue", activebackground="green", fg="white",
                     activeforeground="red", font=("Courier", 24),
                     relief=FLAT, overrelief=GROOVE, command=accept_userinfo)

    btnsend.pack()

