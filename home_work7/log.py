import datetime


def logging(data):
    with open('log.xls', 'a') as file:
        file.write(f'Внесены данные: {data}. Дата и время ввода: '
                   f'{datetime.datetime.today().strftime(" %Y.%m.%d   %H:%M:%S")}\n')


def log_find(item):
    with open('log.xls', 'a') as file:
        file.write(f'Результат поискового запроса: {item}. Дата и время запроса: '
                   f'{datetime.datetime.today().strftime(" %Y.%m.%d   %H:%M:%S")}\n')


def log_output(item):
    with open('log.xls', 'a') as file:
        file.write(f'Телефонный справочник выведен в консоль. Дата и время вывода: '
                   f'{datetime.datetime.today().strftime(" %Y.%m.%d   %H:%M:%S")}\n')

