# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Input.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import PushButton, TextEdit


class Inputer(QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setFixedSize(500, 260)
        self.setupUi()
        self.btnConnect()

    def btnConnect(self) -> None:
        """按钮点击事件链接"""
        self.btnConfirm.clicked.connect(self.btn_confirm_clicked)
        self.btnReject.clicked.connect(self.btn_reject_clicked)

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"self")
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit = TextEdit(self)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setAcceptRichText(False)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnConfirm = PushButton(self)
        self.btnConfirm.setObjectName(u"btnConfirm")

        self.horizontalLayout.addWidget(self.btnConfirm)

        self.btnReject = PushButton(self)
        self.btnReject.setObjectName(u"btnReject")

        self.horizontalLayout.addWidget(self.btnReject)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnReject.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))

    # retranslateUi

    def showEvent(self, event) -> None:
        self.textEdit.clear()
        return super().showEvent(event)

    def btn_confirm_clicked(self):
        self.accept()

    def btn_reject_clicked(self):
        self.reject()

    def exec(self) -> tuple[int, str]:
        data = (super().exec(), self.textEdit.toPlainText())
        return data
