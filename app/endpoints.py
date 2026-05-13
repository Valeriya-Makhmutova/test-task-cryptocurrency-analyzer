import requests

def get_crypto(vs_currency, limit, market_cap_line):
    url = 'https://api.coingecko.com/api/v3/coins/markets'

    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }

    try:
      response = requests.get(url, params=params)
      response.raise_for_status() # защищаем себя от сетевых ошибок

    #   print('response: ', response.json())
      parsed_data = response.json()
      filtred_currencies = [ currency for currency in parsed_data if currency["market_cap"] >= market_cap_line]
      print('length of filtred data', len(filtred_currencies))
      return filtred_currencies
    
    except ValueError:
      print('Problems with value')
    except Exception:
      print('Something going wrong')


