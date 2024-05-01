# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'empLogin.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(739, 474)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pField = QLineEdit(self.centralwidget)
        self.pField.setObjectName(u"pField")
        self.pField.setGeometry(QRect(210, 230, 201, 28))
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(390, 400, 181, 41))
        font = QFont()
        font.setPointSize(12)
        self.backBtn.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 401, 111))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.idField = QLineEdit(self.centralwidget)
        self.idField.setObjectName(u"idField")
        self.idField.setGeometry(QRect(210, 180, 201, 28))
        self.loginBtn = QPushButton(self.centralwidget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(590, 400, 101, 41))
        self.loginBtn.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 170, 161, 41))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 220, 121, 41))
        self.label_3.setFont(font2)
        self.oLabel = QLabel(self.centralwidget)
        self.oLabel.setObjectName(u"oLabel")
        self.oLabel.setGeometry(QRect(190, 320, 401, 41))
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
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Back to Homepage", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Employee Login", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Employee Id:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.oLabel.setText("")
    # retranslateUi

