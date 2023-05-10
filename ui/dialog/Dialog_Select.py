# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_Select.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from typing import Optional
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from ui.widgets import PushButton, LineEdit, TableWidget


class Ui_Dialog(QDialog):

    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.setupUi()
        self._btnConnect()
        self._sigConnect()

    def _btnConnect(self) -> None:
        self.btn_close.clicked.connect(self.reject)
        self.btn_confirm.clicked.connect(self.solt_btn_confirm)

    def _sigConnect(self) -> None:
        self.ledit_search.textChanged.connect(self.solt_search)

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Dialog_Select")
        self.resize(750, 400)
        self.verticalLayout = QVBoxLayout(self)
        self.horizontalLayout = QHBoxLayout()

        self.btn_close = PushButton(self)
        self.horizontalLayout.addWidget(self.btn_close)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ledit_search = LineEdit(self, placeHolderText="输入关键词搜索")
        self.ledit_search.setMinimumWidth(400)
        self.horizontalLayout.addWidget(self.ledit_search)

        self.btn_confirm = PushButton(self, type="success")
        self.horizontalLayout.addWidget(self.btn_confirm)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_dataShow = TableWidget(self)
        self.verticalLayout.addWidget(self.table_dataShow)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.btn_close.setText(QCoreApplication.translate("Dialog", u"\u5173\u95ed", None))
        self.btn_confirm.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9", None))

    # retranslateUi

    def solt_btn_confirm(self) -> None:
        self.accept()

    def solt_search(self) -> None:
        pass

    def exec(self) -> None:
        super().exec()
