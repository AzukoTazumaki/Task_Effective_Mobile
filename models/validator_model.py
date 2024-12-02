from re import search
from messages import validate_title_error, validate_title_len_error, validate_author_error, validate_author_len_error, \
    validate_author_only_digits, validate_year_error, validate_year_type_error, validate_year_range_error


class Validator:
    variable: dict | ValueError

    def __init__(self, book: dict):
        """
        :param book: на валидацию приходит вся книга
        """
        self.book_id: int = book['id']
        self.title: str = book['title']
        self.author: str = book['author']
        self.year: int = book['year']
        self.status: bool = book['status']

    def validate_title(self) -> str | ValueError:
        if self.title == '':
            return ValueError(validate_title_error)
        elif len(self.title) > 45:
            return ValueError(validate_title_len_error)
        else:
            return self.title

    def validate_author(self) -> str | ValueError:
        if self.author == '':
            return ValueError(validate_author_error)
        elif len(self.author) > 15:
            return ValueError(validate_author_len_error)
        else:
            author_without_spaces = self.author.replace(' ', '')
            if author_without_spaces.isdigit():
                return ValueError(validate_author_only_digits)
            return self.author

    def validate_year(self) -> int | ValueError:
        if not int(self.year):
            return ValueError(validate_year_type_error)
        elif self.year == '':
            return ValueError(validate_year_error)
        else:
            year = int(self.year)
            if year > 2024 or year < 1900:
                return ValueError(validate_year_range_error)
            return year

    def final_validation(self) -> dict | ValueError:
        validate_vars = [self.validate_title, self.validate_author, self.validate_year]
        for var in validate_vars:
            if type(var()) is ValueError:
                return var()
            continue
        return {
            'id': self.book_id,
            'title': self.validate_title(),
            'author': self.validate_author(),
            'year': self.validate_year(),
            'status': 'В наличии' if self.status is True else 'Выдана'
        }
