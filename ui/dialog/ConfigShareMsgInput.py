# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigShareMsgInput.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from typing import Optional
from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QDialog)
from ui.widgets import PushButton, LineEdit, TextEdit


class ConfigShareMsgInput(QDialog):
    host: str = ""
    doc: str = ""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("配置共享初始化")
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setFixedSize(600, 320)
        self.setupUi()
        self._btnConnect()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"ConfigShareMsgInput")
        self.verticalLayout = QVBoxLayout(self)
        self.hly_top = QHBoxLayout()
        self.lable_1 = QLabel(self)
        self.hly_top.addWidget(self.lable_1)

        self.ledit_host = LineEdit(self)
        self.hly_top.addWidget(self.ledit_host)

        self.verticalLayout.addLayout(self.hly_top)

        self.tedit_doc = TextEdit(self)
        self.verticalLayout.addWidget(self.tedit_doc)

        self.hly_bottom = QHBoxLayout()
        self.lb_check = QLabel(self)
        self.hly_bottom.addWidget(self.lb_check)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_bottom.addItem(self.hs_1)

        self.btn_reject = PushButton(self)
        self.hly_bottom.addWidget(self.btn_reject)

        self.btn_check = PushButton(self)
        self.hly_bottom.addWidget(self.btn_check)

        self.btn_confirm = PushButton(self)
        self.hly_bottom.addWidget(self.btn_confirm)

        self.verticalLayout.addLayout(self.hly_bottom)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.lable_1.setText(QCoreApplication.translate("ConfigShareMsgInput", u"Host:", None))
        self.ledit_host.setPlaceholderText(QCoreApplication.translate("ConfigShareMsgInput", u"\u8f93\u5165\u68c0\u7d22\u57df\u540d", None))
        self.tedit_doc.setPlaceholderText(QCoreApplication.translate("ConfigShareMsgInput", u"\u8f93\u5165\u914d\u7f6e\u8bf4\u660e\u6587\u6863", None))
        self.lb_check.setText(QCoreApplication.translate("ConfigShareMsgInput", u"\u672a\u68c0\u67e5", None))
        self.btn_reject.setText(QCoreApplication.translate("ConfigShareMsgInput", u"\u53d6\u6d88", None))
        self.btn_check.setText(QCoreApplication.translate("ConfigShareMsgInput", u"\u68c0\u67e5", None))
        self.btn_confirm.setText(QCoreApplication.translate("ConfigShareMsgInput", u"\u786e\u8ba4", None))

    # retranslateUi

    def _btnConnect(self) -> None:
        self.btn_reject.clicked.connect(self.reject)
        self.btn_check.clicked.connect(self._check)
        self.btn_confirm.clicked.connect(self.solt_btn_confirm)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def _check(self) -> bool:
        if self.ledit_host.text() == "":
            self.lb_check.setStyleSheet("color: red")
            self.lb_check.setText("域名不能为空")
            return False
        if self.ledit_host.text().find("/") != -1:
            self.lb_check.setStyleSheet("color: red")
            self.lb_check.setText("请使用根域名")
            return False
        self.lb_check.setStyleSheet("color: green")
        self.lb_check.setText("数据可用")
        return True

    # 按钮信号槽
    # ///////////////////////////////////////////////////////////////
    def solt_btn_confirm(self) -> None:
        if self._check():
            self.host = self.ledit_host.text().strip()
            self.doc = self.tedit_doc.toPlainText().strip()
            self.accept()

    def exec(self) -> tuple[bool, str, str]:
        """运行配置分享初始化窗口

        Returns:
            tuple[bool, str, str]: 返回数据[执行结果,Host,Doc]
        """
        code = super().exec()
        return (True if code == 1 else False, self.host, self.doc)
