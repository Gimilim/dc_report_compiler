import json

import pandas as pd

import calculations as calc


def cdek_get_report(file):
    # список заказов за сегодня
    today_list = []
    # список заказа со вчера
    yesterday_list = []
    # список заказов за последние 5 дней
    last_5_day_list = []
    # список всех осталбных заказов
    rest_list = []

    # Получаем нужный фрагмент таблицы.
    result_table = pd.read_excel(file, usecols='A:C', converters={1: int})
    # Преобразуем таблицу в список.
    pd_json = result_table.to_json(orient='split')
    # Преобразуем список в json (dict).
    parsed_json = json.loads(pd_json)
    # Получаем список строк таблицы с нужными данными.
    data_list = parsed_json.get('data')

    # Формируем списки заказов по дате (только те, где есть наш внутренний
    # номер).
    for element in data_list:
        if element[1] is not (None):
            match calc.string_to_date(element[2]):
                case calc.TimeLineStatus.today:
                    today_list.append(element[1])
                case calc.TimeLineStatus.yesterday:
                    yesterday_list.append(element[1])
                case calc.TimeLineStatus.five_day_ago:
                    last_5_day_list.append(element[1])
                case rest:
                    rest_list.append(element[1])
    result_list = (today_list, yesterday_list, last_5_day_list, rest_list)
    return(result_list)
