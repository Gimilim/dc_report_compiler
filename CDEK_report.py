import json

import pandas as pd


class read_excel_report:
    def __init__(self, file_name, colomn, converters) -> None:
        self.file_name = file_name
        self.colomn = colomn
        self.converters = converters

    pass


def cdek_get_id_list(file_name: str) -> list:
    dc_id_list = []
    id_list = []

    # Получаем нужный фрагмент таблицы.
    result_table = pd.read_excel(
        file_name,
        usecols='A:B',
        converters={0: str, 1: (lambda x: str(x).replace(' ', ''))},
    )
    # Преобразуем таблицу в список.
    pd_json = result_table.to_json(orient='split')
    # Преобразуем список в json (dict).
    parsed_json = json.loads(pd_json)
    # Получаем список строк таблицы с нужными данными.
    data_list = parsed_json.get('data')

    # Формируем список ID из таблицы
    for element in data_list:
        if element[1] is not (None):
            dc_id_list.append(element[0])
            if '00ФР' not in element[1]:
                id_list.append(element[1])

    result_dict = {'dc_id_list': dc_id_list, 'id_list': id_list}

    return result_dict
