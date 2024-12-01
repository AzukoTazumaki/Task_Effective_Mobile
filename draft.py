import time
from re import search
import json
import os
from random import randint

# asd = input('Введите что-нибудь')
# print(type(asd))


# def main_1():
#     return ValueError('Привет')
#
#
# def main_2():
#     return ValueError('Пока')
#
#
# def main_3():
#     return ValueError('Как дела?')
#
#
# funcs = [main_1, main_2, main_3]
# for i in funcs:
#     a = i()
#     if type(a) is ValueError:
#         print(main_1())
#     else:
#         print('Привет')

# open('books.json', 'w')

# name = 'books.json'


# def check_json_files():
#     try:
#         open(name)
#         return True
#     except FileNotFoundError:
#         return False
#
#
# def add_data_json():
#     data = {'books': []}
#     with open(name, 'a') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#
#
# add_data_json

# new_data = {'books': []}
# with open(name, 'w') as file:
#     json.dump(new_data, file, ensure_ascii=False, indent=4)


# with open(name, 'w+') as file:
#     data = json.load(file)
#     new_data = data['books'].append({'a': 'a'})
#     json.dump(new_data, file, ensure_ascii=False, indent=4)
#     file.close()

# name = json.dumps(data)


#def remove_data_from_json():
#   name = 'example.json'
#   with open(name) as file:
#       loaded = json.load(file)
#   print(loaded)
#   
#   
#remove_data_from_json()


class Draft:
    var: dict
    
    def __init__(self, title: str, author: str, year: int):
        self.book_id: int = int(randint(1, 1000000) * 0.8 + randint(1, 1000000) * 0.4)
        self.title = title
        self.author = author
        self.year = year
        self.status = True
    

a = Draft(title='Пособие по Hello, world!', author='Azuko', year=2024)


def check_id(loaded_data: dict, book_id: int) -> int | ValueError:
    for index, book in enumerate(loaded_data['books']):
        if book['id'] == book_id:
            loaded_data['books'].pop(index)
            return True
        continue
    return False


def remove_data(book_id: int):
    folder = 'data'
    file_name = 'example.json'
    path = os.path.join(folder, file_name)
    with open(path, 'r') as file:
        loaded = json.load(file)
        file.close()
    check = check_id(loaded, book_id)
    if not check:
        raise ValueError('Книги с таким ID нет в списке.')
    else:
        with open(path, 'w') as file:
            print(type(loaded))
            json.dump(loaded, file, ensure_ascii=False, indent=4)
            print(f'Книга с идентификатором {book_id} удалена')
        
        
if __name__ == "__main__":
    user_id = input('Введите ID книги, которую хотите удалить:\n>>>  ')
    remove_data(user_id)
