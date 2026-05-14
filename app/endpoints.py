import requests
import sys
import traceback
from config import (
    COIN_GECKO_URL,
    ORDER_TYPE,
    PAGE_NUMBER
)
from requests.exceptions import RequestException

'''

'''


def get_crypto(vs_currency, currency_limit, market_cap_line):
    try:
        url = COIN_GECKO_URL

        params = {
            "vs_currency": vs_currency,
            "order": ORDER_TYPE,
            "per_page": currency_limit,
            "page": PAGE_NUMBER,
            "sparkline": False
        }

        response = requests.get(url, params=params)
        response.raise_for_status()  # защищаем себя от сетевых ошибок

        parsed_data = response.json()

        filtred_currencies = [
            currency
            for currency in parsed_data
            if currency["market_cap"] >= market_cap_line
        ]
        print('length of filtred data', len(filtred_currencies))
        return filtred_currencies

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
