import requests

def get_crypto(vs_currency, limit):
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

      return response.json()
    
    except ValueError:
      print('Problems with value')
    except Exception:
      print('Something going wrong')


