from Book import *
from User import *
import validators
class Library:
    __id = 1
    def __init__(self, name, address, country, email):
        self.__name = name
        self.__address = address
        self.__country = country
        if validators.email(email):
            self.__email = email
        else:
            print("Invalid email")
        self.__books = []
        self.__users = []
        self.__journal = {}
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_Books(self):
        return self.__books
    def get_country(self):
        return self.__country
    def set_country(self, new_country):
        self.__country = new_country

    def get_email(self):
        return self.__email
    def set_email(self, new_email):
        if validators.email(new_email):
            self.__email = new_email
        else:
            print("Invalid email")
    def get_address(self):
        return self.__address
    def set_address(self, new_address):
        self.__address = new_address
    def register_book(self, title, author, year_published, genre):
        self.__books.append(Book(title, author, year_published, genre))
        print("Book was added.")
    def list_books(self):
        for book in self.__books:
            print(book.information())
    def register_user(self, name, telephone, email, year):
        self.__users.append(User(name, telephone, email, year))
    def reserve(self, name, telephone, book):
        for user in self.__users:
            if user.get_name() == name and user.get_telephone() == telephone:
                    book.set_busybook()
                    self.__journal[self.__id] = [book, user]
                    self.__id = self.__id+1
    def return_book(self, name, telephone, title):
        for user in self.__users:
            if user.get_name() == name and user.get_telephone() == telephone:
                for book in self.__books:
                    if book.get_title() == title and not book.get_exist():
                        book.set_freebook()
    def history_journal(self, name, telephone):
        for user in self.__users:
            if user.get_name() == name and user.get_telephone() == telephone:
                for j in self.__journal.values():
                    if j.count(user)==1:
                        print(j[0].get_title() + " " + user.get_name())

    def findbook(self, title):
        booklist = []
        for book in self.__books:
            if book.get_title().capitalize() == title.capitalize():
                booklist.append(book) #додати в список
        return booklist