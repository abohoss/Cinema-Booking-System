# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoveShowTime.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 230, 63, 20))
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 360, 141, 51))
        self.label_5.setFont(font)
        self.name = QComboBox(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(220, 170, 241, 28))
        self.Back = QPushButton(self.centralwidget)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(422, 482, 161, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.Back.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 10, 401, 131))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 430, 401, 41))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 160, 141, 41))
        self.label_2.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 300, 81, 31))
        self.label_4.setFont(font)
        self.confirm = QPushButton(self.centralwidget)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(610, 480, 161, 41))
        self.confirm.setFont(font1)
        self.hallnum = QComboBox(self.centralwidget)
        self.hallnum.setObjectName(u"hallnum")
        self.hallnum.setGeometry(QRect(220, 370, 91, 28))
        self.time = QComboBox(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(230, 230, 221, 28))
        self.date = QComboBox(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(230, 300, 211, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 480, 321, 41))
        self.label_7.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hall Number:", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"Back to Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Remove Show Time", None))
        self.label_6.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Movie Name: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_7.setText("")
    # retranslateUi

