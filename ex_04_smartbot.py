from random import randint


def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player_1 = input('Введите имя первого игрока: ')
player_2 = 'Бот_Валера'

value = int(input('Введите количество конфет: '))
flag = randint(0,2)
if flag:
    print(f'Ходит игрок {player_1}')
else:
    print(f'Ходит игрок {player_2}')

counter_1 = 0
counter_2 = 0
k = 0

while value > 28:
    if flag:
        k = input_dat(player_1)
        counter_1 += k
        value -= k
        flag = False
        p_print(player_1, k, counter_1, value)
    else:
        k = calc(value)
        counter_2 += k
        value -= k
        flag = True
        p_print(player_2, k, counter_2, value)

if flag:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл Бот_Валера")