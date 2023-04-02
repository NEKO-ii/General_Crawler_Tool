# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_config_save_message_input.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QDialog, QStyleFactory, QFormLayout, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)
from core.sys import File, SysPath
from ui.widgets import PushButton, LineEdit, TextEdit


class Dialog_ConfigMessageInput(QDialog):

    config_name: str = "新建配置"
    file_name: str = "new_config.json"
    comment: str = ""
    flag_accept: bool = False
    flag_check_pass: bool = False

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("配置保存")
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setFixedSize(400, 220)
        self.setupUi()
        self.btn_connect()

    def btn_connect(self) -> None:
        """按钮点击事件链接"""
        self.btn_reject.clicked.connect(self.btn_reject_clicked)
        self.btn_check.clicked.connect(self.btn_check_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)

    def init_data(self) -> None:
        """初始化控件内容数据"""
        self.flag_accept = False
        self.flag_check_pass = False
        self.config_name = "新建配置"
        self.file_name = "new_config.json"
        self.comment = ""
        self.ledit_config_name.setText(self.config_name)
        self.ledit_file_name.setText(self.file_name)
        self.tedit_comment.setText(self.comment)
        self.set_check_state()

    def set_check_state(self, state: str = "default", err_msg: str = "") -> None:
        """更新检查结果显示标签"""
        if state == "default":
            self.label_check_msg.setText("未检查")
            self.label_check_msg.setStyleSheet("color: #aaaabb;")
        if state == "pass":
            self.label_check_msg.setText("数据可用")
            self.label_check_msg.setStyleSheet("color: #20b05f;")
        if state == "err":
            self.label_check_msg.setText(err_msg)
            self.label_check_msg.setStyleSheet("color: #ff4040;")

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"self")
        self.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ledit_config_name = LineEdit(self)
        self.ledit_config_name.setObjectName(u"ledit_config_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ledit_config_name)

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.ledit_file_name = LineEdit(self)
        self.ledit_file_name.setObjectName(u"ledit_file_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ledit_file_name)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_check_msg = QLabel(self)
        self.label_check_msg.setObjectName(u"label_check_msg")

        self.horizontalLayout_2.addWidget(self.label_check_msg)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tedit_comment = TextEdit(self)
        self.tedit_comment.setObjectName(u"tedit_comment")

        self.verticalLayout.addWidget(self.tedit_comment)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_reject = PushButton(self, type="error")
        self.btn_reject.setObjectName(u"btn_reject")

        self.horizontalLayout.addWidget(self.btn_reject)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_check = PushButton(self, type="primary")
        self.btn_check.setObjectName(u"btn_check")

        self.horizontalLayout.addWidget(self.btn_check)

        self.btn_save = PushButton(self, type="success")
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.label.setText(QCoreApplication.translate("self", u"\u914d\u7f6e\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("self", u"\u6587\u4ef6\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("self", u"\u5907\u6ce8:", None))
        self.label_check_msg.setText(QCoreApplication.translate("self", u"\u4fe1\u606f\u53ef\u7528", None))
        self.btn_reject.setText(QCoreApplication.translate("self", u"\u53d6\u6d88", None))
        self.btn_check.setText(QCoreApplication.translate("self", u"\u68c0\u67e5", None))
        self.btn_save.setText(QCoreApplication.translate("self", u"\u4fdd\u5b58", None))

    # 每次打开时初始化数据并在控件中显示
    def showEvent(self, event) -> None:
        self.init_data()
        return super().showEvent(event)

    def btn_reject_clicked(self) -> None:
        self.flag_accept = False
        self.reject()

    def btn_check_clicked(self) -> None:
        # TODO: 配置同名检查
        passf = True
        if self.ledit_file_name.text() == "":
            passf = False
            self.set_check_state("err", "文件名不能为空")
        if passf:
            file_name = self.ledit_file_name.text()
            if file_name.endswith(".json") is False:
                file_name = file_name + ".json"
                self.ledit_file_name.setText(file_name)
            path = File.path(SysPath.CONFIGURATION, self.ledit_file_name.text())
            for c in [":"]:
                if file_name.find(c) != -1:
                    passf = False
                    self.set_check_state("err", "文件名无效")
        if passf:
            if File.file_exists(path):
                passf = False
                self.set_check_state("err", "文件已存在")
            else:
                try:
                    with open(path, "w", encoding="UTF-8") as file:
                        pass
                    File.delete(path)
                except:
                    passf = False
                    self.set_check_state("err", "文件名无效")
        if passf:
            self.flag_check_pass = True
            self.set_check_state("pass")

    def btn_save_clicked(self) -> None:
        self.btn_check_clicked()
        if self.flag_check_pass:
            self.flag_accept = True
            self.config_name = self.ledit_config_name.text()
            self.file_name = self.ledit_file_name.text()
            self.comment = self.tedit_comment.toPlainText()
            self.accept()

    def exec(self) -> bool:
        super().exec()
        return self.flag_accept
