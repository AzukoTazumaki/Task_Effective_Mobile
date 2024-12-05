from time import sleep
from models.library_model import Library
from messages import *


class App:
    """
    Класс "Приложение" создан для непосредственного взаимодействия с пользователем.
    """
    def __init__(self):
        """
        Создается экземпляр класса "Библиотека", затем список сообщений о перезагрузке, выходе из приложения,
        в конце задается название приложения.
        """
        self.library = Library()
        self.reload_msg = [reload_1, reload_2, reload_3]
        self.quit_msg = [quit_1, quit_2, quit_3, quit_4]
        self.app_name = 'БИБЛИОТЕКА AZUKO'

    def run(self):
        """
        :return: Возвращает либо вызов метода выбора метода взаимодействия с программой (тавтология получилась,
        конечно (￣_￣)・・・), либо (при остановке программы – обработка нажатия клавиш выхода из программы) метод
        вызова выхода из приложения.
        """
        try:
            sleep(1)
            welcome_msg = [self.app_name, welcome_msg_pt_1, welcome_msg_pt_2, welcome_msg_pt_3]
            self.delay_messages(welcome_msg, 1.5)
            return self.choose_method()
        except KeyboardInterrupt:
            return self.exit_app()

    def choose_method(self):
        """
        :return: Возвращает либо метод взаимодействия с программой, либо сообщения об ошибке в случае, если введенное
        число не входит в диапазон допустимых чисел, или ошибку типа данных (когда пользователь вместо цифры ввел
        буквы или знаки).
        """
        while True:
            try:
                method = int(input(choose_method))
                if 1 <= method <= 6:
                    return self.run_method(method)
                else:
                    self.delay_messages([method_out_of_range_msg, *self.reload_msg], 0.7)
                    continue
            except ValueError:
                self.delay_messages([choose_method_error, *self.reload_msg], 0.7)
                continue

    @staticmethod
    def delay_messages(messages: list, delay: float):
        """
        :param messages: Список сообщений, которые необходимо вывести с некоторой задержкой.
        :param delay: Время задержки сообщений.
        :return: Не возвращает ничего, лишь выводит в консоль сообщения, переданные в качестве аргумента.
        """
        for message in messages:
            print(message)
            sleep(delay)

    def run_method(self, method: int):
        """
        :param method: Принимает число, обозначающее номер метода взаимодействия с программой.
        :return: В каждом блоке case возвращает вызов метода выбора метода взаимодействия с программой ((￣_￣)・・・).
        1 – Добавить книгу: Пользователь вводит три параметра, далее вызывается метод класса "Библиотека", отвечающий
        за создание книги. Если вернулась ошибка ValueError, выводится эта ошибка, затем сообщения о перезагрузке. После
        этого наступает следующая итерация – пользователь заново вводит параметры. После успешного добавления цикл
        прерывается и в консоль выводится сообщение об успешном добавлении книги с ее идентификатором.
        2 – Посмотреть список книг: Вызывается метод класса "Библиотека", отвечающий за вывод всех имеющихся книг.
        Проверяется, есть ли книги в библиотеке. Если имеются, то выводятся в консоль, иначе выводится сообщение олб
        их отсутствии.
        3 – Обновить статус книги: Пользователь вводит идентификатор книги, у которой хочет
        обновить статус. Если книга найдена, выводится название книги и ее новый статус, иначе сообщения об ошибке
        (когда идентификатор не найден либо ошибка ввода).
        4 – Удалить книгу: Пользователь вводит идентификатор книги, которую хочет
        удалить. Если книга найдена, выводится сообщение об ее успешном удалении, иначе сообщения об ошибке
        (когда идентификатор не найден либо ошибка ввода).
        5 – Поиск книги: Пользователь вводит параметр и фрагмент, по которым осуществляет поиск книг. Если список
        пустой, выводится сообщение об отсутствии совпадений, иначе список найденных по запросу пользователя книг.
        6 – Выход из программы: осуществляет остановку приложения.
        """
        match method:
            case 1:
                while True:
                    title = input(title_input)
                    author = input(author_input)
                    year = input(year_input)
                    created_book = self.library.create_book(title=title, author=author, year=year)
                    if type(created_book) is ValueError:
                        print(created_book)
                        self.delay_messages(self.reload_msg, 0.7)
                        continue
                    else:
                        break
                print(add_book_success.format(book_id=created_book))
                return self.choose_method()

            case 2:
                loaded_data = self.library.read_books()
                books_len = len(loaded_data['books'])
                if books_len != 0:
                    print(all_books_msg)
                    for book in loaded_data['books']:
                        print(book_msg.format(
                            book_id=book['id'],
                            title=book['title'],
                            author=book['author'],
                            year=book['year'],
                            status=book['status']))
                    print(all_books_len_msg.format(books_len=books_len))
                else:
                    self.delay_messages([no_books, *self.reload_msg], 0.7)
                return self.choose_method()

            case 3:
                while True:
                    book_id = input(id_input)
                    try:
                        params = self.library.update_book(book_id)
                        print(changed_book_status.format(title=params[0], status=params[1]))
                        break
                    except ValueError:
                        print(search_id_error)
                        self.delay_messages(self.reload_msg, 0.7)
                        continue
                return self.choose_method()

            case 4:
                while True:
                    book_id = input(id_input)
                    deleted_book = self.library.delete_book(book_id)
                    if not deleted_book:
                        print(search_id_error)
                        self.delay_messages(self.reload_msg, 0.7)
                        continue
                    elif type(deleted_book) is ValueError:
                        print(validate_number_error)
                        self.delay_messages(self.reload_msg, 0.7)
                        continue
                    else:
                        print(deleted_book_success)
                        break
                return self.choose_method()

            case 5:
                self.delay_messages([search_by_argument_msg], 1)
                parameter = input(search_by_argument_input)
                fragment = input(search_fragment_input)
                searched_books: list = self.library.search_books(parameter, fragment)
                if searched_books is False:
                    print(searched_null)
                    self.delay_messages(self.reload_msg, 0.7)
                else:
                    self.delay_messages(searched_books, 0.4)
                return self.choose_method()

            case 6:
                self.exit_app()

    def exit_app(self):
        """
        :return: Ничего не возвращает, метод является обработкой ошибки KeyboardInterrupt, выводя сообщения
        о выходе из программы
        """
        self.delay_messages(self.quit_msg, 0.7)
        sleep(1.5)


if __name__ == "__main__":
    app = App()
    app.run()
