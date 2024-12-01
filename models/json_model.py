from json import load, dump, JSONDecodeError
import os


class JSON:
    def __init__(self, data: dict):
        """
        :param data: приходит словарь, который успешно прошел валидацию, затем выполняется метод, указанный пользователем
        """
        self.filename = 'books.json'
        self.folder = 'data'
        self.path = os.path.join(self.folder, self.filename)
        self.data = data

    def load_file(self):
        with open(self.path, 'r') as file:
            json_data = load(file)
            file.close()
        return json_data

    def upload_data(self, json_data: dict):
        with open(self.path, 'w') as file:
            dump(json_data, file, ensure_ascii=False, indent=4)
            file.close()

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

    def add_data_to_json(self):
        json_data = self.start_json()
        json_data['books'].append(self.data)
        self.upload_data(json_data)

    def remove_data_from_json(self, book_id: int):
        json_data = self.start_json()

        def check_id():
            for index, book in enumerate(json_data['books']):
                if book['id'] == book_id:
                    json_data['books'].pop(index)
                    return True
                continue
            return False

        if not check_id():
            return False
        else:
            self.upload_data(json_data)
            return True

    def update_data_in_json(self, status: bool):
        json_data = self.start_json()


    def search_data_in_json(self):
        json_data = self.start_json()
        