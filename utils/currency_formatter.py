'''

'''


def currency_formatter(currencies):
    formatted_currencies = []
    for currency in currencies:
        short_currency_data = {
            "name": currency.get("name"),
            "symbol": currency.get("symbol"),
            "current_price": currency.get("current_price"),
            "market_cap": currency.get("market_cap")
        }
        formatted_currencies.append(short_currency_data)
    return formatted_currencies
