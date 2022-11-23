def list_convertor(lst: list, format: int = 0) -> list:
    """
    Переводит str список в отформатированный список со срезом format.
    """
    formated_list = []
    if format == 0:

        return lst
    else:
        for element in lst:
            formated_element = element[format:]
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
    Получая на входе список возвращает отформатированный текст с каждым
    элементом на новой строке.
    """

    str_list = list_convertor(lst, format)
    str_text = list_to_str(str_list)

    return str_text
