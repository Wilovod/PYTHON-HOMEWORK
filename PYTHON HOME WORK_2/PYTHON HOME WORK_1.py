# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0


lists = []
boxOne = 0
boxZero = 0
money = int(input('Введите количество монеток: '))
for i in range (money):
    lists.append(int(input('Bвeдите сторону, 1 - "орeл", 0 - "peшкa": ')))
print(lists)
for i in lists:
    if i > 0:
        boxOne += 1
    else:
        boxZero += 1
if boxOne < boxZero:
    print(f'Нужно перевернуть {boxOne} монеты решкой вверх')
elif boxOne == boxZero:
    print(f'Нужно перевернуть {boxOne} монеты решкой или {boxZero} монеты орлом вверх')
else:
    print(f'Нужно перевернуть {boxZero} монеты орлом вверх')
