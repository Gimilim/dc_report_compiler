import datetime as dt
import fnmatch
import os
import sys

import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow

import calculations as calc
import CDEK_report as cd
from design11 import Ui_MainWindow


class MainProgram(QMainWindow):
    @staticmethod
    def get_file_date(file_name) -> dt:
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
        Функция для чтения файлов, где первой строчкой идет дата, а в каждой
        последующей строчке ID
        """
        date_format = '%d.%m.%Y %H:%M:%S'
        with open(file_name, 'r') as opened_file:
            id_list = []
            for line in opened_file:
                line = line.rstrip('\n')
                try:
                    id_list.append(int(line))
                except Exception:
                    date_from_file = dt.datetime.strptime(line, date_format)
                    continue
        result = {'date': date_from_file, 'id_list': id_list}
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
        self.complete_upload_table(uplouded_text)

        # Заполняем таблицу "Трек-номера".
        dc_id_text = calc.get_text(excel_dc_id_list)
        self.complete_track_id_table(dc_id_text)

        # Проверяем файл отчёта и выводим данные.
        self.repeats_report_creation(
            text_report_date,
            excel_id_list,
            excel_report_date,
            format_number,
            selected_file,
        )

    def copy_uploaded(self) -> None:
        """
        Функция для копирования загруженных ID.
        """
        text = self.ui.pe_uploaded.toPlainText()
        pyperclip.copy(text)

        return None

    def copy_repeats(self) -> None:
        """
        Функция для копирования повторных ID.
        """
        text = self.ui.pe_repeats.toPlainText()
        pyperclip.copy(text)

        return None

    def copy_result(self) -> None:
        """
        Функция для копирования ID без повторов.
        """
        text = self.ui.pe_result.toPlainText()
        pyperclip.copy(text)

        return None

    def copy_track_id(self) -> None:
        """
        Функция для копирования трек-номеров.
        """
        text = self.ui.pe_track_id.toPlainText()
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
        # Кнопка загрузки файла.
        self.ui.btn_upload.clicked.connect(self.load_file)

        # Кнопки копирования текста из поля.
        self.ui.btn_copy_uploaded.clicked.connect(self.copy_uploaded)
        self.ui.btn_copy_repeats.clicked.connect(self.copy_repeats)
        self.ui.btn_copy_result.clicked.connect(self.copy_result)
        self.ui.btn_copy_track_id.clicked.connect(self.copy_track_id)

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
                pattern = 'Boxberry'
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
        for arg in args:
            arg.clear()
        return None

    def complete_upload_table(self, uplouded_text) -> None:
        """
        Функция заполнения таблицы "Выгружено".
        """
        self.ui.pe_uploaded.setPlainText(uplouded_text)

        uploaded_amount = len(uplouded_text.splitlines())
        self.ui.le_uploaded.setText(f'Всего: {uploaded_amount}')

        return None

    def complete_repeats_table(self, repeats_text) -> None:
        """
        Функция заполнения таблицы "Повторы".
        """
        self.ui.pe_repeats.setPlainText(repeats_text)

        # Выводим количество повторяющихся ID.
        repeats_amount = len(repeats_text.splitlines())
        self.ui.le_repeats.setText(f'Всего: {repeats_amount}')

        return None

    def complete_result_table(self, result_text) -> None:
        """
        Функция заполнения таблицы "Результат".
        """
        self.ui.pe_result.setPlainText(result_text)

        # Выводим количество ID без повторов.
        result_amount = len(result_text.splitlines())
        self.ui.le_result.setText(f'Всего: {result_amount}')

        return None

    def complete_track_id_table(self, dc_id_text) -> None:
        """
        Функция заполнения таблицы "Трек-номера".
        """
        self.ui.pe_track_id.setPlainText(dc_id_text)

        track_amount = len(dc_id_text.splitlines())
        self.ui.le_track_id.setText(f'Всего: {track_amount}')

        return None

    def repeats_report_creation(
        self,
        text_report_date,
        excel_id_list,
        excel_report_date,
        format_number,
        selected_file,
    ) -> None:
        """
        Функция для создания и обновления файла повторов и вывода результата.
        """
        full_id_text = calc.get_text(excel_id_list)
        report_file = 'repeats_reports.txt'
        repeats_list = []
        if not (os.path.exists(report_file)):
            # Если файла отчёта нет - создаем его и заполняем ID из таблицы.
            self.update_report_file(
                report_file, text_report_date, full_id_text
            )

            # Пишем лог.
            log_text = f'Создан файл: {report_file}'
            self.log_updater(log_text)
        else:
            # Если файл отчёта есть - считываем дату.
            file_data = self.get_file_data(report_file)
            date_from_file = file_data.get('date')

            # Проверяем какие данные более свежие.
            if date_from_file < excel_report_date:
                # Если данные в файлее отчета старее, чем данные в таблице, то
                # Ищем повторы.
                id_list = file_data.get('id_list')
                for element in excel_id_list:
                    if element in id_list:
                        repeats_list.append(element)

                # Замещаем данные в файле отчета данными из таблицы.
                self.update_report_file(
                    report_file, text_report_date, full_id_text
                )

                # Выводим повторяющиеся ID.
                repeats_text = calc.get_text(repeats_list, format_number)
                self.complete_repeats_table(repeats_text)

                # Выводим ID без повторов.
                result_list = self.list_difference(excel_id_list, repeats_list)
                result_text = calc.get_text(result_list, format_number)
                self.complete_result_table(result_text)

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
                    self.ui.pe_repeats,
                    self.ui.le_repeats,
                    self.ui.pe_result,
                    self.ui.le_result,
                )

        return None

    # def repeats_report_track_id_creation(
    #     self, text_report_date, excel_dc_id_list
    # ) -> None:
    #     """
    #     Функция для создания и обновления файла повторов трек номеров.
    #     """
    #     report_file = 'track_id_repeats.txt'
    #     full_id_text = calc.get_text(excel_dc_id_list)
    #     if not (os.path.exists(report_file)):
    #         # Если файла отчёта нет - создаем его и заполняем ID из таблицы.
    #         self.update_report_file(
    #             report_file, text_report_date, full_id_text
    #         )
    #     return None


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
# Переработать логику с проверкой файла на наличие.
# Добавить обработку файлов с -1 (актуально для боксбери).
# Добавить обработку разных ТК.
# Создавать файл BU для каждого дня.
# Время поменять на Московское.
# Добавить отображение даты последнего загруженного отчета.
# Добавить проверку для трек номеров на повтор трека с 00фр.
