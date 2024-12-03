from models.book_model import Book
from models.validator_model import Validator
from models.json_model import JSON, MethodsJSON
from models.search_model import Search


class Library:
    def __init__(self):
        self.json_obj = JSON()
        self.start_json = self.json_obj.start_json
        self.methods_json_obj = MethodsJSON
        self.validator = Validator
        self.search = Search

    def create_book(self, title: str, author: str, year: int) -> bool | ValueError:
        book = Book(title=title, author=author, year=year)
        activate_validator = self.validator(book.return_dict())
        if type(activate_validator.final_validation()) is ValueError:
            return activate_validator.final_validation()
        else:
            loaded_json_model = self.methods_json_obj()
            loaded_json_model.add_data_to_json(activate_validator.final_validation())
            return book.book_id

    def read_books(self) -> dict:
        return self.start_json()

    def update_book(self, book_id: int) -> list:
        int_book_id = int(book_id)
        index_book = self.search(int_book_id).search_by_id()
        if type(index_book) is not bool:
            book_status = self.methods_json_obj().update_data_in_json(index_book)
            return [self.start_json()['books'][index_book]['title'], book_status]
        else:
            return TypeError

    def delete_book(self) -> bool | ValueError:
        pass

    def search_books(self) -> list:
        pass
