# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'success.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 355)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 30, 411, 81))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: Green;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 90, 301, 71))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.seatsLabel = QLabel(self.centralwidget)
        self.seatsLabel.setObjectName(u"seatsLabel")
        self.seatsLabel.setGeometry(QRect(210, 170, 391, 41))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.seatsLabel.setFont(font2)
        self.seatsLabel.setAlignment(Qt.AlignCenter)
        self.priceLabel = QLabel(self.centralwidget)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setGeometry(QRect(210, 230, 391, 41))
        self.priceLabel.setFont(font2)
        self.priceLabel.setAlignment(Qt.AlignCenter)
        self.returnBtn = QPushButton(self.centralwidget)
        self.returnBtn.setObjectName(u"returnBtn")
        self.returnBtn.setGeometry(QRect(310, 300, 171, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.returnBtn.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reservation Successful", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Happy Movies!", None))
        self.seatsLabel.setText("")
        self.priceLabel.setText("")
        self.returnBtn.setText(QCoreApplication.translate("MainWindow", u"Return to Movies", None))
    # retranslateUi

