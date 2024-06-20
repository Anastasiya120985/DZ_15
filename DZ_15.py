# Напишите информационную систему «Сотрудники». Программа должна обеспечивать ввод данных, редактирование данных
# сотрудника, удаление сотрудника, поиск сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного
# возраста, или фамилия которых начинается на указанную букву. Организуйте возможность сохранения найденной информации
# в файл. Также весь список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе
# исполнения программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

import json

def read_data(file_name):
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            data = json.loads(file.read())
        return data
    except FileNotFoundError:
        return []

def save_data(file_name, data):
    with open(file_name, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

def get_staffer(data):
    surname = input('Введите фамилию сотрудника: ')
    name = input('Введите имя сотрудника: ')
    age = int(input('Введите возраст сотрудника: '))
    staffer = {'surname': surname, 'name': name, 'age': age}
    data.append(staffer)
    print(f'Сотрудник {surname} успешно добавлен! \n')

def edit_staffer(data):
    surname = input('Введите фамилию сотрудника для редактирования: ')
    search = False
    for staffer in data:
        if staffer['surname'] == surname:
            staffer['surname'] = input('Введите новую фамилию сотрудника: ')
            staffer['name'] = input('Введите новое имя сотрудника: ')
            staffer['age'] = int(input('Введите новый возраст сотрудника: '))
            print(f'Данные сотрудника {surname} успешно обновлены! \n')
            search = True
    if not search:
        print(f'Сотрудник с фамилией {surname} не найден! \n')

def del_staffer(data):
    surname = input('Введите фамилию сотрудника для удаления: ')
    search = False
    for staffer in data:
        if staffer['surname'] == surname:
            data.remove(staffer)
            print(f'Сотрудник {surname} успешно удален! \n')
            search = True
    if not search:
        print(f'Сотрудник с фамилией {surname} не найден! \n')

def search_surname(data):
    surname = input('Введите фамилию сотрудника для поиска: ')
    select_staffer = [staffer for staffer in data if staffer['surname'] == surname]
    if select_staffer:
        print('Найденные сотрудники:')
        for staffer in select_staffer:
            print(f"{staffer['surname']} {staffer['name']}, {staffer['age']} лет")
        print('\n')
    else:
        print(f'Сотрудник с фамилией {surname} не найден! \n')

def search_age(data):
    age = int(input('Введите возраст для поиска сотрудников: '))
    select_staffer = [staffer for staffer in data if staffer['age'] == age]
    if select_staffer:
        print(f'Найденные сотрудники в возрасте {age}:')
        for staffer in select_staffer:
            print(f"{staffer['surname']} {staffer['name']}")
        print('\n')
    else:
        print(f'Сотрудники в возрасте {age} не найдены! \n')

def search_letter(data):
    letter = input('Введите букву для поиска сотрудников с фамилией, начинающейся на нее: ')
    select_staffer = [staffer for staffer in data if staffer['surname'].startswith(letter)]
    if select_staffer:
        print(f'Найденные сотрудники с фамилией на букву - {letter.upper()}:')
        for staffer in select_staffer:
            print(f"{staffer['surname']} {staffer['name']}, {staffer['age']} лет")
        print('\n')
    else:
        print(f'Сотрудники с фамилией на букву {letter.upper()} не найдены! \n')

def main():
    file_name = input('Введите путь и имя файла с данными сотрудников: ')
    #'staffers.json'
    staffers_data = read_data(file_name)

    while True:
        print('1. Добавление сотрудника')
        print('2. Редактирование сотрудника')
        print('3. Удаление сотрудника')
        print('4. Поиск сотрудника по фамилии')
        print('5. Вывод информации обо всех сотрудниках, указанного возраста')
        print('6. Вывод информации обо всех сотрудниках, фамилия которых начинается на указанную букву')
        print('7. Сохранение данных')
        print('8. Выход')

        choice = input('Выберите пункт меню "Сотрудники": ')
        if choice == '1':
            get_staffer(staffers_data)
        elif choice == '2':
            edit_staffer(staffers_data)
        elif choice == '3':
            del_staffer(staffers_data)
        elif choice == '4':
            search_surname(staffers_data)
        elif choice == '5':
            search_age(staffers_data)
        elif choice == '6':
            search_letter(staffers_data)
        elif choice == '7':
            save_data(file_name, staffers_data)
            print('Данные успешно сохранены!  \n')
        elif choice == '8':
            save_data(file_name, staffers_data)
            print('Данные успешно сохранены! Выход из программы!  \n')
            break
        else:
            print('Неверный пункт меню! \n')

if __name__ == '__main__':
    main()