from models.book_model import Book
from models.validator_model import Validator
from models.json_model import JSON, MethodsJSON


class Library:
    def __init__(self):
        self.json_obj = JSON
        self.methods_json_obj = MethodsJSON
        self.validator = Validator

    def create_book(self, title: str, author: str, year: int) -> bool | ValueError:
        book = Book(title=title, author=author, year=year)
        activate_validator = self.validator(book.return_dict())
        if type(activate_validator.final_validation()) is ValueError:
            return activate_validator.final_validation()
        else:
            loaded_json = self.methods_json_obj(activate_validator.final_validation())
            loaded_json.add_data_to_json()
            return book.book_id

    def read_books(self) -> list:
        return self.json_obj().start_json()

    def update_book(self) -> bool:
        pass

    def delete_book(self) -> bool | ValueError:
        pass

    def search_books(self) -> list:
        pass
