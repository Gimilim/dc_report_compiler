import datetime as dt
import fnmatch
import os
import sys

import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow

import calculations as calc
import CDEK_report as cd
from design6 import Ui_MainWindow


class MainProgram(QMainWindow):
    def __init__(self):
        super(MainProgram, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Кнопка загрузки файла.
        self.ui.btn_load.clicked.connect(lambda: self.load_file())

        # Кнопка копирования результата (нужно переработать)
        # self.ui.btn_copy.clicked.connect(lambda: self.copy_orders())

        # Заполняем комбобокс.
        listOfFiles = os.listdir('.')
        pattern = "*.xlsx"
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                self.ui.comboBox.addItem(entry)

        # Заполняем текущую дату.
        self.today_date = dt.datetime.now().date()
        text_today_date = self.today_date.strftime('%d.%m.%Y')
        self.ui.le_date.setText(text_today_date)

    def load_file(self) -> None:
        """Заполняет колонки с ID"""
        # Считываем выбранный файл из comboBox.
        selected_file = self.ui.comboBox.currentText()

        # Получаем весь список ID CDEK'а.
        cd_list = cd.cdek_get_id_list(selected_file)

        # Заполняем данные по файлу.
        # Определяем дату отчета.
        cdek_report_date_from_file = self.ui.comboBox.currentText()[19:29]
        sdek_report_day = int(cdek_report_date_from_file[8:10])
        sdek_report_month = int(cdek_report_date_from_file[5:7])
        sdek_report_year = int(cdek_report_date_from_file[0:4])
        sdek_report_date = dt.date(
            sdek_report_year, sdek_report_month, sdek_report_day
        )
        text_sdek_report_date = sdek_report_date.strftime('%d.%m.%Y')
        self.ui.le_report_date.setText(text_sdek_report_date)
        if self.today_date != sdek_report_date:
            self.ui.le_report_date.setStyleSheet('background-color: red')
        else:
            self.ui.le_report_date.setStyleSheet('background-color: green')

        # Определяем ТК.
        if 'CDEK' in self.ui.comboBox.currentText():
            self.ui.le_dc.setText('CDEK')

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
        report_file = 'repeats_reports.txt'
        repeats_list = []
        if not (os.path.exists(report_file)):
            with open(report_file, 'w') as opened_file:
                opened_file.write(uplouded_text)
            self.ui.pe_log.setPlainText(f'Создан файл: {report_file}')
        else:
            with open(report_file, 'r') as opened_file:
                file_list = []
                for line in opened_file:
                    line = line.rstrip('\n')
                    file_list.append(int(line))
            for element in cd_list:
                if element in file_list:
                    repeats_list.append(element)
            if repeats_list == []:
                with open(report_file, 'w') as opened_file:
                    writing_text = calc.get_text(cd_list)
                    opened_file.write(writing_text)
                # в коде выше есть ошибка. Повторы неправильно перезаписываются

        # Заполняем данные по повторам.
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

        # Считаем и выводим количество заказов

        # Выводим количество ID из таблицы..
        # result_amount = ...
        #
        # self.ui.le_result.setText(f'Всего: {result_amount}')

        # Заполняем лог.
        # pass
        # self.ui.pe_log.setPlainText(...)

    def copy_orders(self):
        """
        Функция для копирования всего текста итогового списка ID
        """
        text = self.ui.pe_result.toPlainText()
        pyperclip.copy(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainProgram()
    window.show()
    sys.exit(app.exec())

# pyside6-uic design.ui -o design.py
# Изменения для тестовой ветки
