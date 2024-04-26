# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userLogin.ui'
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
    QPushButton, QSizePolicy, QWidget)

class UserLogin(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(763, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loginBtn = QPushButton(self.centralwidget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(620, 430, 101, 41))
        font = QFont()
        font.setPointSize(12)
        self.loginBtn.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 250, 121, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setItalic(True)
        self.label_3.setFont(font1)
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 430, 181, 41))
        self.backBtn.setFont(font)
        self.passField = QLineEdit(self.centralwidget)
        self.passField.setObjectName(u"passField")
        self.passField.setGeometry(QRect(210, 260, 201, 28))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 200, 91, 41))
        self.label_2.setFont(font1)
        self.accBtn = QPushButton(self.centralwidget)
        self.accBtn.setObjectName(u"accBtn")
        self.accBtn.setGeometry(QRect(430, 430, 151, 41))
        self.accBtn.setFont(font)
        self.emailField = QLineEdit(self.centralwidget)
        self.emailField.setObjectName(u"emailField")
        self.emailField.setGeometry(QRect(210, 210, 201, 28))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 20, 401, 111))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Back to Homepage", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.accBtn.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Login", None))
    # retranslateUi

