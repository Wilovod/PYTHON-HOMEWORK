# Задача 1.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1



# n = int(input('Введите количество элементов массива: '))
# print('Введите элементы массива: ')
# lst = [int(input()) for i in range(n)]
# conunt = lst.count(int(input('Определить сколько раз повторялось число: ')))
# print(conunt)



# import random

# n = int(input('Введите количество элементов в массиве: '))
# list = [random.randint(1, 5) for i in range(n)]
# print(list)
# lastElementNumber = len(list) - 1
# lastElement = list[lastElementNumber]
# print(f"Последний элемент массива = {lastElement}")
# result = list.count(lastElement)
# print(f"Число {lastElement} встречается в массиве {result} раз")


import random

array_length = int(input('Введите количество элементов в массиве: '))
arr = []
count = 0
for i in range(0, array_length):
    arr.append(random.randint(1, 10))
print(f'Массив {arr}')
num2 = int(input('Какое число нужно посчитать? '))
for i in range(0, array_length):
    if arr[i] == num2:
        count += 1
print(f'Число {num2} встречается {count} раз')

