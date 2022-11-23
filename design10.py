# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design10.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 614)
        MainWindow.setMinimumSize(QSize(580, 614))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.cb_tk = QComboBox(self.centralwidget)
        self.cb_tk.setObjectName(u"cb_tk")

        self.horizontalLayout_2.addWidget(self.cb_tk)

        self.cb_file = QComboBox(self.centralwidget)
        self.cb_file.setObjectName(u"cb_file")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_file.sizePolicy().hasHeightForWidth())
        self.cb_file.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.cb_file)

        self.chb_id10 = QCheckBox(self.centralwidget)
        self.chb_id10.setObjectName(u"chb_id10")
        self.chb_id10.setChecked(True)

        self.horizontalLayout_2.addWidget(self.chb_id10)

        self.btn_upload = QPushButton(self.centralwidget)
        self.btn_upload.setObjectName(u"btn_upload")

        self.horizontalLayout_2.addWidget(self.btn_upload)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.le_date = QLineEdit(self.centralwidget)
        self.le_date.setObjectName(u"le_date")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_date.sizePolicy().hasHeightForWidth())
        self.le_date.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_date)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.le_report_date = QLineEdit(self.centralwidget)
        self.le_report_date.setObjectName(u"le_report_date")
        sizePolicy1.setHeightForWidth(self.le_report_date.sizePolicy().hasHeightForWidth())
        self.le_report_date.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_report_date)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.le_last_repeats_date = QLineEdit(self.centralwidget)
        self.le_last_repeats_date.setObjectName(u"le_last_repeats_date")
        sizePolicy1.setHeightForWidth(self.le_last_repeats_date.sizePolicy().hasHeightForWidth())
        self.le_last_repeats_date.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_last_repeats_date)


        self.verticalLayout_7.addLayout(self.formLayout)

        self.btn_make_invoice = QPushButton(self.centralwidget)
        self.btn_make_invoice.setObjectName(u"btn_make_invoice")

        self.verticalLayout_7.addWidget(self.btn_make_invoice)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pe_log = QPlainTextEdit(self.centralwidget)
        self.pe_log.setObjectName(u"pe_log")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pe_log.sizePolicy().hasHeightForWidth())
        self.pe_log.setSizePolicy(sizePolicy2)
        self.pe_log.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_3.addWidget(self.pe_log)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_clean_log = QPushButton(self.centralwidget)
        self.btn_clean_log.setObjectName(u"btn_clean_log")

        self.verticalLayout_3.addWidget(self.btn_clean_log)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.le_uploaded = QLineEdit(self.centralwidget)
        self.le_uploaded.setObjectName(u"le_uploaded")

        self.verticalLayout.addWidget(self.le_uploaded)

        self.pe_uploaded = QPlainTextEdit(self.centralwidget)
        self.pe_uploaded.setObjectName(u"pe_uploaded")
        self.pe_uploaded.setReadOnly(True)

        self.verticalLayout.addWidget(self.pe_uploaded)

        self.btn_copy_uploaded = QPushButton(self.centralwidget)
        self.btn_copy_uploaded.setObjectName(u"btn_copy_uploaded")

        self.verticalLayout.addWidget(self.btn_copy_uploaded)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.le_repeats = QLineEdit(self.centralwidget)
        self.le_repeats.setObjectName(u"le_repeats")

        self.verticalLayout_2.addWidget(self.le_repeats)

        self.pe_repeats = QPlainTextEdit(self.centralwidget)
        self.pe_repeats.setObjectName(u"pe_repeats")
        self.pe_repeats.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.pe_repeats)

        self.btn_copy_repeats = QPushButton(self.centralwidget)
        self.btn_copy_repeats.setObjectName(u"btn_copy_repeats")

        self.verticalLayout_2.addWidget(self.btn_copy_repeats)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_5)

        self.le_result = QLineEdit(self.centralwidget)
        self.le_result.setObjectName(u"le_result")

        self.verticalLayout_16.addWidget(self.le_result)

        self.pe_result = QPlainTextEdit(self.centralwidget)
        self.pe_result.setObjectName(u"pe_result")
        self.pe_result.setReadOnly(True)

        self.verticalLayout_16.addWidget(self.pe_result)

        self.btn_copy_result = QPushButton(self.centralwidget)
        self.btn_copy_result.setObjectName(u"btn_copy_result")

        self.verticalLayout_16.addWidget(self.btn_copy_result)


        self.horizontalLayout.addLayout(self.verticalLayout_16)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043e\u0442\u0447\u0435\u0442\u043e\u0432 \u0422\u041a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u041a", None))
        self.chb_id10.setText(QCoreApplication.translate("MainWindow", u"ID \u0431\u0435\u0437 10", None))
        self.btn_upload.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0434\u0430\u0442\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0447\u0435\u0442 \u0437\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043e:", None))
        self.btn_make_invoice.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u044d\u043a \u043d\u043e\u043c\u0435\u0440\u0430 \u0434\u043b\u044f CDEK \u043d\u0430\u043a\u043b\u0430\u0434\u043d\u043e\u0439", None))
        self.btn_clean_log.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043b\u043e\u0433", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0436\u0435\u043d\u043e:", None))
        self.btn_copy_uploaded.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u044b:", None))
        self.btn_copy_repeats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.btn_copy_result.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

