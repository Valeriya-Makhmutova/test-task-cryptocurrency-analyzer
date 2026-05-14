'''
Функция, которая фильтрует валюты по
переданному значению рыночной капитализации (market_cap_line)

Примнимает спарсенные данные в виде списка валют
и значение для фильтрации.
'''


def market_capitalization_filter(parsed_data, market_cap_line):
    filtred_currencies = [
        currency
        for currency in parsed_data
        if currency["market_cap"] >= market_cap_line
    ]

    return filtred_currencies
