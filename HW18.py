# : Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны
# N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

N = abs(int(input('Введите количество элементов списка: ')))
My_number = input("Введите числа в сиписок : ").split()

if len(My_number) != N:
    print('Неправильное колличество элементов!')

else:
    X = int(input('Введите число X, которому необходимо найти самые близкие числа  в списке: '))
    min_from_X = abs(X-My_number[0])
    index = 0
    for i in range (1,N):
        count = abs(X-My_number[i])
        if count < min:
            min= count
            index = i
    max_from_X = abs(X + My_number[0])
    index = 0 
    for j in range (1,N):
        count = abs(X + My_number[j])
        if count > max:
            max= count
            index = j
            print(f'Cамые близкие числа к числу  {X}  {min_from_X}  {max_from_X} ')