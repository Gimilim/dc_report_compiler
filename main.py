import fnmatch
import os
import sys

import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow

import calculations as calc
import CDEK_report as cd
from design5 import Ui_MainWindow


class MainProgram(QMainWindow):
    def __init__(self):
        super(MainProgram, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_load.clicked.connect(lambda: self.add_orders())

        self.ui.btn_generate.clicked.connect(lambda: self.combine_orders())
        self.ui.btn_copy.clicked.connect(lambda: self.copy_orders())

        self.ui.comboBox.addItem('Выберите файл')
        listOfFiles = os.listdir('.')
        pattern = "*.xlsx"
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                self.ui.comboBox.addItem(entry)

        print(self.ui.comboBox.currentText())

    def add_orders(self):
        # Начало мусорной конструкции.
        (
            today_list,
            yesterday_list,
            last_5_day_list,
            rest_list,
        ) = cd.cdek_get_report(self.ui.comboBox.currentText())

        id_dict = calc.qt_json_convert(
            today_list, yesterday_list, last_5_day_list, rest_list
        )
        # Конец мусорной конструкции.

        format_number = 0
        if self.ui.chb_id10.isChecked():
            format_number = 2
        today_text = calc.get_text(id_dict, 'today', format_number)
        self.ui.pe_today.setPlainText(today_text)

        yesterda_text = calc.get_text(id_dict, 'yesterday', format_number)
        self.ui.pe_yesterday.setPlainText(yesterda_text)

        last_5_day_text = calc.get_text(id_dict, 'last_5_day', format_number)
        self.ui.pe_last_5_day.setPlainText(last_5_day_text)

        rest_text = calc.get_text(id_dict, 'rest', format_number)
        self.ui.pe_rest.setPlainText(rest_text)

        today_amount = len(today_text.splitlines())
        self.ui.le_today.setText(f'Всего: {today_amount}')

        yesterday_amount = len(yesterda_text.splitlines())
        self.ui.le_yesterday.setText(f'Всего: {yesterday_amount}')

        last_5_day_amount = len(last_5_day_text.splitlines())
        self.ui.le_last_5_day.setText(f'Всего: {last_5_day_amount}')

        rest_amount = len(rest_text.splitlines())
        self.ui.le_rest.setText(f'Всего: {rest_amount}')

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
