# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень
# B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# import random
# random = random.randint(1, 100)


number_first = int(input('Введите первое число: '))
number_degree = int(input('Введите второе число: '))
def rec_degree(number_first, number_degree):
    if number_degree == 0:
        return 1
    return number_first* rec_degree (number_first, number_degree-1)


print(rec_degree(number_first, number_degree))

