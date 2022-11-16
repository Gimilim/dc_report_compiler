import json

import pandas as pd


def cdek_get_id_list(file):
    result_list = []

    # Получаем нужный фрагмент таблицы.
    result_table = pd.read_excel(file, usecols='A:C', converters={1: int})
    # Преобразуем таблицу в список.
    pd_json = result_table.to_json(orient='split')
    # Преобразуем список в json (dict).
    parsed_json = json.loads(pd_json)
    # Получаем список строк таблицы с нужными данными.
    data_list = parsed_json.get('data')

    # Формируем список ID из таблицы
    for element in data_list:
        if element[1] is not (None):
            result_list.append(element[1])
    return result_list
