# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design6.ui'
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
        self.chb_id10 = QCheckBox(self.centralwidget)
        self.chb_id10.setObjectName(u"chb_id10")
        self.chb_id10.setGeometry(QRect(380, 10, 71, 20))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 10, 341, 21))
        self.btn_load = QPushButton(self.centralwidget)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(450, 10, 111, 24))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 130, 531, 441))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.le_uplouaded = QLineEdit(self.horizontalLayoutWidget)
        self.le_uplouaded.setObjectName(u"le_uplouaded")

        self.verticalLayout.addWidget(self.le_uplouaded)

        self.pe_uplouded = QPlainTextEdit(self.horizontalLayoutWidget)
        self.pe_uplouded.setObjectName(u"pe_uplouded")
        self.pe_uplouded.setReadOnly(True)

        self.verticalLayout.addWidget(self.pe_uplouded)

        self.btn_copy_uploaded = QPushButton(self.horizontalLayoutWidget)
        self.btn_copy_uploaded.setObjectName(u"btn_copy_uploaded")

        self.verticalLayout.addWidget(self.btn_copy_uploaded)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.le_repeats = QLineEdit(self.horizontalLayoutWidget)
        self.le_repeats.setObjectName(u"le_repeats")

        self.verticalLayout_2.addWidget(self.le_repeats)

        self.pe_repeats = QPlainTextEdit(self.horizontalLayoutWidget)
        self.pe_repeats.setObjectName(u"pe_repeats")
        self.pe_repeats.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.pe_repeats)

        self.btn_copy_repeats = QPushButton(self.horizontalLayoutWidget)
        self.btn_copy_repeats.setObjectName(u"btn_copy_repeats")

        self.verticalLayout_2.addWidget(self.btn_copy_repeats)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_5)

        self.le_result = QLineEdit(self.horizontalLayoutWidget)
        self.le_result.setObjectName(u"le_result")

        self.verticalLayout_16.addWidget(self.le_result)

        self.pe_result = QPlainTextEdit(self.horizontalLayoutWidget)
        self.pe_result.setObjectName(u"pe_result")
        self.pe_result.setReadOnly(True)

        self.verticalLayout_16.addWidget(self.pe_result)

        self.btn_copy_result = QPushButton(self.horizontalLayoutWidget)
        self.btn_copy_result.setObjectName(u"btn_copy_result")

        self.verticalLayout_16.addWidget(self.btn_copy_result)


        self.horizontalLayout.addLayout(self.verticalLayout_16)

        self.le_report_date = QLineEdit(self.centralwidget)
        self.le_report_date.setObjectName(u"le_report_date")
        self.le_report_date.setGeometry(QRect(130, 70, 113, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 70, 61, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 40, 81, 16))
        self.le_date = QLineEdit(self.centralwidget)
        self.le_date.setObjectName(u"le_date")
        self.le_date.setGeometry(QRect(130, 40, 113, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 100, 21, 16))
        self.le_dc = QLineEdit(self.centralwidget)
        self.le_dc.setObjectName(u"le_dc")
        self.le_dc.setGeometry(QRect(130, 100, 113, 21))
        self.pe_log = QPlainTextEdit(self.centralwidget)
        self.pe_log.setObjectName(u"pe_log")
        self.pe_log.setGeometry(QRect(280, 50, 281, 71))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043e\u0442\u0447\u0435\u0442\u043e\u0432 \u0422\u041a", None))
        self.chb_id10.setText(QCoreApplication.translate("MainWindow", u"ID \u0431\u0435\u0437 10", None))
        self.btn_load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0436\u0435\u043d\u043e", None))
        self.btn_copy_uploaded.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u044b", None))
        self.btn_copy_repeats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.btn_copy_result.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0447\u0435\u0442 \u0437\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0434\u0430\u0442\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u041a", None))
    # retranslateUi

