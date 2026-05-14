'''
Функция, которая создает список строк для таблицы.

Примнимает список с данными о валютах
и список с названиями столбцов.

'''


def get_lines_list(currencies_list, currencies_params_keys):
    lines_dictionary = {}

    for key in currencies_params_keys:
        lines_dictionary[key] = [currency[key] for currency in currencies_list]

    return lines_dictionary
