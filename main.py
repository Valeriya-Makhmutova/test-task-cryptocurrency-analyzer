import sys
import traceback
from utils.get_arguments_cli import get_arguments_cli
from app.endpoints import get_crypto
from utils.currency_formatter import currency_formatter
from utils.get_lines_list import get_lines_list
from utils.export_xlsx_file import create_xlsx_file

'''


'''


def main():
    try:
        # инициализация аргументов
        arguments = get_arguments_cli()
        # получение данных из GET запроса к API
        currencies_data = get_crypto(
            arguments.currency,
            arguments.limit,
            arguments.marketCapLine
        )
        # оставляем только интересующие нас свойства
        formatted_currencies = currency_formatter(currencies_data)
        # стобцы, которые мы хотим увидеть в таблице
        currencies_params_keys = [
            "name",
            "symbol",
            "current_price",
            "market_cap"
        ]
        # строки по столбцам
        lines_list = get_lines_list(
            formatted_currencies,
            currencies_params_keys
        )
        # создаем и форматируем excel file
        create_xlsx_file(lines_list)

    except Exception as excp:
        print("Error in main module\n")
        print(f"Error description: {excp}\n")
        traceback.print_exc()
        sys.exit(1)
    else:
        print("Данные успешно сохранены в файл 'output.xlsx'")


if __name__ == '__main__':
    main()
