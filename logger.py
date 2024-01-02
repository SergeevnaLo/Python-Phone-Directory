from data_create import name_data, surname_data, phone_data, address_data

#Функция ввода данных пользователем
def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"Первый вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"Второй вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"
    f"Выберите вариант: "))
    
    # Проверка на неверный ввод
    while var != 1 and var !=2:
        print("Неверный ввод")
        command = int(input('Введите число '))
    
    # Запись введенных данных в файл №1 или №2 в зависимости от выбранного варианта
    if var == 1:
        with open('data.first.variant.csv','a', encoding='utf-8') as f:
            f.write(f"\n{name}\n{surname}\n{phone}\n{address}")

    elif var == 2:
        with open('data.second.variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"\n{name};{surname};{phone};{address}")


# Функция вывода данных из файлов
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data.first.variant.csv','r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) -1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
        
    print('Вывожу данные из 2 файла: \n')
    with open('data.second.variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

# Функция поиска и изменения данных     
def change_data():
    # Первый справочник
    with open('data.first.variant.csv', 'r+', encoding='utf-8') as f:
        data_change = f.readlines()
        print("Доступные для изменения данные из файла 'data.first.variant.csv' (введите 0 чтобы перейти к следующему файлу): ")
        
        for i, line in enumerate(data_change):
             print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно изменить: "))
        if selection>0 and selection<= len(data_change):
            new_data = input("Введите новые данные: ")
            data_change[selection-1] = new_data + '\n'
            f.seek(0)
            f.writelines(data_change)
            f.truncate()
            print("Данные успешно изменены!")
        elif selection == 0:
                print("Выход из файла.")
        else:
            print('Некорректный ввод данных')
    
    # Второй справочник
    with open('data.second.variant.csv', 'r+', encoding='utf-8') as f:
        data_change = f.readlines()
        print("Доступные для изменения данные из файла 'data.second.variant.csv' (введите 0 чтобы выйти):")
        
        for i, line in enumerate(data_change):
             print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно изменить: "))
        if selection>0 and selection<= len(data_change):
            new_data = input("Введите новые данные: ")
            data_change[selection-1] = new_data + '\n'
            f.seek(0)
            f.writelines(data_change)
            f.truncate()
            print("Данные успешно изменены!")
        elif selection == 0:
                print("Выход из файла и режима редактирования.")
        else:
            print('Некорректный ввод данных')

# Функция удаления данных
def delete_date():
     with open('data.first.variant.csv', 'r', encoding='utf-8') as f:
        data_delete = f.readlines()
        print("Доступные данные из файла 'data.first.variant.csv' (введите 0 чтобы перейти к следующему файлу): ")
        
        for i, line in enumerate(data_delete):
            print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно удалить: "))
    
        with open("data.first.variant.csv", "w", encoding="utf-8") as f:
            for i, line in enumerate(data_delete):
                if i+1 != selection:
                    f.write(line)

    
        with open("data.second.variant.csv", "r", encoding="utf-8") as f:
            data_delete = f.readlines()
        print("Доступные для удаления данные из файла 'data_second_variant.csv' (введите 0 чтобы выйти):")
        for i, line in enumerate(data_delete):
            print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно удалить: "))
        with open("data.second.variant.csv", "w", encoding="utf-8") as f:
            for i, line in enumerate(data_delete):
                if i+1 != selection:
                    f.write(line)

