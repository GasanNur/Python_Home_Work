# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 1 числа. n — кол-во элементов первого
# множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint
first_set = set(randint(1, 15) for i in range (int(input('Введите колличество элементов первого списка: '))))
print(first_set)
second_set= set(randint(1,15) for i in range (int(input('Введите количество элементов второго списка: '))))
print(second_set)
simlar_set = sorted(first_set.intersection(second_set))
print(simlar_set)

