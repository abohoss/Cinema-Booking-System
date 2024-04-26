# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddMovie.ui'
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

class MovieAdd(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Add = QPushButton(self.centralwidget)
        self.Add.setObjectName(u"Add")
        self.Add.setGeometry(QRect(638, 470, 121, 41))
        self.Back = QPushButton(self.centralwidget)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(50, 470, 121, 41))
        self.cast = QLineEdit(self.centralwidget)
        self.cast.setObjectName(u"cast")
        self.cast.setGeometry(QRect(180, 390, 411, 28))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 270, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(72, 120, 101, 20))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(72, 190, 63, 20))
        self.label_3.setFont(font)
        self.genre = QLineEdit(self.centralwidget)
        self.genre.setObjectName(u"genre")
        self.genre.setGeometry(QRect(180, 190, 191, 28))
        self.description = QLineEdit(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(180, 270, 411, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 0, 221, 91))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.label.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 390, 63, 31))
        self.label_5.setFont(font)
        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(180, 120, 191, 28))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 470, 391, 41))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_6.setFont(font2)
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
        self.Add.setText(QCoreApplication.translate("MainWindow", u"confirm", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"Back To Home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Genre:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cast:", None))
        self.label_6.setText("")
    # retranslateUi

