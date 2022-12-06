import datetime as dt
import fnmatch
import json
import os
import sys

import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow

import calculations as calc
import CDEK_report as cd
from design11 import Ui_MainWindow

ID_LENGTH = 8


class MainProgram(QMainWindow):
    @staticmethod
    def get_file_date(file_name) -> dt:
        """
        Функция получает дату создания отчета по имени файла.
        """
        file_name_list = file_name.replace(".xlsx", "").split(" ")

        date_time_str = file_name_list[-2:]
        date_str = date_time_str[0]
        time_str = ":".join(date_time_str[1].split("_")[:3])
        file_date = dt.datetime.strptime(
            f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S"
        )

        return file_date

    @staticmethod
    def list_difference(lst1: list, lst2: list) -> list:
        """
        Считает разницу между двумя списками с неповторяющимися элементами.
        """
        set1 = set(lst1)
        set2 = set(lst2)
        result_set = set1 - set2
        result_list = list(result_set)

        return result_list

    @staticmethod
    def get_file_data(file_name: str) -> dict:
        """
        Функция для чтения файлов, где первой строчкой идет дата, затем в
        каждой строчке внутренние ID, а после трек номера в ТК. Возвращает
        результат ввиде словаря с ключами 'date', 'id_list', 'track_id_list'
        соответственно.
        """
        date_format = '%d.%m.%Y %H:%M:%S'
        with open(file_name, 'r') as opened_file:
            id_list = []
            track_id_list = []
            for line in opened_file:
                line = line.rstrip('\n')
                try:
                    int(line)
                    if len(line) == ID_LENGTH:
                        id_list.append(line)
                    else:
                        track_id_list.append(line)

                except Exception:
                    date_from_file = dt.datetime.strptime(line, date_format)
                    continue
        result = {
            'date': date_from_file,
            'id_list': id_list,
            'track_id_list': track_id_list,
        }
        return result

    @staticmethod
    def update_report_file(file_name: str, text_date: str, text: str) -> None:
        """
        Функция для записи в первую строчку файла даты, а далее построчно ID.
        """
        with open(file_name, 'w') as opened_file:
            opened_file.write(f'{text_date}\n')
            opened_file.write(text)
        return None

    def __init__(self):
        super(MainProgram, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.le_uploaded = self.ui.le_uploaded
        self.le_repeats = self.ui.le_repeats
        self.le_result = self.ui.le_result
        self.le_track_id = self.ui.le_track_id

        self.pe_uploaded = self.ui.pe_uploaded
        self.pe_repeats = self.ui.pe_repeats
        self.pe_result = self.ui.pe_result
        self.pe_track_id = self.ui.pe_track_id

        # Папка с excel отчетами.
        self.dir = '.'

        # Заполняем часть полей при запуске.
        self.first_load_setup()

    def load_file(self) -> None:
        """
        Функция обработки загрузки файла.
        """
        # Считываем выбранный файл из cb_file.
        selected_file = self.ui.cb_file.currentText()

        # Получаем весь список ID из эксель таблицы.
        dc_data_dict = cd.cdek_get_id_list(selected_file)
        excel_id_list = dc_data_dict.get('id_list')
        excel_dc_id_list = dc_data_dict.get('dc_id_list')

        # Заполняем дату отчета.
        excel_report_date = self.get_file_date(selected_file)
        date_format = '%d.%m.%Y %H:%M:%S'
        text_report_date = excel_report_date.strftime(date_format)
        self.ui.le_report_date.setText(text_report_date)

        # Проверяем нужно ли отбрасывать первые 2 символа ID.
        format_number = 0
        if self.ui.chb_id10.isChecked():
            format_number = 2

        # Заполняем таблицу "Выгружено".
        uplouded_text = calc.get_text(excel_id_list, format_number)
        self.complete_table(self.le_uploaded, self.pe_uploaded, uplouded_text)

        # Проверяем файл отчёта и выводим данные.
        self.repeats_report_creation(
            text_report_date,
            excel_id_list,
            excel_report_date,
            format_number,
            selected_file,
            excel_dc_id_list,
        )

    def copy_field_text(self, field: QMainWindow) -> None:
        """
        Функция для копирования текста из поля.
        """
        text = field.toPlainText()
        pyperclip.copy(text)

        return None

    def log_updater(self, text: str) -> None:
        """
        Функция для обновления информации в логе
        """
        time = dt.datetime.now().time().strftime('%H:%M:%S')
        self.ui.pe_log.appendPlainText(f'{time} {text}')

        return None

    def log_cleaner(self) -> None:
        """
        Функция для очистки сообщений лога.
        """
        self.ui.pe_log.clear()

        return None

    def load_btn_connection(self) -> None:
        """
        Функция для связи кнопок с функциями-обработчиками.
        """
        # Кнопка загрузки файла.
        self.ui.btn_upload.clicked.connect(self.load_file)

        # Кнопки копирования текста из поля.
        self.ui.btn_copy_uploaded.clicked.connect(
            lambda: self.copy_field_text(self.pe_uploaded)
        )
        self.ui.btn_copy_repeats.clicked.connect(
            lambda: self.copy_field_text(self.pe_repeats)
        )
        self.ui.btn_copy_result.clicked.connect(
            lambda: self.copy_field_text(self.pe_result)
        )
        self.ui.btn_copy_track_id.clicked.connect(
            lambda: self.copy_field_text(self.pe_track_id)
        )

        # Кнопка очистки лога.
        self.ui.btn_clean_log.clicked.connect(self.log_cleaner)

        # Подключение combobox'а для фильтра ТК.
        self.ui.cb_tk.activated.connect(self.cb_dc_pattern_filter)

        return None

    def cb_dc_pattern_filter(self) -> None:
        """
        Считывает выбранный текст из ComboBox'а выбор ТК и передает pattern в
        cb_file_add_filtered_items для заполнения списка файлов.
        """
        match self.ui.cb_tk.currentText():
            case 'CDEK':
                pattern = "CDEK*.xlsx"
            case 'Shiptor':
                pattern = 'Shiptor'
            case 'Boxberry':
                pattern = 'parcel_export_*.xlsx'
            case 'Grastin':
                pattern = 'Grastin'
        self.cb_file_add_filtered_items(pattern)

        return None

    def cb_file_add_filtered_items(self, pattern) -> None:
        """
        Получая на входе паттерн заполняет файлы в ComboBox файлов,
        соответствующие данному фильтру.
        """
        listOfFiles = os.listdir(self.dir)
        self.ui.cb_file.clear()
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                self.ui.cb_file.addItem(entry)

        return None

    def first_load_setup(self) -> None:
        """
        Заполнение некоторых полей при первом запуске.
        """
        # Заполняем ComboBox ТК.
        tk_list = ('CDEK', 'Shiptor', 'Boxberry', 'Grastin')
        self.ui.cb_tk.addItems(tk_list)

        # Заполняем текущую дату.
        today_date = dt.datetime.now().date()
        text_today_date = today_date.strftime('%d.%m.%Y')
        self.ui.le_date.setText(text_today_date)

        # Первично заполняем ComboBox файлами.
        self.cb_dc_pattern_filter()

        # Подключаем кнопки.
        self.load_btn_connection()

        return None

    def clear_table(self, *args) -> None:
        """
        Очищает данные в выбранных таблицах.
        """
        for arg in args:
            arg.clear()
        return None

    def complete_table(self, le_field, pe_field, text) -> None:
        """
        Функция заполняет текст в поле Plain Edit и записывает количество
        строк в поле Line Edit.
        """
        pe_field.setPlainText(text)

        amount = len(text.splitlines())
        le_field.setText(f'Всего: {amount}')
        return None

    def repeats_report_creation(
        self,
        text_report_date,
        excel_id_list,
        excel_report_date,
        format_number,
        selected_file,
        excel_dc_id_list,
    ) -> None:
        """
        Функция для создания и обновления файла повторов и вывода результата.
        """
        report_excel_list = excel_id_list + excel_dc_id_list
        report_id_text = calc.get_text(report_excel_list)
        report_file = 'repeats_reports.txt'
        track_id_without_repeats = []
        if not (os.path.exists(report_file)):
            track_id_without_repeats = excel_dc_id_list
            self.create_report_file(
                report_file,
                text_report_date,
                report_id_text,
                excel_id_list,
                track_id_without_repeats,
                format_number,
            )
        else:
            file_data = self.get_file_data(report_file)
            date_from_file = file_data.get('date')

            # Проверяем какие данные более свежие.
            if date_from_file < excel_report_date:
                # Получаем словарь с данными из файла
                repeat_dict = self.repeats_list_creation(
                    file_data, excel_id_list, excel_dc_id_list
                )

                # Получаем списки из словаря.
                repeats_list = repeat_dict.get('repeats_list')
                track_id_without_repeats = repeat_dict.get(
                    'track_id_without_repeats'
                )

                # Заполняем таблицы.
                self.complete_all_tables(
                    excel_id_list,
                    track_id_without_repeats,
                    format_number,
                    repeats_list,
                )

                # Замещаем данные в файле отчета данными из таблицы.
                self.update_report_file(
                    report_file, text_report_date, report_id_text
                )

                file_name = 'sdek_report.txt'
                self.upd_cdek_report_file(
                    file_name,
                    text_report_date,
                    excel_id_list,
                    excel_dc_id_list,
                )

                # Пишем лог.
                log_text = f'Загружены данные из файла {selected_file}'
                self.log_updater(log_text)

                log_text = f'Файл {report_file} обновлён.'
                self.log_updater(log_text)
            else:
                # Если актуальные файлы уже были в отчете.
                # Пишем лог.
                log_text = 'Данные в выбранном отчете устарели!'
                self.log_updater(log_text)

                # Очищаем повторяющиеся и неповторяющиеся ID и их количество.
                self.clear_table(
                    self.pe_repeats,
                    self.le_repeats,
                    self.pe_result,
                    self.le_result,
                    self.pe_track_id,
                    self.le_track_id,
                )

        return None

    def create_report_file(
        self,
        report_file,
        text_report_date,
        report_id_text,
        excel_id_list,
        track_id_without_repeats,
        format_number,
    ) -> None:
        """
        Функция для создания файла отчета.
        """
        self.update_report_file(report_file, text_report_date, report_id_text)

        # Заполняем таблицы.
        self.complete_all_tables(
            excel_id_list,
            track_id_without_repeats,
            format_number,
        )

        # Пишем лог.
        log_text = f'Создан файл: {report_file}'
        self.log_updater(log_text)
        return None

    def complete_all_tables(
        self,
        excel_id_list,
        track_id_without_repeats,
        format_number,
        repeats_list=[],
    ) -> None:
        """
        Заполняет таблицы 'Повторы', 'Результат' и 'Трек-номера'
        """
        # Выводим повторяющиеся ID.
        repeats_text = calc.get_text(repeats_list, format_number)
        self.complete_table(self.le_repeats, self.pe_repeats, repeats_text)

        # Выводим ID без повторов.
        result_list = self.list_difference(excel_id_list, repeats_list)
        result_text = calc.get_text(result_list, format_number)
        self.complete_table(self.le_result, self.pe_result, result_text)

        # Заполняем таблицу "Трек-номера".
        dc_id_text = calc.get_text(track_id_without_repeats)
        self.complete_table(self.le_track_id, self.pe_track_id, dc_id_text)

        return None

    def repeats_list_creation(
        self, file_data, excel_id_list, excel_dc_id_list
    ) -> dict:
        """
        Функция для создания списков повторов ID и трек номеров.
        """
        repeats_list = []
        track_id_without_repeats = []
        id_list = file_data.get('id_list')
        report_track_id_list = file_data.get('track_id_list')
        for element in excel_id_list:
            if element in id_list:
                repeats_list.append(element)

        for element in excel_dc_id_list:
            if element not in report_track_id_list:
                track_id_without_repeats.append(element)

        result_dict = {
            'repeats_list': repeats_list,
            'track_id_without_repeats': track_id_without_repeats,
        }

        return result_dict

    @staticmethod
    def upd_cdek_report_file(
        file_name, report_date, id_list, dc_id_list
    ) -> None:
        """
        Updating CDEK report file func.
        """

        text = (
            f'{{"date": "{report_date}", '
            f'"id_list": "{id_list}", '
            f'"dc_id_list": "{dc_id_list}"}}'
        )

        with open(file_name, 'w') as opened_file:
            opened_file.write(text)

        return None

    @staticmethod
    def read_cdek_report(file_name) -> dict:
        """
        Read CDEK report file func.
        """
        with open(file_name, 'r') as opened_file:
            file_data = opened_file.read()
            data_dict = json.loads(file_data)

        return data_dict


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainProgram()
    window.show()
    sys.exit(app.exec())


# Для комплирования дизайна.
# pyside6-uic design.ui -o design.py

# Для компилирования .exe файла.
# pyinstaller --onefile  --noconsole main.py

# Для изменения цвета задника.
# self.ui.le_report_date.setStyleSheet('background-color: green')

# todo:
# Переработать логику с проверкой файла report на наличие.
# Добавить обработку файлов с -1 (актуально для боксбери).
# Добавить обработку разных ТК.
# Создавать файл BU для каждого дня.
# Время поменять на Московское (или показывать и то и другое).
# Добавить отображение даты последнего загруженного отчета.

# Добавить файл конфига где будет выбор откуда брать файлы отчета и
# настройки "парса" эксель отчетов разных ТК.

# Добавить галочку для загрузки отчета без изменений в report файл.
# Написать тесты для функций.
# Поправить импорты (импортировать только необходимые методы).
# Читать и записывать информацию в json формате.
# Печатать накладные ТК
# Функцию считывания даты из названия файла впихнуть в класс ТК.
# Добавить кнопку обновить файлы в комбо бокс (или оновлять их автоматически)
