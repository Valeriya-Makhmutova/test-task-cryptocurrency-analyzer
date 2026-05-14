'''
Функция, которая создает Excel файл,
записывает данные в таблицу и форматирует её.

Принимает в качестве аргумента - список готовых строк.

Столбцы таблицы формируются в frame_data,
здесь можно добавить или удалить столбец
'''

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from config import TABLE_HEAD_COLOR_CODE


def create_xlsx_file(lines_list):
    frame_data = pd.DataFrame({
        "Name": lines_list["name"],
        "Symbol": lines_list["symbol"],
        "Price": lines_list["current_price"],
        "Market Capitalization": lines_list["market_cap"],
    })

    frame_data.to_excel('output.xlsx', index=True)

    work_book = load_workbook('output.xlsx')
    work_sheet = work_book.active

    green_fill = PatternFill(
        start_color=TABLE_HEAD_COLOR_CODE,
        end_color=TABLE_HEAD_COLOR_CODE,
        fill_type="solid"
    )
    bold_font = Font(bold=True)
    # окрашиваем шапку таблицы
    for cell in work_sheet[1]:
        cell.fill = green_fill
        cell.font = bold_font
    # настраиваем автоотступы
    for col in work_sheet.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = col[0].column_letter
        work_sheet.column_dimensions[col_letter].width = max_len + 3
    # настраиваем отображение тысяч в числе
    with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
        frame_data.to_excel(writer, index=True)

        numbers_format = '#,##0'

        for row in range(2, work_sheet.max_row + 1):
            work_sheet[f'D{row}'].number_format = numbers_format
            work_sheet[f'E{row}'].number_format = numbers_format

    work_book.save('output.xlsx')
