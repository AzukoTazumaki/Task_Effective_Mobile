from random import randint


class Book:
    """
    Класс, описывающий книгу и содержащий в себе всю необходимую про нее информацию.
    """
    def __init__(self, title: str, author: str, year: int):
        """
        :param title: Название книги.
        :param author: Имя автора.
        :param year: Год выпуска.
        """
        self.book_id: int = int(randint(1, 1000000) * 0.8 + randint(1, 1000000) * 0.4)
        self.title = title
        self.author = author
        self.year = year
        self.status = True

    def return_dict(self):
        """
        :return: Возвращает словарь, содержащий в себе всю необходимую информацию о книге.
        """
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    
