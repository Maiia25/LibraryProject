from tkinter import *
#from PIL import Image, ImageTk
from PIL import Image, ImageTk

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
library = Library(name="Бібліотека", address="Київ", country="Україна", email="library@gmail.com")
library.register_book(title="Гарі Потер", author="Роулінг", year_published=2010, genre="фентезі")
library.register_book(title="Книга1", author="Автор1", year_published=2022, genre="історія")
library.register_book(title="Книга2", author="Автор2", year_published=2022, genre="фентезі")
library.register_book(title="Книга1", author="Автор2", year_published=2015, genre="історія")

def choosebook():
  btn.destroy()
  btn1.destroy()
  btn2.destroy()
  var1 = StringVar()#String для букв, а не чисел
  entry = Entry(screen, font=("Courier", 30), textvariable=var1)  # поле для вводу
  entry.pack()
  def findbook():
     booklist = library.findbook(var1.get())  #назва, яку ввів користувач
     if len(booklist)!=0:
         listbox = Listbox(bg="white", font=('Arial', 30), height=5)
         listbox.pack()
         entry.destroy()
         btn3.destroy()
         #listbox.insert(END, "Book 1")
         for book in booklist:
             listbox.insert(END, book.information())
             print(book.information())
         #def takebook(): #обрати книгу з наявних
         btn4 = Button(screen, text="Обрати книгу", bg="blue", activebackground="green", fg="white",
                  activeforeground="red", font=("Courier", 30),
                     relief=FLAT, overrelief=GROOVE)
         btn4.pack()
  btn3 = Button(screen, text="Шукати книгу", bg="blue", activebackground="green", fg="white",
              activeforeground="red", font=("Courier", 30),
                 relief=FLAT, overrelief=GROOVE, command = findbook)
  btn3.pack()
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

