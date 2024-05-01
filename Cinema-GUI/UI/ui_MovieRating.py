# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MovieRating.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 200, 141, 41))
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.Back = QPushButton(self.centralwidget)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(100, 480, 121, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 20, 331, 161))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 480, 291, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.confirm = QPushButton(self.centralwidget)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(600, 480, 101, 41))
        self.name = QComboBox(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(330, 210, 241, 28))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 280, 141, 41))
        self.label_4.setFont(font)
        self.rating = QComboBox(self.centralwidget)
        self.rating.setObjectName(u"rating")
        self.rating.setGeometry(QRect(330, 290, 111, 28))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 370, 141, 41))
        self.label_5.setFont(font)
        self.comment = QLineEdit(self.centralwidget)
        self.comment.setObjectName(u"comment")
        self.comment.setGeometry(QRect(330, 380, 261, 31))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 490, 341, 31))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Movie name:", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"Back To Movies", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rate Movie", None))
        self.label_3.setText("")
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rating:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Comment:", None))
        self.label_6.setText("")
    # retranslateUi

