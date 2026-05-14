'''
Модуль для парсинга и фильтрации криптовалютных данных.

Запрашивает информацию о валютах через CoinGecko API и фильтрует
их по минимальной рыночной капитализации.

Принимает аргументы, полученые с помощью командной строки
или значения по умолчанию: 
    лимит валют на странице (currency_limit),
    пороговое значение капитализации рынка валюты (market_cap_line) 
'''

import requests
import sys
import traceback
from config import (
    COIN_GECKO_URL,
    ORDER_TYPE,
    PAGE_NUMBER,
    VS_CURRENCY
)
from requests.exceptions import RequestException
from utils.market_cap_filtration import market_capitalization_filter


def get_crypto(currency_limit, market_cap_line):
    try:
        url = COIN_GECKO_URL

        params = {
            "vs_currency": VS_CURRENCY,
            "order": ORDER_TYPE,
            "per_page": currency_limit,
            "page": PAGE_NUMBER,
            "sparkline": False
        }

        response = requests.get(url, params=params)
        response.raise_for_status()  # защищаем себя от сетевых ошибок

        parsed_data = response.json()
        
        return market_capitalization_filter(parsed_data, market_cap_line)

    except RequestException as req_exc:
        print(f"Request error: {req_exc}")
    except ValueError:
        print('Problems with value')
    except KeyError:
        print('Problems with keys in dictionary')
    except Exception as excp:
        print("Error in endpoints module\n")
        print(f"Error description: {excp}\n")
        traceback.print_exc()
        sys.exit(1)
