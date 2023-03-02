'''Задание №1.
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
Ввод:

пара-ра-рам рам-пам-папам па-ра-па-да

Вывод:
Парам пам-пам'''





def str_counter_list(input_list, benchlist):
    count_list = [(sum(map(lambda item: 1 if item in benchlist else 0, part))) for part in input_list]
    return count_list

input_Pooh = input('Введите стих или нажмите Entrt: ') or 'пара-ра-рам рам-пам-папам па-ра-па-да'
list_Pooh = input_Pooh.split(' ')
vowels = ('а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е')


if len(set(str_counter_list(list_Pooh, vowels))) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')



