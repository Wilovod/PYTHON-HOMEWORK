# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5



array_length = int(input('Введите количество элементов массива: '))
arr = []
count = 0
for i in range(0, array_length):
    arr.append(i)
print(f'Массив {arr}')
num = int(input('Введите X: '))
for i in range(0, array_length):
    if num < 0:
        print('Вы ввели отрицательное число, нужно ввести натуральное число')
    elif arr[i] == num:
        print(f'Вы ввели число из массива, это {arr[i]}')
    elif arr[-1] < num:
        print(f'Вы ввели число которого нет в массиве и получается что самое близкое число это {arr[-1]}')
        break