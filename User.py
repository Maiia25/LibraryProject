import validators
from datetime import datetime
class User:
    def __init__(self, name, telephone, email, year):
        self.__name = name
        self.__telephone = telephone
        if validators.email(email):
            self.__email = email
        else:
            print("Invalid email")
        if  year < datetime.now().year - 10:
            self.__year = year
        else:
            print("Invalid date")
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
    def get_telephone(self):
        return self.__telephone
    def set_telephone(self, new_telephone):
        self.__telephone = new_telephone
    def get_email(self):
        return self.__email
    def set_email(self, new_email):
        if validators.email(new_email):
            self.__email = new_email
        else:
            print("Invalid email")

    def get_year(self):
        return self.__year
    def set_year(self, new_year):
        if  new_year < datetime.now().year - 10:
            self.__year = new_year
        else:
            print("Invalid date")
    