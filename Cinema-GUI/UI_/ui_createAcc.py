# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createAcc.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class CreateAccount(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 10, 401, 111))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 150, 141, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 200, 141, 41))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 250, 91, 41))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 290, 71, 51))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 340, 101, 41))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 390, 201, 41))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 440, 131, 41))
        self.label_8.setFont(font1)
        self.fName = QLineEdit(self.centralwidget)
        self.fName.setObjectName(u"fName")
        self.fName.setGeometry(QRect(240, 160, 241, 28))
        self.lName = QLineEdit(self.centralwidget)
        self.lName.setObjectName(u"lName")
        self.lName.setGeometry(QRect(240, 210, 241, 28))
        self.emailField = QLineEdit(self.centralwidget)
        self.emailField.setObjectName(u"emailField")
        self.emailField.setGeometry(QRect(240, 260, 241, 28))
        self.phoneField = QLineEdit(self.centralwidget)
        self.phoneField.setObjectName(u"phoneField")
        self.phoneField.setGeometry(QRect(260, 400, 241, 28))
        self.phoneField.setMaxLength(11)
        self.ageField = QLineEdit(self.centralwidget)
        self.ageField.setObjectName(u"ageField")
        self.ageField.setGeometry(QRect(240, 300, 241, 28))
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(240, 450, 241, 28))
        self.mRadio = QRadioButton(self.centralwidget)
        self.mRadio.setObjectName(u"mRadio")
        self.mRadio.setGeometry(QRect(250, 350, 112, 26))
        self.mRadio.setFont(font1)
        self.fRadio = QRadioButton(self.centralwidget)
        self.fRadio.setObjectName(u"fRadio")
        self.fRadio.setGeometry(QRect(350, 350, 112, 26))
        self.fRadio.setFont(font1)
        self.createAccBtn = QPushButton(self.centralwidget)
        self.createAccBtn.setObjectName(u"createAccBtn")
        self.createAccBtn.setGeometry(QRect(600, 520, 151, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.createAccBtn.setFont(font2)
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(420, 520, 151, 41))
        self.backBtn.setFont(font2)
        self.oLabel = QLabel(self.centralwidget)
        self.oLabel.setObjectName(u"oLabel")
        self.oLabel.setGeometry(QRect(10, 520, 401, 41))
        font3 = QFont()
        font3.setPointSize(14)
        self.oLabel.setFont(font3)
        self.oLabel.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.mRadio.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.fRadio.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.createAccBtn.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Back to Login", None))
        self.oLabel.setText("")
    # retranslateUi

