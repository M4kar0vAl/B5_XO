player1 = input('Игрок 1, представьтесь: ')
player2 = input('Игрок 2, представьтесь: ')

from random import randint

choice = randint(1, 2)
chosen = player1 if choice == 1 else player2
other = player2 if chosen == player1 else player1
print('')
print(f'По случайному стечению обстоятельств {chosen} выбирает символ')
print('')
chosen_symbol = input(f'{chosen}, ваш выбор: ')
other_symbol = None
first_move_symbol = None
second_move_symbol = None
while True:
    if chosen_symbol in 'XxХх' and len(chosen_symbol) == 1:  # буквы латиницы и кириллицы
        other_symbol = 'O'
        first_move_symbol = chosen_symbol
        second_move_symbol = other_symbol
        first_move = chosen
        second_move = other
        break
    elif chosen_symbol in 'OoОо0' and len(chosen_symbol) == 1:  # буквы латиницы и кириллицы и ноль
        other_symbol = 'X'
        first_move_symbol = other_symbol
        second_move_symbol = chosen_symbol
        first_move = other
        second_move = chosen
        break
    else:
        print('Мы играем в КРЕСТИКИ-НОЛИКИ')
        chosen_symbol = input('Выберите соответствующий символ:')
print(f'Тогда {other} играет за {other_symbol}')
print('')
print(f'Первый ход за {first_move}')
print('')


def is_coord_correct(func):
    """Проверяет корректность введенных координат и возвращает строку вида 'буква + цифра'"""

    def wrapper():
        numbers = None
        letters = None
        while True:
            coords = func()
            if coords.isdigit() or coords.isalpha():  # если оба символа цифры или оба буквы
                print('Координаты введены неверно')
                continue
            elif coords.isalnum():  # если цифры и буквы
                if all([coords[0].isdigit(), coords[0] in [str(i) for i in range(1, 4)], coords[1] in 'abc',
                        len(coords) == 2]):
                    numbers = coords[0]
                    letters = coords[1]
                    break
                elif all([coords[1].isdigit(), coords[1] in [str(i) for i in range(1, 4)], coords[0] in 'abc',
                          len(coords) == 2]):
                    numbers = coords[1]
                    letters = coords[0]
                    break
                else:
                    print('Координаты введены неверно')
                    continue
        return letters + numbers

    return wrapper


def is_position_empty(func):
    """Проверяет занята ли позиция другим символом.
    Если позиция свободна присваивает ей символ.
    Если позиция занята сообщает об этом и запрашивает новые координаты.
    Возвращает игровое поле"""

    def wrapper():
        while True:
            coords = func()
            coords = [int(i) for i in coords.translate(coords.maketrans('abc', '123'))]
            if battlefield[coords[0] - 1][coords[1] - 1] == '_':
                battlefield[coords[0] - 1][coords[1] - 1] = symbol
                break
            else:
                coords = ''.join(list(map(str, coords)))
                coords = coords[0].translate(coords[0].maketrans('123', 'abc')) + coords[1]
                print(f'Координаты {coords} уже заняты')
        return battlefield

    return wrapper


@is_position_empty
@is_coord_correct
def ask_coords():
    coords = input('Введите координаты: ').lower()
    coords = ''.join([i for i in coords if i.isalpha()] + [i for i in coords if i.isdigit()])
    return coords


move_count = 1
battlefield = [['_', '_', '_'],
               ['_', '_', '_'],
               ['_', '_', '_']]


def print_battlefield():
    letters = 'abc'
    print(f"{''.join([f'{row + 1:>5}' for row in range(len(battlefield))])}")
    for row in range(len(battlefield)):
        print(f"{letters[row]}{' ':<3}{battlefield[row][0]}{' ':<4}{battlefield[row][1]}{' ':<4}{battlefield[row][2]}")


print_battlefield()
import numpy as np

while True:
    if move_count % 2 == 1:
        symbol = first_move_symbol
        print('')
        print(f'Сейчас ходит: {first_move}')
    else:
        symbol = second_move_symbol
        print('')
        print(f'Сейчас ходит: {second_move}')
    print('')
    ask_coords()
    print('')
    print_battlefield()
    if any([all([el == symbol for el in row]) for row in battlefield]) \
            or any([all([el == symbol for el in col]) for col in np.transpose(battlefield)]) \
            or all([el == symbol for el in np.diagonal(battlefield)]) \
            or all([el == symbol for el in np.fliplr(battlefield).diagonal()]):
        if symbol == first_move_symbol:
            print(f'{first_move} побеждает!')
            break
        if symbol == second_move_symbol:
            print(f'{second_move} побеждает!')
            break
    elif move_count == 9:
        print('Ничья!')
        break
    move_count += 1
