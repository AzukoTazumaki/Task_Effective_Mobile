from models.book_model import Book
from models.validator_model import Validator
from models.json_model import JSON, MethodsJSON
from models.search_model import Search


class Library:
    """
    Класс "Библиотека", использующий все созданные классы для выполнения необходимых операций.
    """
    def __init__(self):
        """
        Автоматически инициализируются все классы. Классы JSON и MethodsJSON вызываются сразу же,
        так как ничего не принимают в качестве параметров.
        """
        self.json_obj = JSON()
        self.start_json = self.json_obj.start_json
        self.methods_json_obj = MethodsJSON()
        self.validator = Validator
        self.search = Search

    def create_book(self, title: str, author: str, year: int) -> int | ValueError:
        """
        :param title: Название книги, введенное пользователем.
        :param author: Автор книги, введенный пользователем.
        :param year: Год книги, введенный пользователем.
        :return: Если тип ответа, который возвращает метод из класса, отвечающего за валидацию данных, –
        это ValueError, то возвращается сообщение-ошибка, иначе возвращается идентификатор добавленной книги.
        Для начала создается объект книги, куда в качестве аргументов попадают введенные пользователем данные.
        Затем вызывается метод представления объекта книги как словаря и в качестве аргумента отправляется на валидацию.
        При успешной валидации книга автоматически добавляется в библиотеку.
        """
        book = Book(title=title, author=author, year=year)
        activate_validator = self.validator(book.return_dict())
        if type(activate_validator.final_validation()) is ValueError:
            return activate_validator.final_validation()
        else:
            loaded_json_model = self.methods_json_obj
            loaded_json_model.add_data_to_json(activate_validator.final_validation())
            return book.book_id

    def read_books(self) -> dict:
        """
        :return: Метод из класса JSON возвращает загруженный файл .json, его и возвращаем при вызове
        метода прочтения всего списка книг, имеющихся в библиотеке.
        """
        return self.start_json()

    def update_book(self, book_id: int) -> list | TypeError:
        """
        :param book_id: Принимает идентификатор книги, у которой необходимо обновить статус.
        :return: При успешной валидации возвращает список, содержащий в себе название книги и
        ее обновленный статус, иначе ошибку TypeError. Пришедший идентификатор отправляется на
        валидацию, чтобы проверить, является ли он числом. Далее вызывается метод класса, отвечающего
        за поиск.
        """
        validated_book_id = self.validator.validate_number(book_id)
        index_book = self.search(validated_book_id).search_by_id()
        if type(index_book) is not bool:
            book_status = self.methods_json_obj.update_data_in_json(index_book)
            book_title = self.start_json()['books'][index_book]['title']
            return [book_title, book_status]
        else:
            return ValueError

    def delete_book(self, book_id: int) -> bool | ValueError:
        """
        :param book_id: Принимает идентификатор книги, которую необходимо удалить.
        :return: Возвращает True, False или пустой вызов ValueError (в связи с выводом сообщений в консоль).
        Есть способ сделать лучше, но я пока не додумался, как было бы лучше это сделать.
        Пришедший идентификатор отправляется на валидацию для проверки на число. Если ответ от метода класса,
        отвечающего за валидацию, – ValueError, возвращается ValueError (сообщение о том, что валидация не пройдена),
        иначе вызываем метод класса, отвечающего за работу с файлом .json. Если в ответ приходит False, то и возвращаем
        False (сообщение о том, что книга с введенным идентификатором не найдена), иначе True (сообщение об успешном
        удалении книги).
        """
        validated_book_id = self.validator.validate_number(book_id)
        if type(validated_book_id) is ValueError:
            return ValueError()
        else:
            removed_book = self.methods_json_obj.remove_data_from_json(validated_book_id)
            return False if not removed_book else True

    def search_books(self, parameter: int, fragment: str) -> list | ValueError:
        """
        :param parameter: Принимает номер параметра, по которому пользователь хочет осуществить поиск (от 1 до 3 –
        название, автор и год выпуска книги соответственно).
        :param fragment: Фрагмент, по которому необходимо осуществить поиск.
        :return: В зависимости от выбранного параметра возвращает метод класса, отвечающего за поиск, куда аргументами
        отправляются выбранные параметр и фрагмент. Для начала параметр проходит валидацию на соответствие условиям
        выполнения кода, затем с помощью конструкции match - case выбирается нужный параметр. Если же валидация не
        прошла, возвращается сообщение об ошибке.
        """
        validated_parameter = self.validator.validate_number(parameter)
        if 1 <= validated_parameter <= 3:
            match validated_parameter:
                case 1:
                    return self.search(title=fragment).match_args('title')
                case 2:
                    return self.search(author=fragment).match_args('author')
                case 3:
                    return self.search(year=fragment).match_args('year')
        elif type(validated_parameter) is ValueError:
            return validated_parameter
