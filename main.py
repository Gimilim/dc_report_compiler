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

        # Кнопка загрузки заказов.
        self.ui.btn_load.clicked.connect(lambda: self.add_orders())

        # Кнопка генерации результата (более не используется).
        # self.ui.btn_generate.clicked.connect(lambda: self.combine_orders())

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

    def add_orders(self) -> None:
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
        upouded_text = calc.get_text(cd_list, format_number)
        self.ui.pe_uplouded.setPlainText(upouded_text)

        uploaded_amount = len(upouded_text.splitlines())
        self.ui.le_uplouaded.setText(f'Всего: {uploaded_amount}')

        # Проверяем наличие файла отчета за дату и создаем его если нет.
        # 16.11.2022-CDEK.txt
        if not (os.path.exists('16.11.2022-CDEK.txt')):
            with open('16.11.2022-CDEK.txt', 'w+') as opened_file:
                opened_file.write(upouded_text)
        else:
            with open('16.11.2022-CDEK.txt') as opened_file:
                repeats_list = []
                for line in opened_file:
                    line = line.rstrip('\n')
                    repeats_list.append(line)

        print(repeats_list)
        repeats_text = '\n'.join(repeats_list)
        # result_text = ...
        self.ui.pe_repeats.setPlainText(repeats_text)
        # self.ui.pe_result.setPlainText(result_text)

        # Считаем и выводим количество заказов

        # Выводим количество ID миз таблицы
        # repeats_amount = ...
        # result_amount = ...
        # self.ui.le_repeats.setText(f'Всего: {repeats_amount}')
        # self.ui.le_result.setText(f'Всего: {result_amount}')

        # Заполняем лог.
        # pass
        # self.ui.pe_log.setPlainText(...)

        # Старая логика
        # format_number = 0
        # if self.ui.chb_id10.isChecked():
        #     format_number = 2
        # today_text = calc.get_text(id_dict, 'today', format_number)
        # self.ui.pe_today.setPlainText(today_text)

        # yesterda_text = calc.get_text(id_dict, 'yesterday', format_number)
        # self.ui.pe_yesterday.setPlainText(yesterda_text)

        # last_5_day_text = calc.get_text(id_dict, 'last_5_day', format_number)
        # self.ui.pe_last_5_day.setPlainText(last_5_day_text)

        # rest_text = calc.get_text(id_dict, 'rest', format_number)
        # self.ui.pe_rest.setPlainText(rest_text)

        # today_amount = len(today_text.splitlines())
        # self.ui.le_today.setText(f'Всего: {today_amount}')

        # yesterday_amount = len(yesterda_text.splitlines())
        # self.ui.le_yesterday.setText(f'Всего: {yesterday_amount}')

        # last_5_day_amount = len(last_5_day_text.splitlines())
        # self.ui.le_last_5_day.setText(f'Всего: {last_5_day_amount}')

        # rest_amount = len(rest_text.splitlines())
        # self.ui.le_rest.setText(f'Всего: {rest_amount}')

    def combine_orders(self):
        """
        Функция для создания итогового списка ID.
        """
        combine_text = ''
        if self.ui.chb_today.isChecked():
            combine_text = self.ui.pe_today.toPlainText()
        if self.ui.chb_yesterday.isChecked():
            if combine_text == '' or combine_text.readlines() == '/n':
                combine_text = self.ui.pe_yesterday.toPlainText()
            else:
                combine_text = '\n'.join(
                    [combine_text, self.ui.pe_yesterday.toPlainText()]
                )
        if self.ui.chb_last_5_day.isChecked():
            if combine_text == '' or combine_text.readlines() == '/n':
                combine_text = self.ui.pe_last_5_day.toPlainText()
            else:
                combine_text = '\n'.join(
                    [combine_text, self.ui.pe_last_5_day.toPlainText()]
                )
        if self.ui.chb_rest.isChecked():
            if combine_text == '' or combine_text.readlines() == '/n':
                combine_text = self.ui.pe_rest.toPlainText()
            else:
                combine_text = '\n'.join(
                    [combine_text, self.ui.pe_rest.toPlainText()]
                )
        self.ui.pe_result.setPlainText(combine_text)
        result_amount = len(combine_text.splitlines())
        self.ui.le_result.setText(f'Всего: {result_amount}')

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
