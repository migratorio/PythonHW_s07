from data_enter import input_data, write_data, export_data
from data_output import output_data
from data_find import find_data
from log import log_find, log_output


def instruction():
    print("ТЕЛЕФОННЫЙ СПРАВОЧНИК\n\
    1 - Ввести данные\n\
    2 - Вывести список контактов \n\
    3 - Найти контакт")
    option = input("Выберите операцию: ")
    options(option)


def options(option):
    if option == '1':
        write_data(input_data(), ',')
        z = input('Продолжить ввод? (д/н)')
        if z == 'д':
            options(option)
        else:
            exit()
    elif option == '2':
        data = export_data()
        log_output(None)
        output_data(data)
    else:
        f_d = input("Введите данные для поиска: ")
        data = export_data()
        item = find_data(f_d, data)
        print('проверка', item)
        log_find(item)

        if item is not None:
            for i in range(0, 5):
                print(item[i].ljust(15), end='')

        else:
            print("Контакт с такими данными не найден!")
