from main import Book
from re import search


class ValidateBook(Book):
    variable: str

    def __init__(self):
        super().__init__(
            author=self.author,
            title=self.title,
            year=self.year
        )

    def validate_title(self):
        pass

    def validate_author(self):
        pass

    def validate_year(self) -> int:
        if search(r'/\D/g', self.year):
            raise ValueError('Ошибка при попытке добавить книгу. Год ее выпуска, к сожалению, не может быть чем-то кроме числа.')
        elif self.year == '' or self.year is None:
            raise ValueError('Ошибка при попытке добавить книгу. Необходимо ввести год ее выпуска.')
        else:
            year = int(self.year)
            if year > 2024 or year < 1900:
                raise ValueError('Ошибка при попытке добавить книгу. Год выпуска должен быть в пределах [1900 - 2024]')
            return year
