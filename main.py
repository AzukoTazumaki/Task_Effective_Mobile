from time import sleep
from models.library_model import Library
from messages import *
from sys import exit


class App:
    def __init__(self):
        self.library = Library()
        self.reload_msg = [reload_1, reload_2, reload_3]
        self.quit_msg = [quit_1, quit_2, quit_3, quit_4]
        self.app_name = 'БИБЛИОТЕКА AZUKO'

    def run(self):
        try:
            sleep(1)
            # welcome_msg = [self.app_name, welcome_msg_pt_1, welcome_msg_pt_2, welcome_msg_pt_3]
            # self.delay_messages(welcome_msg, 2)
            self.choose_method()
        except KeyboardInterrupt:
            self.exit_app()

    def choose_method(self):
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
        for message in messages:
            print(message)
            sleep(delay)

    def run_method(self, method: int):
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
                print(all_books_msg)
                for book in loaded_data['books']:
                    print(book_msg.format(
                        book_id=book['id'],
                        title=book['title'],
                        author=book['author'],
                        year=book['year'],
                        status=book['status']))
                print(all_books_len_msg.format(books_len=books_len))
                return self.choose_method()

            case 3:
                while True:
                    book_id = input(id_input)
                    try:
                        params = self.library.update_book(book_id)
                        print(changed_book_status.format(title=params[0], status=params[1]))
                        break
                    except TypeError:
                        print(search_id_error)
                        self.delay_messages(self.reload_msg, 0.7)
                        continue
                return self.choose_method()

            case 4:
                while True:
                    book_id = input(id_input)
                    deleted_book = self.library.delete_book(book_id)
                    if not deleted_book:
                        print(validate_id_error)
                        self.delay_messages(self.reload_msg, 0.7)
                        continue
                    elif type(deleted_book) is ValueError:
                        print(search_id_error)
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
        self.delay_messages(self.quit_msg, 0.7)
        sleep(1.5)


if __name__ == "__main__":
    app = App()
    app.run()

