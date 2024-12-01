from random import randint


class Book:
    """
    :param title: Название книги, может содержать как цифры, так и буквы.
    :param author: Имя автора, строго буквы.
    :param year: Год выпуска, строго цифры.
    """
    variable: dict

    def __init__(self, title: str, author: str, year: int):
        self.book_id: int = int(randint(1, 1000000) * 0.8 + randint(1, 1000000) * 0.4)
        self.title = title
        self.author = author
        self.year = year
        self.status = True

    
