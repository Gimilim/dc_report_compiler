import datetime as dt
import fnmatch
import os
import sys

import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow

import calculations as calc
import CDEK_report as cd
from design9 import Ui_MainWindow


class MainProgram(QMainWindow):
    def __init__(self):
        super(MainProgram, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_btn_connection()

        # Заполняем комбобокс ТК.
        tk_list = ('CDEK', 'Shiptor', 'Boxberry', 'Grastin')
        self.ui.cb_tk.addItems(tk_list)

        # Заполняем комбобокс файлов.
        listOfFiles = os.listdir('.')
        pattern = "*.xlsx"
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                self.ui.cb_file.addItem(entry)

        # Заполняем текущую дату.
        self.today_date = dt.datetime.now().date()
        text_today_date = self.today_date.strftime('%d.%m.%Y')
        self.ui.le_date.setText(text_today_date)

        # test
        self.some_func('result')
        # test

    def load_file(self) -> None:
        """Заполняет колонки с ID"""
        # Считываем выбранный файл из cb_file.
        selected_file = self.ui.cb_file.currentText()

        # Получаем весь список ID CDEK'а.
        cd_list = cd.cdek_get_id_list(selected_file)

        report_date = self.get_file_date(selected_file)
        date_format = '%d.%m.%Y %H:%M:%S'
        text_report_date = report_date.strftime(date_format)
        self.ui.le_report_date.setText(text_report_date)

        # Формируем и выводим список ID.
        format_number = 0
        if self.ui.chb_id10.isChecked():
            format_number = 2

        # Заполняем данные из таблицы.
        uplouded_text = calc.get_text(cd_list, format_number)
        self.ui.pe_uplouded.setPlainText(uplouded_text)

        uploaded_amount = len(uplouded_text.splitlines())
        self.ui.le_uplouaded.setText(f'Всего: {uploaded_amount}')

        # Проверяем наличие файла отчета за дату и создаем его если нет.
        # Тут нужно проверять повторы и создавать файл для каждой ТК
        report_file = 'repeats_reports.txt'
        repeats_list = []
        if not (os.path.exists(report_file)):
            with open(report_file, 'w') as opened_file:
                opened_file.write(f'{text_report_date}\n')
                opened_file.write(uplouded_text)
            log_text = f'Создан файл: {report_file}'
            self.log_updater(log_text)
        else:
            date_from_file = ''
            with open(report_file, 'r') as opened_file:
                file_list = []
                for line in opened_file:
                    line = line.rstrip('\n')
                    try:
                        file_list.append(int(line))
                    except Exception:
                        date_from_file = dt.datetime.strptime(
                            line, date_format
                        )
                        continue
            if date_from_file == '' or date_from_file < report_date:
                for element in cd_list:
                    if element in file_list:
                        repeats_list.append(element)
                with open(report_file, 'w') as opened_file:
                    opened_file.write(f'{text_report_date}\n')

                    writing_text = calc.get_text(cd_list)
                    opened_file.write(writing_text)

                repeats_text = calc.get_text(repeats_list, format_number)
                self.ui.pe_repeats.setPlainText(repeats_text)

                repeats_amount = len(repeats_text.splitlines())
                self.ui.le_repeats.setText(f'Всего: {repeats_amount}')

                # Заполняем данные результата.
                uplouded_set = set(cd_list)
                repeats_set = set(repeats_list)
                result_set = uplouded_set - repeats_set
                result_list = list(result_set)
                result_text = calc.get_text(result_list, format_number)
                self.ui.pe_result.setPlainText(result_text)
                result_amount = len(result_text.splitlines())
                self.ui.le_result.setText(f'Всего: {result_amount}')
            else:
                log_text = 'Данные в выбранном отчете устарели!'
                self.log_updater(log_text)
                self.ui.pe_repeats.clear()
                self.ui.le_repeats.clear()
                self.ui.pe_result.clear()
                self.ui.le_result.clear()

    def copy_uploaded(self) -> None:
        """
        Функция для копирования загруженных ID.
        """
        text = self.ui.pe_uplouded.toPlainText()
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
        self.ui.btn_load.clicked.connect(self.load_file)

        # Кнопки копирования текста из поля.
        self.ui.btn_copy_uploaded.clicked.connect(self.copy_uploaded)
        self.ui.btn_copy_repeats.clicked.connect(self.copy_repeats)
        self.ui.btn_copy_result.clicked.connect(self.copy_result)

        # Кнопка очистки лога.
        self.ui.btn_clean_log.clicked.connect(self.log_cleaner)

        return None

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

    def some_func(self, name) -> None:
        test_str = f'self.ui.pe_{name}.setPlainText("test")'
        # self.ui.pe_result.setPlainText(result_text)
        eval(test_str)
        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainProgram()
    window.show()
    sys.exit(app.exec())

# pyside6-uic design.ui -o design.py
# Изменения для тестовой ветки
# Исправить очептки с upload (и вообще это должно быть download)
# self.ui.le_report_date.setStyleSheet('background-color: green')
