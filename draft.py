import time
from re import search
import json
import os

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

name = 'books.json'


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


with open(name, 'w+') as file:
    data = json.load(file)
    new_data = data['books'].append({'a': 'a'})
    json.dump(new_data, file, ensure_ascii=False, indent=4)
    file.close()

# name = json.dumps(data)

