import json

import pandas as pd


class read_excel_report:
    def __init__(self, file_name: str, colomn: str, converters: dict) -> None:
        self.file_name = file_name
        self.colomn = colomn
        self.converters = converters

    def get_file_data(self) -> dict:
        """
        Возвращает словарь с внутренними ID и с трек-номерами ТК.
        """
        id_list = []
        track_id_list = []

        result_table = pd.read_excel(
            self.file_name,
            usecols=self.colomn,
            converters=self.converters,
        )

        # Преобразуем таблицу в json.
        pd_json = result_table.to_json(orient='split')
        # Преобразуем список в dict.
        parsed_json = json.loads(pd_json)
        # Получаем список строк таблицы с нужными данными.
        data_list = parsed_json.get('data')

        # Формируем список ID из таблицы
        for element in data_list:
            if element[1] is not (None):
                track_id_list.append(element[0])
                if '00ФР' not in element[1]:
                    id_list.append(element[1])

        result = {'id_list': id_list, 'track_id_list': track_id_list}
        return result


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
    # Преобразуем список в dict.
    parsed_json = json.loads(pd_json)
    # Получаем список строк таблицы с нужными данными.
    data_list = parsed_json.get('data')

    # Формируем список ID из таблицы
    for element in data_list:
        if element[1] is not (None):
            dc_id_list.append(element[0])
            if '00ФР' not in element[1]:
                id_list.append(element[1])

    result_dict = {'track_id_list': dc_id_list, 'id_list': id_list}

    return result_dict


if __name__ == '__main__':

    cdek_file_name = 'CDEK Orders Report 2022-11-22 11_08_54_1.xlsx'
    cdek_colomn = 'A:B'
    cdek_converters = {
        'Номер заказа': str,
        'Номер отправления ИМ': (lambda x: str(x).replace(' ', '')),
    }
    cdek = read_excel_report(cdek_file_name, cdek_colomn, cdek_converters)

    # print(cdek.get_file_data())

    boxberry_file_name = 'parcel_export_637f625539516.xlsx'
    boxberry_colomn = 'A,C'
    boxberry_converters = {
        'Код для слежения': str,
        'Номер заказа': (lambda x: str(x).replace(' ', '').replace('-1', '')),
    }
    boxberry = read_excel_report(
        boxberry_file_name, boxberry_colomn, boxberry_converters
    )
    print(boxberry.get_file_data())

    # Изучить пример и переписать replace.

    # # Функция для замены нескольких значений
    # def multiple_replace(target_str, replace_values):
    #     # получаем заменяемое: подставляемое из словаря в цикле
    #     for i, j in replace_values.items():
    #         # меняем все target_str на подставляемое
    #         target_str = target_str.replace(i, j)
    #     return target_str

    # # создаем словарь со значениями и строку, которую будет изменять
    # replace_values = {"кот": "кошка", "кошка": "собака"}
    # my_str = "У меня есть кот и кошка"

    # # изменяем и печатаем строку
    # my_str = multiple_replace(my_str, replace_values)
    # print(my_str)

    # Источник https://all-python.ru/osnovy/replace.html
