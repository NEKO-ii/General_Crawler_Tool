# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_page3.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_test_page3(object):

    def setupUi(self, test_page):
        if not test_page.objectName():
            test_page.setObjectName(u"test_page")
        test_page.resize(449, 346)
        self.verticalLayout = QVBoxLayout(test_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(test_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(test_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(test_page)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(test_page)

        QMetaObject.connectSlotsByName(test_page)

    # setupUi

    def retranslateUi(self, test_page):
        test_page.setWindowTitle(QCoreApplication.translate("test_page", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("test_page", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("test_page", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("test_page", u"PushButton", None))

    # retranslateUi
