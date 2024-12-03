from json import load, dump
import os


class JSON:
    def __init__(self):
        self.folder = 'data'
        self.filename = 'books.json'
        self.path = self.get_the_directory()
        self.loaded_data = self.start_json()

    def get_the_directory(self):
        directory = os.getcwd()
        path = os.path.join(directory, self.folder, self.filename)
        return path

    def load_file(self):
        with open(self.path, 'r') as file:
            json_data = load(file)
            file.close()
        return json_data

    def check_json_file(self) -> bool:
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
        self.check_json_file()
        return self.load_file()


class MethodsJSON(JSON):
    def __init__(self):
        super().__init__()

    def upload_data(self, json_data: dict):
        with open(self.path, 'w') as file:
            dump(json_data, file, ensure_ascii=False, indent=4)
            file.close()

    def add_data_to_json(self, data: dict):
        self.loaded_data['books'].append(data)
        self.upload_data(self.loaded_data)

    def remove_data_from_json(self, book_id: int):
        def check_id():
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
        books = self.loaded_data['books']
        if books[index]['status'] == 'В наличии':
            books[index]['status'] = 'Выдана'
        else:
            books[index]['status'] = 'В наличии'
        self.upload_data(self.loaded_data)
        return books[index]['status']
