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
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
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
        self.Add.setGeometry(QRect(610, 510, 161, 41))
        font = QFont()
        font.setPointSize(12)
        self.Add.setFont(font)
        self.Add.setCheckable(False)
        self.Add.setChecked(False)
        self.Back = QPushButton(self.centralwidget)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(400, 510, 161, 41))
        self.Back.setFont(font)
        self.cast = QLineEdit(self.centralwidget)
        self.cast.setObjectName(u"cast")
        self.cast.setGeometry(QRect(150, 400, 411, 28))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 260, 121, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_4.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(72, 120, 91, 31))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 190, 81, 31))
        self.label_3.setFont(font1)
        self.genre = QLineEdit(self.centralwidget)
        self.genre.setObjectName(u"genre")
        self.genre.setGeometry(QRect(180, 190, 191, 28))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 0, 221, 91))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 400, 63, 31))
        self.label_5.setFont(font1)
        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(180, 120, 191, 28))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 510, 391, 41))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 360, 531, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.description = QTextEdit(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(220, 260, 431, 85))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 450, 121, 31))
        self.label_9.setFont(font1)
        self.imageUrl = QLineEdit(self.centralwidget)
        self.imageUrl.setObjectName(u"imageUrl")
        self.imageUrl.setGeometry(QRect(190, 450, 411, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Add.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"Back To Home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Genre:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cast:", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Note : Cast must be Comma Separated ( Ahmed, Yehia )", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Image URL:", None))
    # retranslateUi

