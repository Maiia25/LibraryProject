from tkinter import *
#from PIL import Image, ImageTk
from PIL import Image, ImageTk

from FindBookPage import find_book_page
from Library import *
from Book import *  # * - імпортує все
from ReturnButton import return_userbook
screen = Tk()
screen.geometry("600x400")
screen.title("Welcome to the library")
bg_image = Image.open("book.jpg")
bg_image = bg_image.resize((600, 400)) #картеж- список. який не можна змінювати
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(screen, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
def choosebook():
    btn.destroy()
    btn1.destroy()
    btn2.destroy()
    find_book_page(screen)
btn = Button(screen, text="Пошук книги", bg="blue", activebackground="green", fg="white",
              activeforeground="red", font=("Courier", 30),
                 relief=FLAT, overrelief=GROOVE, command = choosebook) #relief - рамка кнопки
btn.pack(pady=20) #відступ
def returnbook():
  btn.destroy()
  btn1.destroy()
  btn2.destroy()
  user_book = StringVar()
  label_returnbook = Label(screen, text="Введіть назву книги", font=("Courier", 24))
  label_returnbook.pack()
  entry = Entry(screen, font=("Courier", 30), textvariable=user_book)
  entry.pack()
  user_name = StringVar()
  label_name = Label(screen, text="Введіть ім'я", font=("Courier", 24))
  label_name.pack()
  entry_name = Entry(screen, font=("Courier", 30), textvariable=user_name)
  entry_name.pack()
  user_phone = StringVar()
  label_phone = Label(screen, text="Введіть телефон", font=("Courier", 24))
  label_phone.pack()
  entry_phone = Entry(screen, font=("Courier", 30), textvariable=user_phone)
  entry_phone.pack()
  def send_data ():
      label_returnbook.destroy()
      entry.destroy()
      label_name.destroy()
      entry_name.destroy()
      label_phone.destroy()
      entry_phone.destroy()
      btn4.destroy()
      return_userbook(screen, user_book, user_name, user_phone)
  btn4 = Button(screen, text="Повернути", bg="blue", activebackground="green", fg="white",
              activeforeground="red", font=("Courier", 30),
                 relief=FLAT, overrelief=GROOVE, command = send_data)
  btn4.pack()
btn1 = Button(screen, text="Повернути книгу", bg="blue", activebackground="green", fg="white",
              activeforeground="red", font=("Courier", 30),
                 relief=FLAT, overrelief=GROOVE, command = returnbook) #relief - рамка кнопки
btn1.pack()
btn2 = Button(screen, text="Вийти з програми", bg="blue", activebackground="green", fg="white",
              activeforeground="red", font=("Courier", 30),
                 relief=FLAT, overrelief=GROOVE, command = screen.destroy)
btn2.pack(pady=20)
screen.mainloop()