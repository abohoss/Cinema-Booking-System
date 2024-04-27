# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.userBtn = QPushButton(self.centralwidget)
        self.userBtn.setObjectName(u"userBtn")
        self.userBtn.setGeometry(QRect(520, 460, 141, 61))
        font = QFont()
        font.setPointSize(14)
        self.userBtn.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 200, 471, 121))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 50, 401, 111))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.empBtn = QPushButton(self.centralwidget)
        self.empBtn.setObjectName(u"empBtn")
        self.empBtn.setGeometry(QRect(140, 460, 141, 61))
        self.empBtn.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 290, 361, 91))
        font3 = QFont()
        font3.setPointSize(12)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.userBtn.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome to Cinema Booking System", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cinema Booking System", None))
        self.empBtn.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Press Employee or User to continue...", None))
    # retranslateUi

