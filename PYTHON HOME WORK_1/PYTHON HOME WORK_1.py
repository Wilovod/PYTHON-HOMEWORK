# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)



a = int(input('Введите трехзначное число: '))
q = a // 100
w = a % 10
e = a % 100 // 10
sum = q + w + e
print(q, ' + ', w, ' + ', e, ' = ', q + w + e)


