from log import logging


def input_data():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    brithday = input('Введите дату рождения: ')
    contact_number = input('Введите номер контакта: ')
    return [last_name, first_name, second_name, brithday, contact_number]


def write_data(data, sep=None):
    # print(type(data))
    # print(data)
    with open('phone_guide.txt', 'a+') as f:
        f.write(sep.join(data))
        f.write(f'\n')
        logging(data)


def export_data():
    with open('phone_guide.txt', 'r') as f:
        data = []
        for el in f:
            temp = el.strip().split(',')
            data.append(temp)
    return data
