# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

number_first = int(input('Введите первое число: '))
number_second = int(input('Введите второе число: '))
def rec_degree(number_first, number_second):
    if number_second == 0:
        return 1
    return number_first + number_second

print(rec_degree(number_first, number_second))