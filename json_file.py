from json import load, dump, JSONDecodeError


class JSON:
    def __init__(self, data: dict):
        """
        :param data: приходит словарь, который успешно прошел валидацию, затем выполняется метод, указанный пользователем
        """
        self.filename = 'books.json'
        self.data = data

    def check_json_files(self) -> bool:
        try:
            open(self.filename)
            return True
        except FileNotFoundError:
            initial_data = {'books': []}
            with open(self.filename, 'w') as file:
                dump(initial_data, file)
            return False

    def add_data_json(self) -> bool:
        try:
            with open(self.filename, 'r') as file:
                json_data = load(file)
                file.close()
            json_data['books'].append(self.data)
            with open(self.filename, 'w') as f:
                dump(json_data, f, ensure_ascii=False, indent=4)
                file.close()
            return True
        except JSONDecodeError:
            return False

    def remove_data_from_json(self):
        pass

    def update_data_in_json(self):
        pass
