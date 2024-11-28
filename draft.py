from re import search

# asd = input('Введите что-нибудь')
# print(type(asd))


def main_1():
    return ValueError('Привет')


def main_2():
    return ValueError('Пока')


def main_3():
    return ValueError('Как дела?')


funcs = [main_1, main_2, main_3]
for i in funcs:
    a = i()
    if type(a) is ValueError:
        print(main_1())
    else:
        print('Привет')

