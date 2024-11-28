from datetime import datetime
class Book:
    def __init__(self, title, author, year_published, genre):
        self.__title = title
        self.__author = author
        if year_published > datetime.now().year:
            print("The year must be less than current year")
        elif year_published < 1000:
            print("The year must be greater than current year")
        else:
            self.__year_published = year_published
        self.__genre = genre
        self.__exist = True
    def information(self):
        return self.get_title() + " " +self.get_author() + " "+ str(self.get_year_published()) + " "+ self.get_genre()
    def get_exist(self):
        return self.__exist
    def set_busybook(self):
        self.__exist = False
    def set_freebook(self):
        self.__exist = True
    def get_title(self):
        return self.__title
    def set_title(self, new_title):
        self.__title = new_title
    def get_author(self):
        return self.__author
    def set_author(self, new_author):
        self.__author = new_author
    def get_year_published(self):
        return self.__year_published
    def set_year_published(self, new_year_published):
        if new_year_published > datetime.now().year:
            print("The year must be less than current year")
        elif new_year_published < 1000:
            print("The year must be greater than current year")
        else:
            self.__year_published = new_year_published
    def get_genre(self):
        return self.__genre
    def set_genre(self, new_genre):
        self.__genre = new_genre

#class User, library