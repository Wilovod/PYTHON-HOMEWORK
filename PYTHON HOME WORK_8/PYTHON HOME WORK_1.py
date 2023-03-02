'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной
5. Добавить контакт
1. Чтение
2. Поиск
3. Добавить
4. Сохранить

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
5. Редактировать
6. Удалить
'''




import os



contacts_file = r'PYTHON HOME WORK_8\contacts.txt'


def append_contact(contacts_file):
    contact = input('Введите контакт в формате Ф И О Телефон: ')
    with open(contacts_file, 'a', encoding="utf-8") as f:
        f.write(f'\n{contact}')
    print ('Контакт добавлен')

def read_file(contacts_file):
    with open(contacts_file, 'r', encoding="utf-8") as f:
        print (f.read())

def search_contact(contacts_file):
    search_by = input("Введите информацию для поиска (фамилия, имя или отчество): ")
    with open(contacts_file, 'r', encoding="utf-8") as f:
        for line in f:
            if search_by in line:
                # print(line)
                return str(line) #Нашли по имени или фамилии


def remove_contact(contacts_file):
    print('Для удаления контакта: ')
    card = search_contact(contacts_file) # Просим оператора ввести Ф или И, чтобы найти карточку контакта
    del_cont = (input(f'Вы хотите удалить контакт \n {card} \n 1 - ДА \n 2 - НЕТ\n')) #Просим подтвердить удаление контакта
    if del_cont == '1':
        with open(contacts_file, 'r', encoding="utf-8") as f: #Открываем всю книгу
                all = f.readlines() #Преобразуем всю книжку с список (каждую строку в отдельный элемент списка)
        for i in range(len(all)-1): #Проходимся по списку
            if  card == all[i]: # сравниваем найденный контакт с каждым элементом списка
                all.pop(i) #и удаляем его из списка
        cont_2 = ''.join(all) #Преобразуем список обратно в строки
        with open(contacts_file, 'w', encoding="utf-8") as f: # Перезаписываем всю книгу без удалённого контакта
            f.write(f'{cont_2}')
            print ('Контакт удалён')

def change_contact(contacts_file):
    print('Для изменения контакта: ')
    card = search_contact(contacts_file) # Просим оператора ввести Ф или И, чтобы найти карточку контакта
    del_cont = (input(f'Вы хотите изменить контакт \n {card} \n 1 - ДА \n 2 - НЕТ\n')) #Просим подтвердить удаление контакта
    if del_cont == '1':
        with open(contacts_file, 'r', encoding="utf-8") as f: #Открываем всю книгу
                all = f.readlines() #Преобразуем всю книжку с список (каждую строку в отдельный элемент списка)
        for i in range(len(all)-1): #Проходимся по списку
            if  card == all[i]: # сравниваем найденный контакт с каждым элементом списка
                new_contact = (str(input("Введите новые данные контакта: ")+'\n')) #Просим ввести новые данные контакта
                all[i] = new_contact# и присваиваем
        cont_2 = ''.join(all) #Преобразуем список обратно в строки
        with open(contacts_file, 'w', encoding="utf-8") as f: # Перезаписываем всю книгу с изменённым контактом
            f.write(f'{cont_2}')
            print ('Контакт изменён')

def user_action():
    print ('Добро пожаловать! \n'
    '1) Вывести весь справочник\n'
    '2) Добавить контакт \n'
    '3) Найти контакт\n'
    '4) Найти и удалить контакт\n'
    '5) Найти и изменить контакт\n')
    while (input1:= int(input('Выберите действие со справочником (0 = выход): '))) != 0:
        if input1 == 1:
            read_file(contacts_file)
        elif input1 == 2:
            append_contact(contacts_file)
        elif input1 == 3:
            print(search_contact(contacts_file))
        elif input1 == 4:
            remove_contact(contacts_file)
        elif input1 == 5:
            change_contact(contacts_file)
        else:
            print("Некорректный ввод")

user_action()
