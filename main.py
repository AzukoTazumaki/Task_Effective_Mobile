from time import sleep
from models.library_model import Library
from messages import *


class App:
    def __init__(self):
        self.library = Library()
        self.methods = [
            self.library.create_book,
            self.library.read_books,
            self.library.delete_book,
            self.library.update_book,
            self.library.search_books
        ]
        self.app_name = 'БИБЛИОТЕКА AZUKO'

    def run(self):
        sleep(1)
        welcome_msg = [self.app_name, welcome_msg_pt_1, welcome_msg_pt_2, welcome_msg_pt_3]
        self.delay_messages(welcome_msg, 2)
        while True:
            try:
                method = int(input(choose_method))
                return self.run_method(method)
            except ValueError:
                error_choose_method_msg = [choose_method_error, reload_1, reload_2, reload_3]
                self.delay_messages(error_choose_method_msg, 0.7)
                continue

    @staticmethod
    def delay_messages(messages: list, delay: float):
        for message in messages:
            print(message)
            sleep(delay)

    def run_method(self, method: int):
        print(self.methods[method - 1]())


if __name__ == "__main__":
    app = App()
    app.run()
