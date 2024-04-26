# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddShowTime.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class ShowAdd(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(172, 330, 81, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 400, 91, 20))
        self.Back = QPushButton(self.centralwidget)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(52, 470, 121, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(172, 190, 101, 20))
        self.time = QLineEdit(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(280, 260, 191, 28))
        self.date = QLineEdit(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(280, 330, 351, 28))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(212, 480, 371, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.hallnum = QLineEdit(self.centralwidget)
        self.hallnum.setObjectName(u"hallnum")
        self.hallnum.setGeometry(QRect(280, 400, 351, 28))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 0, 331, 131))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.label.setFont(font1)
        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(280, 190, 191, 28))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(172, 260, 63, 20))
        self.Add = QPushButton(self.centralwidget)
        self.Add.setObjectName(u"Add")
        self.Add.setGeometry(QRect(640, 470, 121, 41))
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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hall number:", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"Back To Home", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Movie name:", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add Show Time", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.Add.setText(QCoreApplication.translate("MainWindow", u"confirm", None))
    # retranslateUi

