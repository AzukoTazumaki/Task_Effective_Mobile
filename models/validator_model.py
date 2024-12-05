from messages import validate_title_error, validate_title_len_error, validate_author_error, validate_author_len_error, \
    validate_author_only_digits, validate_year_error, validate_year_type_error, validate_year_range_error, \
    validate_number_error


class Validator:
    def __init__(self, book: dict):
        """
        :param book: На валидацию приходит вся книга, из которой забирается вся необходимая информация.
        """
        self.book_id: int = book['id']
        self.title: str = book['title']
        self.author: str = book['author']
        self.year: str = book['year']
        self.status: bool = book['status']

    @staticmethod
    def validate_number(number: str) -> int | ValueError:
        """
        :param number: Принимает число, введенное пользователем.
        :return: Возвращает ValueError (сообщение о том, что валидация не пройдена), если пользователь ввел не цифры
        (или не только цифры), либо само число, переведенное из типа "str" в int".
        """
        try:
            int_number = int(number)
            return int_number
        except ValueError:
            return ValueError(validate_number_error)

    def validate_title(self) -> str | ValueError:
        """
        :return: Возвращает ValueError (сообщение о том, что валидация не пройдена), если пользователь не ввел ничего
        или ввел количество символов, превышающее максимальное, либо строку, содержащую название книги.
        """
        if self.title == '':
            return ValueError(validate_title_error)
        elif len(self.title) > 45:
            return ValueError(validate_title_len_error)
        else:
            return self.title

    def validate_author(self) -> str | ValueError:
        """
        :return: Возвращает ValueError (сообщение о том, что валидация не пройдена), если пользователь не ввел ничего,
        ввел количество символов, превышающее максимальное, или ввел только цифры, либо строку, содержащую автора
        книги.
        """
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
        """
        :return: Возвращает ValueError (сообщение о том, что валидация не пройдена), если пользователь ввел не цифры
        (или не только цифры), отправил пустую строку, ничего не заполнив, или ввел год, не попадающий в допустимый
        диапазон чисел, либо возвращает год выпуска книги, переведенный из типа "str" в int".
        """
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
        """
        :return: Возвращает либо ошибку из находящихся выше методов, либо, в случае успешной валидации, словарь
        с введенными пользователем значениями.
        Создается список с методами без их вызова. Далее цикл проходится по каждому из методов и вызывает его,
        возвращая ValueError (в случае, если какой-либо из методов возвращает данную ошибку). Далее возвращается
        словарь.
        """
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
