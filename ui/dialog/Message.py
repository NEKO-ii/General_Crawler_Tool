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


class Message(QDialog):

    _msgCount: dict = {"default": 0, "success": 0, "info": 0, "warn": 0, "error": 0}

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setFixedSize(500, 260)
        self.setupUi()
        self.btnConnect()

    def btnConnect(self) -> None:
        """按钮点击事件链接"""
        self.btnConfirm.clicked.connect(self.btn_confirm_clicked)

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"self")
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit = TextEdit(self)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnConfirm = PushButton(self)
        self.btnConfirm.setObjectName(u"btnConfirm")

        self.horizontalLayout.addWidget(self.btnConfirm)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"\u6d88\u606f", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))

    # retranslateUi

    def showEvent(self, event) -> None:
        return super().showEvent(event)

    def btn_confirm_clicked(self):
        self.accept()

    def exec(self):
        super().exec()
        self.clearMsg()

    def appendMsg(self, msg: str, mtype: str = "default") -> None:
        """添加消息后另起一行

        Args:
            msg (str): 消息内容
            colorType (str, optional): 颜色类型[default,info,warn,success,error]. Defaults to "default".
            pre (str, optional): 前缀(不带颜色). Defaults to None.
            after (str, optional): 后缀(不带颜色). Defaults to None.
        """
        preMsg = {"default": "MSG", "info": "INFO", "warn": "WARN", "success": "OK", "error": "ERR"}
        self.textEdit.c_appendWithColor(preMsg[mtype], mtype, "[", F"] {msg}")
        self._msgCount[mtype] += 1

    def isEmptyMsg(self) -> bool:
        """判断消息内容是否为空

        Returns:
            bool: 消息为空返回True,否则返回False
        """
        if self.textEdit.toPlainText().strip() == "":
            return True
        else:
            return False

    def clearMsg(self) -> None:
        """清空消息内容
        """
        self.textEdit.clear()
        self._initMsgCountDict()

    def getMsgCount(self, mtype: str) -> int:
        """获取消息统计数据

        Args:
            mtype (str): 消息类型[default,success,info,warn,error]

        Returns:
            int: 返回统计数量
        """
        return self._msgCount[mtype]

    def _initMsgCountDict(self) -> None:
        """初始化消息类型统计
        """
        self._msgCount = {"default": 0, "success": 0, "info": 0, "warn": 0, "error": 0}

    # def insertMsg(self, msg: str, mtype: str = "default") -> None:
    #     """添加消息后不会另起一行

    #     Args:
    #         msg (str): 消息内容
    #         colorType (str, optional): 颜色类型[default,info,warn,success,error]. Defaults to "default".
    #         pre (str, optional): 前缀(不带颜色). Defaults to None.
    #         after (str, optional): 后缀(不带颜色). Defaults to None.
    #     """
    #     self.textEdit.c_insertWithColor(msg, mtype, pre, after)
