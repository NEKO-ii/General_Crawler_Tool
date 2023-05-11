# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TemoviewRead.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
from ui.widgets import PushButton, TextEdit


class Ui_TempviewRead(object):

    def setupUi(self, TempviewRead):
        if not TempviewRead.objectName():
            TempviewRead.setObjectName(u"TempviewRead")
        self.verticalLayout = QVBoxLayout(TempviewRead)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()

        self.btn_back = PushButton(TempviewRead)
        self.horizontalLayout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tedit_view = TextEdit(TempviewRead)
        self.tedit_view.setReadOnly(True)
        self.verticalLayout.addWidget(self.tedit_view)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(TempviewRead)

    # setupUi

    def retranslateUi(self):
        self.btn_back.setText(QCoreApplication.translate("TempviewRead", u"\u8fd4\u56de", None))

    # retranslateUi
