from json import load, dump
import os


class JSON:
    """
    Класс занимается сугубо инициализацией работы с файлом .json. Он автоматически при создании получает директорию,
    в которой находится файл, и загружает его данные.
    """
    def __init__(self):
        self.folder = 'data'
        self.filename = 'books.json'
        self.path = self.get_the_directory()
        self.loaded_data = self.start_json()

    def get_the_directory(self) -> str:
        """
        :return: Возвращает путь к файлу .json с книгами.
        """
        directory = os.getcwd()
        path = os.path.join(directory, self.folder, self.filename)
        return path

    def load_file(self) -> dict:
        """
        :return: Возвращает загруженный файл .json в виде словаря.
        """
        with open(self.path, 'r') as file:
            json_data = load(file)
            file.close()
        return json_data

    def check_json_file(self) -> bool:
        """
        :return: Возвращает True либо False в зависимости от того, существует ли открываемый файл. Если удалось открыть,
        возвращается True, если же не удалось – создается файл со словарем внутри ит возвращается False.
        """
        try:
            open(self.path)
            return True
        except FileNotFoundError:
            initial_data = {'books': []}
            with open(self.path, 'w') as file:
                dump(initial_data, file)
                file.close()
            return False

    def start_json(self):
        """
        :return: Возвращает загруженный файл .json. Метод создан для имитации активации класса JSON как цельной программы по работе с .json.
        Как результат, этим методом автоматически загружается файл (либо создается), а дальше уже работаем с этим файлом.
        """
        self.check_json_file()
        return self.load_file()


class MethodsJSON(JSON):
    """
    Дочерний класс, созданный по логике для выполнения методов по работе с файлом .json.
    """
    def __init__(self):
        super().__init__()

    def upload_data(self, json_data: dict):
        """
        :param json_data: Принимает перезаписанный словарь, который загружается в файл .json.
        :return: Возвращает True по окончании выполнения кода.
        """
        with open(self.path, 'w') as file:
            dump(json_data, file, ensure_ascii=False, indent=4)
            file.close()
            return True

    def add_data_to_json(self, data: dict):
        """
        :param data: Принимает словарь, успешно прошедший валидацию.
        :return: Возвращает вызов метода загрузки перезаписанного словаря со списком книг в файл .json.
        """
        self.loaded_data['books'].append(data)
        return self.upload_data(self.loaded_data)

    def remove_data_from_json(self, book_id: int):
        """
        :param book_id: Принимает идентификатор книги, успешно прошедший валидацию на ввод числа,
        которую необходимо удалить из файла .json.
        :return: Возвращает True или False в зависимости от того, была ли удалена книга или нет.
        Если книга была успешно удалена, файл .json перезаписывается.
        """
        def check_id():
            """
            :return: Возвращает True или False в зависимости от того, найден ли идентификатор (существует ли
            данная книга или нет). Циклом for метод проходится по всем имеющимся в библиотеке книгам и проверяет
            на совпадение идентификатор, введенный пользователем, с идентификатором книги на каждой итерации.
            """
            for index, book in enumerate(self.loaded_data['books']):
                if book['id'] == book_id:
                    self.loaded_data['books'].pop(index)
                    return True
                continue
            return False

        if not check_id():
            return False
        else:
            self.upload_data(self.loaded_data)
            return True

    def update_data_in_json(self, index: int):
        """
        :param index: Принимает индекс книги в списке, у которой необходимо обновить статус.
        :return: Возвращает обновленный статус книги. Упрощенный метод, который автоматически меняет
        статус выбранной книги на противоположный, так как представлено всего два варианта: "В наличии" и "Выдана".
        """
        books = self.loaded_data['books']
        if books[index]['status'] == 'В наличии':
            books[index]['status'] = 'Выдана'
        else:
            books[index]['status'] = 'В наличии'
        self.upload_data(self.loaded_data)
        return books[index]['status']
