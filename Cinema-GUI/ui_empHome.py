# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'empHome.ui'
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

class EmpHome(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 40, 601, 111))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.AddMovie = QPushButton(self.centralwidget)
        self.AddMovie.setObjectName(u"AddMovie")
        self.AddMovie.setGeometry(QRect(550, 240, 131, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.AddMovie.setFont(font1)
        self.AddShow = QPushButton(self.centralwidget)
        self.AddShow.setObjectName(u"AddShow")
        self.AddShow.setGeometry(QRect(100, 230, 151, 41))
        self.AddShow.setFont(font1)
        self.removeShow = QPushButton(self.centralwidget)
        self.removeShow.setObjectName(u"removeShow")
        self.removeShow.setGeometry(QRect(90, 300, 171, 41))
        self.removeShow.setFont(font1)
        self.removeMovie = QPushButton(self.centralwidget)
        self.removeMovie.setObjectName(u"removeMovie")
        self.removeMovie.setGeometry(QRect(550, 300, 141, 41))
        self.removeMovie.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Employee Cinema Back-End System", None))
        self.AddMovie.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.AddShow.setText(QCoreApplication.translate("MainWindow", u"Add Showtime", None))
        self.removeShow.setText(QCoreApplication.translate("MainWindow", u"Remove Showtime", None))
        self.removeMovie.setText(QCoreApplication.translate("MainWindow", u"Remove Movie", None))
    # retranslateUi

