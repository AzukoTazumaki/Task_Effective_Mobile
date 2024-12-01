from models.book_model import Book
from models.validator_model import Validator
from models.json_model import JSON


class Library:
    def __init__(self):
        self.json_obj = JSON()

    def create_book(self) -> bool | ValueError:
        pass

    def read_books(self) -> list:
        return self.json_obj.start_json()

    def update_book(self) -> bool:
        pass

    def delete_book(self) -> bool | ValueError:
        pass

    def search_books(self) -> list:
        pass
