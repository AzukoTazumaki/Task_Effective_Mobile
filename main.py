from random import randint
from validator import ValidateBook


class Book:
    """
    :param title: Название книги, может содержать как цифры, так и буквы.
    :param author: Имя автора, строго буквы.
    :param year: Год выпуска, строго цифры.
    """
    variable: dict

    def __init__(self,
                 title: str,
                 author: str,
                 year: int):
        self.book_id: int = int(randint(1, 1000000) * 0.8 + randint(1, 1000000) * 0.4)
        self.title = title
        self.author = author
        self.year = year
        self.status = True

    def create_book(self):
        pass

    def read_book(self):
        pass

    def update_book(self):
        pass

    def delete_book(self):
        pass

    def search_book(self):
        pass


if __name__ == '__main__':
    pass
