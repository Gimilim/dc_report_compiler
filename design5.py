# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design5.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(583, 581)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 130, 111, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.le_today = QLineEdit(self.verticalLayoutWidget)
        self.le_today.setObjectName(u"le_today")

        self.verticalLayout.addWidget(self.le_today)

        self.pe_today = QPlainTextEdit(self.verticalLayoutWidget)
        self.pe_today.setObjectName(u"pe_today")
        self.pe_today.setReadOnly(True)

        self.verticalLayout.addWidget(self.pe_today)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(160, 130, 111, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.le_yesterday = QLineEdit(self.verticalLayoutWidget_2)
        self.le_yesterday.setObjectName(u"le_yesterday")

        self.verticalLayout_2.addWidget(self.le_yesterday)

        self.pe_yesterday = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.pe_yesterday.setObjectName(u"pe_yesterday")
        self.pe_yesterday.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.pe_yesterday)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(290, 130, 111, 211))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.le_rest = QLineEdit(self.verticalLayoutWidget_3)
        self.le_rest.setObjectName(u"le_rest")

        self.verticalLayout_3.addWidget(self.le_rest)

        self.pe_rest = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.pe_rest.setObjectName(u"pe_rest")
        self.pe_rest.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.pe_rest)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(160, 360, 111, 211))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.le_last_5_day = QLineEdit(self.verticalLayoutWidget_5)
        self.le_last_5_day.setObjectName(u"le_last_5_day")

        self.verticalLayout_5.addWidget(self.le_last_5_day)

        self.pe_last_5_day = QPlainTextEdit(self.verticalLayoutWidget_5)
        self.pe_last_5_day.setObjectName(u"pe_last_5_day")
        self.pe_last_5_day.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.pe_last_5_day)

        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(420, 130, 121, 441))
        self.verticalLayout_16 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_5)

        self.le_result = QLineEdit(self.verticalLayoutWidget_6)
        self.le_result.setObjectName(u"le_result")

        self.verticalLayout_16.addWidget(self.le_result)

        self.pe_result = QPlainTextEdit(self.verticalLayoutWidget_6)
        self.pe_result.setObjectName(u"pe_result")
        self.pe_result.setReadOnly(True)

        self.verticalLayout_16.addWidget(self.pe_result)

        self.btn_copy = QPushButton(self.verticalLayoutWidget_6)
        self.btn_copy.setObjectName(u"btn_copy")

        self.verticalLayout_16.addWidget(self.btn_copy)

        self.verticalLayoutWidget_10 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(380, 41, 187, 82))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_generate = QPushButton(self.verticalLayoutWidget_10)
        self.btn_generate.setObjectName(u"btn_generate")

        self.verticalLayout_9.addWidget(self.btn_generate)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.chb_today = QCheckBox(self.verticalLayoutWidget_10)
        self.chb_today.setObjectName(u"chb_today")

        self.verticalLayout_7.addWidget(self.chb_today)

        self.chb_yesterday = QCheckBox(self.verticalLayoutWidget_10)
        self.chb_yesterday.setObjectName(u"chb_yesterday")

        self.verticalLayout_7.addWidget(self.chb_yesterday)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.chb_last_5_day = QCheckBox(self.verticalLayoutWidget_10)
        self.chb_last_5_day.setObjectName(u"chb_last_5_day")

        self.verticalLayout_8.addWidget(self.chb_last_5_day)

        self.chb_rest = QCheckBox(self.verticalLayoutWidget_10)
        self.chb_rest.setObjectName(u"chb_rest")

        self.verticalLayout_8.addWidget(self.chb_rest)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.chb_id10 = QCheckBox(self.centralwidget)
        self.chb_id10.setObjectName(u"chb_id10")
        self.chb_id10.setGeometry(QRect(220, 30, 71, 20))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 10, 421, 21))
        self.btn_load = QPushButton(self.centralwidget)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(460, 10, 111, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043e\u0442\u0447\u0435\u0442\u043e\u0432 \u0422\u041a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0447\u0435\u0440\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430 5 \u0434\u043d\u0435\u0439", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.chb_today.setText(QCoreApplication.translate("MainWindow", u"C\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.chb_yesterday.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0447\u0435\u0440\u0430", None))
        self.chb_last_5_day.setText(QCoreApplication.translate("MainWindow", u"5 \u0414\u043d\u0435\u0439", None))
        self.chb_rest.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435", None))
        self.chb_id10.setText(QCoreApplication.translate("MainWindow", u"ID \u0431\u0435\u0437 10", None))
        self.btn_load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

