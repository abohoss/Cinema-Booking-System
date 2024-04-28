# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReserveView.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 30, 241, 81))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(480, 300, 251, 161))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.seat17 = QPushButton(self.gridLayoutWidget)
        self.seat17.setObjectName(u"seat17")
        self.seat17.setCheckable(True)

        self.gridLayout.addWidget(self.seat17, 4, 1, 1, 1)

        self.seat3 = QPushButton(self.gridLayoutWidget)
        self.seat3.setObjectName(u"seat3")
        self.seat3.setCheckable(True)

        self.gridLayout.addWidget(self.seat3, 0, 2, 1, 1)

        self.seat7 = QPushButton(self.gridLayoutWidget)
        self.seat7.setObjectName(u"seat7")
        self.seat7.setCheckable(True)

        self.gridLayout.addWidget(self.seat7, 1, 1, 1, 1)

        self.seat20 = QPushButton(self.gridLayoutWidget)
        self.seat20.setObjectName(u"seat20")
        self.seat20.setCheckable(True)

        self.gridLayout.addWidget(self.seat20, 4, 4, 1, 1)

        self.seat6 = QPushButton(self.gridLayoutWidget)
        self.seat6.setObjectName(u"seat6")
        self.seat6.setCheckable(True)

        self.gridLayout.addWidget(self.seat6, 1, 0, 1, 1)

        self.seat10 = QPushButton(self.gridLayoutWidget)
        self.seat10.setObjectName(u"seat10")
        self.seat10.setCheckable(True)

        self.gridLayout.addWidget(self.seat10, 1, 4, 1, 1)

        self.seat4 = QPushButton(self.gridLayoutWidget)
        self.seat4.setObjectName(u"seat4")
        self.seat4.setCheckable(True)

        self.gridLayout.addWidget(self.seat4, 0, 3, 1, 1)

        self.seat19 = QPushButton(self.gridLayoutWidget)
        self.seat19.setObjectName(u"seat19")
        self.seat19.setCheckable(True)

        self.gridLayout.addWidget(self.seat19, 4, 3, 1, 1)

        self.seat16 = QPushButton(self.gridLayoutWidget)
        self.seat16.setObjectName(u"seat16")
        self.seat16.setCheckable(True)

        self.gridLayout.addWidget(self.seat16, 4, 0, 1, 1)

        self.seat2 = QPushButton(self.gridLayoutWidget)
        self.seat2.setObjectName(u"seat2")
        self.seat2.setCheckable(True)

        self.gridLayout.addWidget(self.seat2, 0, 1, 1, 1)

        self.seat11 = QPushButton(self.gridLayoutWidget)
        self.seat11.setObjectName(u"seat11")
        self.seat11.setCheckable(True)

        self.gridLayout.addWidget(self.seat11, 2, 0, 1, 1)

        self.seat14 = QPushButton(self.gridLayoutWidget)
        self.seat14.setObjectName(u"seat14")
        self.seat14.setCheckable(True)

        self.gridLayout.addWidget(self.seat14, 2, 3, 1, 1)

        self.seat12 = QPushButton(self.gridLayoutWidget)
        self.seat12.setObjectName(u"seat12")
        self.seat12.setCheckable(True)

        self.gridLayout.addWidget(self.seat12, 2, 1, 1, 1)

        self.seat13 = QPushButton(self.gridLayoutWidget)
        self.seat13.setObjectName(u"seat13")
        self.seat13.setCheckable(True)

        self.gridLayout.addWidget(self.seat13, 2, 2, 1, 1)

        self.seat9 = QPushButton(self.gridLayoutWidget)
        self.seat9.setObjectName(u"seat9")
        self.seat9.setCheckable(True)

        self.gridLayout.addWidget(self.seat9, 1, 3, 1, 1)

        self.seat15 = QPushButton(self.gridLayoutWidget)
        self.seat15.setObjectName(u"seat15")
        self.seat15.setCheckable(True)

        self.gridLayout.addWidget(self.seat15, 2, 4, 1, 1)

        self.seat1 = QPushButton(self.gridLayoutWidget)
        self.seat1.setObjectName(u"seat1")
        self.seat1.setCheckable(True)

        self.gridLayout.addWidget(self.seat1, 0, 0, 1, 1)

        self.seat5 = QPushButton(self.gridLayoutWidget)
        self.seat5.setObjectName(u"seat5")
        self.seat5.setCheckable(True)

        self.gridLayout.addWidget(self.seat5, 0, 4, 1, 1)

        self.seat18 = QPushButton(self.gridLayoutWidget)
        self.seat18.setObjectName(u"seat18")
        self.seat18.setCheckable(True)

        self.gridLayout.addWidget(self.seat18, 4, 2, 1, 1)

        self.seat8 = QPushButton(self.gridLayoutWidget)
        self.seat8.setObjectName(u"seat8")
        self.seat8.setCheckable(True)

        self.gridLayout.addWidget(self.seat8, 1, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 170, 121, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 230, 111, 41))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 290, 81, 41))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 410, 141, 51))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 350, 161, 31))
        self.label_6.setFont(font1)
        self.time = QComboBox(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(190, 170, 131, 28))
        self.date = QComboBox(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(190, 240, 131, 28))
        self.hallnum = QComboBox(self.centralwidget)
        self.hallnum.setObjectName(u"hallnum")
        self.hallnum.setGeometry(QRect(190, 300, 81, 28))
        self.ptype = QComboBox(self.centralwidget)
        self.ptype.setObjectName(u"ptype")
        self.ptype.setGeometry(QRect(190, 350, 111, 28))
        self.reserveType = QLineEdit(self.centralwidget)
        self.reserveType.setObjectName(u"reserveType")
        self.reserveType.setGeometry(QRect(190, 420, 171, 28))
        self.reserveType.setReadOnly(True)
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(440, 540, 161, 40))
        font2 = QFont()
        font2.setPointSize(12)
        self.backBtn.setFont(font2)
        self.confirmBook = QPushButton(self.centralwidget)
        self.confirmBook.setObjectName(u"confirmBook")
        self.confirmBook.setGeometry(QRect(620, 540, 161, 40))
        self.confirmBook.setFont(font2)
        self.oLabel = QLabel(self.centralwidget)
        self.oLabel.setObjectName(u"oLabel")
        self.oLabel.setGeometry(QRect(30, 480, 411, 51))
        self.oLabel.setFont(font1)
        self.oLabel.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(450, 160, 311, 121))
        self.label_7.setStyleSheet(u"background-color: black;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 540, 371, 41))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Book Seats", None))
        self.seat17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.seat3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.seat7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.seat20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.seat6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.seat10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.seat4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.seat19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.seat16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.seat2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.seat11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.seat14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.seat12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.seat13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.seat9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.seat15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.seat1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.seat5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.seat18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.seat8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Show Time", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Show Date", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hall Id", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Reserve Type", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Payment Type", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Back to Movies", None))
        self.confirmBook.setText(QCoreApplication.translate("MainWindow", u"Confirm Booking", None))
        self.oLabel.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
    # retranslateUi

