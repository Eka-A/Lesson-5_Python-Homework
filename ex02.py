#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

from random import randint


def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')

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
        k = input_dat(player_2)
        counter_2 += k
        value -= k
        flag = True
        p_print(player_2, k, counter_2, value)

if flag:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл {player_2}")
