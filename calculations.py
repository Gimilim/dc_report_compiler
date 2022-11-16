import datetime as dt


def string_to_date(string: str) -> dt.date:
    """
    Преобразование даты из формата DD.MM.YYYY в экземпляр класса datetime.
    """
    year = int(string[6:])
    day = int(string[:2])
    month = int(string[3:5])
    formated_date = dt.date(year, month, day)
    return formated_date


def id_format(id: int, format: int) -> int:
    """
    Форматирование id убирая первые знаки id в количестве format.
    """
    if format == 0:
        return id
    str_id = str(id)
    formated_str = str_id[format:]
    result = int(formated_str)
    return result


def list_convertor(lst: list, format: int = 0) -> list:
    """
    Переводит список с int данными в список с str данными.
    """
    formated_list = []
    for element in lst:
        str_element = str(element)
        formated_element = str_element[format:]
        formated_list.append(formated_element)
    return formated_list


def list_to_str(lst: list) -> str:
    """
    Переводит список в строку, где каждый элемент в новой строчке.
    """
    result = '\n'.join(lst)
    return result


def get_text(lst: list, format: int = 0) -> str:
    """
    Получая на входе список возвращает текст с каждым элементом на новой
    строке.
    """

    str_list = list_convertor(lst, format)
    str_text = list_to_str(str_list)
    return str_text
