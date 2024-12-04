from tkinter import *
#from PIL import Image, ImageTk
from PIL import Image, ImageTk

from FindBookPage import find_book_page
from Library import *
from Book import *  # * - імпортує все
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
  entry = Entry(screen, font=("Courier", 30))
  entry.pack()
  btn4 = Button(screen, text="Введіть назву книги", bg="blue", activebackground="green", fg="white",
              activeforeground="red", font=("Courier", 30),
                 relief=FLAT, overrelief=GROOVE)
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

