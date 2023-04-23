# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import PushButton


class Question(QDialog):
    flag_accept: bool = False

    color: dict = {"default": "#aaaabb", "info": "rgb(17, 169, 225)", "warning": "#f0f020", "error": "#ff4040", "success": "#20cc5f"}

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("提示窗口")
        self.setStyleSheet("background-color: #2c313c;")
        self.setFixedSize(400, 160)
        self.setupUi()
        self.btn_connect()

    def btn_connect(self) -> None:
        self.btn_reject.clicked.connect(self.btn_reject_clicked)
        self.btn_accept.clicked.connect(self.btn_accept_clicked)

    def exec(self, title="标题", msg="信息", titleType="info", msgType="default", btnRejectText="取消", btnAcceptText="确认") -> bool:
        self.label_title.setText(title)
        self.label_text.setText(msg)
        self.btn_reject.setText(btnRejectText)
        self.btn_accept.setText(btnAcceptText)
        self.label_title.setStyleSheet(F"color: {self.color[titleType.lower()]};")
        self.label_text.setStyleSheet(F"color: {self.color[msgType.lower()]};")
        super().exec()
        return self.flag_accept

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Question")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(self)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(11)
        self.label_title.setFont(font)
        self.label_title.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_title)

        self.label_text = QLabel(self)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_text)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_reject = PushButton(self, type="error")
        self.btn_reject.setObjectName(u"btn_reject")

        self.horizontalLayout.addWidget(self.btn_reject)

        self.btn_accept = PushButton(self, type="success")
        self.btn_accept.setObjectName(u"btn_accept")

        self.horizontalLayout.addWidget(self.btn_accept)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.label_title.setText(QCoreApplication.translate("Question", u"\u6807\u9898", None))
        self.label_text.setText(QCoreApplication.translate("Question", u"\u5185\u5bb9", None))
        self.btn_reject.setText(QCoreApplication.translate("Question", u"\u53d6\u6d88", None))
        self.btn_accept.setText(QCoreApplication.translate("Question", u"\u786e\u8ba4", None))

    def showEvent(self, event) -> None:
        self.flag_accept = False
        return super().showEvent(event)

    def btn_reject_clicked(self) -> None:
        self.reject()

    def btn_accept_clicked(self) -> None:
        self.flag_accept = True
        self.accept()
