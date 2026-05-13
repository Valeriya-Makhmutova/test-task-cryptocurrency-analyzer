import argparse
import sys
from app.endpoints import get_crypto

def main():
    parser = argparse.ArgumentParser(
        description="Консольная утилита для анализа криптовалюты"
    )

    parser.add_argument(
        "-c", "--currency", 
        type=str, 
        default="usd", 
        help="Валюта сравнения (usd, eur, rub)"
    )

    parser.add_argument(
        "--limit", 
        type=int, 
        default=25, 
        help="Количество разных криптовалют в выгрузке (по умолчанию 25)"
    )

    args = parser.parse_args()
    data = get_crypto(args.currency, args.limit)
    # print('data: ', data)

    new_data = []
    for currency in data:
        short_curr_data = {
            "name": currency.get("name"),
            "symbol": currency.get("symbol"),
            "current_price": currency.get("current_price"),
            "market_cap": currency.get("market_cap")
        }
        new_data.append(short_curr_data)

    print(new_data)
# try:

# except *название исключения*:
if __name__ == '__main__':
    main()