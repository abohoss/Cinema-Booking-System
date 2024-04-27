# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoveMovie.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(734, 509)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 0, 331, 161))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 240, 131, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(270, 250, 201, 31))
        self.confirm = QPushButton(self.centralwidget)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(550, 390, 101, 41))
        self.Back = QPushButton(self.centralwidget)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(50, 390, 121, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 734, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Remove Movie", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Movie Name:", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"Back To Home", None))
    # retranslateUi

