from models.json_model import JSON


class Search:
    """
    Класс "Поиск", содержит необязательные параметры, так как при разных условиях понадобится ввести только один
    из параметров, по которому будет осуществляться поиск книг.
    """
    def __init__(self, book_id=None, title=None, author=None, year=None, status=None):
        """
        :param book_id: Идентификатор книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год выпуска книги.
        :param status: Статус книги ("В наличии" или "Выдана").
        Помимо параметров здесь сразу вызывается метод класса JSON, который автоматически при создании экземпляра
        класса "Поиск" загружает файл .json.
        """
        self.book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: bool = status
        self.loaded_data: dict = JSON().start_json()

    def search_by_id(self) -> int | bool:
        """
        :return: Возвращает либо индекс книги, в которой найдено совпадение с идентификатором, введенным пользователем,
        либо False, означающего отсутствие совпадений. Циклом for проверяется каждая книга в загруженных данных из файла
        .json, на каждой итерации сравниваются идентификатор книги и тот, что ввел пользователь.
        """
        for index, book in enumerate(self.loaded_data['books']):
            if book['id'] == self.book_id:
                return index
            continue
        return False

    def search_by_argument(self, arg_key: str, arg_class: str | int | bool) -> list | bool:
        """
        :param arg_key: Ключ, по которому осуществляется поиск.
        :param arg_class: Фрагмент, на основе которого ищутся совпадения.
        :return: Возвращает False, если совпадений не найдено, либо список найденных книг.
        Создается пустой список, куда будут добавляться найденные по введенному пользователем фрагменту книги.
        Далее вызывается вложенная функция, которая циклом проходится по каждой книге, имеющейся в библиотеке.
        В конце проверяется длина итогового списка, если она равна нулю, значит совпадений не найдено и возвращается
        False, иначе возвращается сам список с найденными совпадениями.
        """
        found_books_null = []

        def match_check():
            """
            :return: Возвращает список найденных совпадений.
            На каждой итерации цикла проверяется, имеется ли фрагмент, введенный пользователем, в выбранном параметре.
            Если совпадение есть, книга добавляется в созданный список, иначе начинается следующая итерация. В конце
            цикла возвращается итоговый список с найденными совпадениями.
            """
            for index, book in enumerate(self.loaded_data['books']):
                if (arg_class in book[arg_key]) or (arg_class == book[arg_key]):
                    found_books_null.append(self.loaded_data['books'][index])
                continue
            return found_books_null

        found_books = match_check()

        if len(found_books) == 0:
            return False
        else:
            return found_books

    def match_args(self, argument: str) -> str | int | bool | list:
        """
        :param argument: Принимает аргумент (ключ словаря книги), в котором будет осуществляться поиск
        совпадений с фрагментом, введенным пользователем.
        :return: Возвращает вызов метода, куда в качестве аргументов отправляются ключ словаря и фрагмент, поиск по
        которым необходимо осуществить.
        """
        match argument:
            case 'title':
                return self.search_by_argument('title', self.title)
            case 'author':
                return self.search_by_argument('author', self.author)
            case 'year':
                return self.search_by_argument('year', self.year)
