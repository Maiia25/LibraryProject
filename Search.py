class Search:
    def __init__ (self, library):
        self.library = library
    def search_by_title(self, title):
        filtered_books = []
        for book in self.library.get_Books :
            if book.get_title() == title:
                filtered_books.append(book.information())
        return filtered_books
    def search_by_author(self, author):
        filtered_books = []
        for book in self.library.get_Books:
            if book.get_author() == author:
                filtered_books.append(book.information())
        return filtered_books
    def search_by_year_published(self, year_published):
        filtered_books = []
        for book in self.library.get_Books():
            if book.get_year_published() == year_published:
                filtered_books.append(book.information())
        return filtered_books
    def search_by_genre(self, genre):
        filtered_books = []
        for book in self.library.get_Books:
            if book.get_genre() == genre:
                filtered_books.append(book.information())
        return filtered_books

