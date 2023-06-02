# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_ScriptTest.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Signal)
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import LineEdit, TextEdit, PushButton


class ScriptTest(QDialog):
    sig_btn_run_clicked = Signal(str, list)
    sig_stop = Signal()

    path: str = None

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("脚本测试")
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setFixedSize(870, 500)
        self.setupUi()
        self._btnConnect()

    def _btnConnect(self) -> None:
        """按钮点击事件链接"""
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_run.clicked.connect(self.sig_run)

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Dialog_ScriptTest")
        self.verticalLayout = QVBoxLayout(self)
        self.horizontalLayout = QHBoxLayout()

        self.btn_close = PushButton(self)
        self.horizontalLayout.addWidget(self.btn_close)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self)
        self.horizontalLayout.addWidget(self.label)

        self.ledit_args = LineEdit(self, placeHolderText="位置参数,以空格分隔")
        self.ledit_args.setMinimumWidth(500)
        self.horizontalLayout.addWidget(self.ledit_args)

        self.btn_run = PushButton(self, type="success")
        self.horizontalLayout.addWidget(self.btn_run)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tedit_msg = TextEdit(self)
        self.tedit_msg.setReadOnly(True)
        self.verticalLayout.addWidget(self.tedit_msg)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.btn_close.setText(QCoreApplication.translate("Dialog_ScriptTest", u"\u5173\u95ed", None))
        self.label.setText(QCoreApplication.translate("Dialog_ScriptTest", u"\u53c2\u6570", None))
        self.btn_run.setText(QCoreApplication.translate("Dialog_ScriptTest", u"\u8fd0\u884c", None))

    # retranslateUi

    def btn_close_clicked(self) -> None:
        self.sig_stop.emit()
        self.reject()

    def sig_run(self) -> None:
        self.tedit_msg.clear()
        self.msgAppend("INFO", "info", "[", "] 测试开始")
        self.msgInsert("INFO", "info", "[", "] 读取文件路径: ")
        self.msgAppend(self.path, "info")
        self.msgInsert("INFO", "info", "[", "] 读取参数列表: ")
        argsStr = self.ledit_args.text()
        if argsStr:
            args = list(self.ledit_args.text().strip().split())
            self.msgAppend(str(args), "info")
        else:
            self.msgAppend("None", "info")
            args = []
        self.msgAppend("INFO", "info", "[", "] 开始运行脚本 ")
        self.sig_btn_run_clicked.emit(self.path, args)

    def msgAppend(self, msg, ctype: str = "default", pre: str = None, end: str = None) -> None:
        self.tedit_msg.c_appendWithColor(msg, ctype, pre, end)

    def msgInsert(self, msg, ctype: str = "default", pre: str = None, end: str = None) -> None:
        self.tedit_msg.c_insertWithColor(msg, ctype, pre, end)

    def exec(self, name: str = None, path: str = None) -> None:
        """显示脚本测试窗口

        Args:
            name (str, optional): 脚本名称. Defaults to None.
            path (str, optional): 脚本路径. Defaults to None.
        """
        self.path = path
        self.ledit_args.clear()
        self.tedit_msg.clear()
        self.tedit_msg.setPlaceholderText(F"加载脚本: {name}\n脚本路径: {path}\n点击运行开始测试")
        super().exec()
