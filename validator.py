from main import Book
from re import search


class ValidateBook(Book):
    variable: dict | ValueError

    def __init__(self):
        super().__init__(
            author=self.author,
            title=self.title,
            year=self.year
        )

    def validate_title(self) -> str | ValueError:
        if self.title == '':
            raise ValueError('Ошибка ввода. Напишите, пожалуйста, название книги.')
        elif len(self.title > 45):
            raise ValueError('Ошибка ввода. Длина названия не должна превышать 15 символов.')
        else:
            return self.title

    def validate_author(self) -> str | ValueError:
        if self.author == '':
            return ValueError('Ошибка ввода. Напишите, пожалуйста, имя автора книги.')
        elif len(self.author > 15):
            return ValueError('Ошибка ввода. Длина имени не должна превышать 15 символов.')
        else:
            return self.author

    def validate_year(self) -> int | ValueError:
        if search(r'/\D/g', self.year):
            return ValueError('Ошибка при попытке добавить книгу. Год ее выпуска, к сожалению, не может быть чем-то '
                              'кроме числа.')
        elif self.year == '':
            return ValueError('Ошибка при попытке добавить книгу. Необходимо ввести год ее выпуска.')
        else:
            year = str(self.year)
            if year > 2024 or year < 1900:
                return ValueError('Ошибка при попытке добавить книгу. Год выпуска должен быть в пределах [1900 - 2024]')
            return year

    def final_validation(self) -> dict | ValueError:
        validate_vars = [self.validate_title, self.validate_author, self.validate_year]
        for var in validate_vars:
            if type(var()) is ValueError:
                return var()
            continue
        return {
            'title': self.validate_title(),
            'author': self.validate_author(),
            'year': self.validate_year()
        }
