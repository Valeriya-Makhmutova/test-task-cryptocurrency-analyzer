'''
Функция, которая обрабатывает аргументы из консоли
при запуске приложенрия. 

Подставлят значения по умолчанию из файла config.py,
если аргументы не были переданы.
'''

import argparse
from config import (
    DEFAULT_VS_CURRENCY,
    DEFAULT_CURRENCIES_PER_PAGE,
    DEFAULT_MARKET_CAP_LINE
)


def get_arguments_cli():
    parser = argparse.ArgumentParser(
        description="Консольная утилита для анализа криптовалюты"
    )

    parser.add_argument(
        "-c", "--currency",
        type=str,
        default=DEFAULT_VS_CURRENCY,
        help="Валюта сравнения (usd, eur, rub)"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_CURRENCIES_PER_PAGE,
        help="Количество разных криптовалют в выгрузке (по умолчанию 25)"
    )

    parser.add_argument(
        "--marketCapLine",
        type=int,
        default=DEFAULT_MARKET_CAP_LINE,
        help="Пороговое значение капитализации рынка"
    )

    return parser.parse_args()
