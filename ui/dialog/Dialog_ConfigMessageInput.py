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
from core.sys import File, SysPath, DataType
from core.static import Define
from ui.widgets import PushButton, LineEdit, TextEdit


class Dialog_ConfigMessageInput(QDialog):

    configName: str = "新建配置"
    fileName: str = "new_config.json"
    comment: str = ""
    flag_accept: bool = False
    flag_checkPass: bool = False
    color: dict

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.color = Define.TYPE_COLOR
        self.setWindowTitle("配置保存")
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setFixedSize(400, 220)
        self.setupUi()
        self._btnConnect()

    def _btnConnect(self) -> None:
        """按钮点击事件链接"""
        self.btn_reject.clicked.connect(self.btn_reject_clicked)
        self.btn_check.clicked.connect(self.btn_check_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)

    def _initData(self) -> None:
        """初始化控件内容数据"""
        self.flag_accept = False
        self.flag_checkPass = False
        self.configName = "新建配置"
        self.fileName = "new_config.json"
        self.comment = ""
        self.ledit_configName.setText(self.configName)
        self.ledit_fileName.setText(self.fileName)
        self.tedit_comment.setText(self.comment)
        self._setCheckState()

    def _setCheckState(self, state: str = "default", msg: str = "") -> None:
        """更新检查结果显示标签"""
        if state == "default":
            self.label_checkMsg.setText("未检查")
            self.label_checkMsg.setStyleSheet("color: #aaaabb;")
        elif state == "pass":
            self.label_checkMsg.setText("数据可用")
            self.label_checkMsg.setStyleSheet("color: #20b05f;")
        elif state == "warn":
            self.label_checkMsg.setText(msg)
            self.label_checkMsg.setStyleSheet("color: #f0f020;")
        elif state == "error":
            self.label_checkMsg.setText(msg)
            self.label_checkMsg.setStyleSheet("color: #ff4040;")

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

        self.ledit_configName = LineEdit(self)
        self.ledit_configName.setObjectName(u"ledit_config_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ledit_configName)

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.ledit_fileName = LineEdit(self)
        self.ledit_fileName.setObjectName(u"ledit_file_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ledit_fileName)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_checkMsg = QLabel(self)
        self.label_checkMsg.setObjectName(u"label_check_msg")

        self.horizontalLayout_2.addWidget(self.label_checkMsg)

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
        self.label_checkMsg.setText(QCoreApplication.translate("self", u"\u4fe1\u606f\u53ef\u7528", None))
        self.btn_reject.setText(QCoreApplication.translate("self", u"\u53d6\u6d88", None))
        self.btn_check.setText(QCoreApplication.translate("self", u"\u68c0\u67e5", None))
        self.btn_save.setText(QCoreApplication.translate("self", u"\u4fdd\u5b58", None))

    # 每次打开时初始化数据并在控件中显示
    def showEvent(self, event) -> None:
        self._initData()
        return super().showEvent(event)

    def btn_reject_clicked(self) -> None:
        self.flag_accept = False
        self.reject()

    def btn_check_clicked(self) -> None:
        passf = True
        warnf = False
        if self.ledit_fileName.text() == "":
            passf = False
            self._setCheckState("error", "文件名不能为空")
        if self.ledit_configName.text() == "":
            passf = False
            self._setCheckState("error", "配置名不能为空")
        if passf:
            fileName = self.ledit_fileName.text()
            if fileName.endswith(".json") is False:
                fileName = fileName + ".json"
                self.ledit_fileName.setText(fileName)
            path = File.path(SysPath.CONFIGURATION, self.ledit_fileName.text())
            if File.checkFileName(fileName) is False:
                passf = False
                self._setCheckState("error", "文件名无效(包含非法字符)")
                return
            if File.isFileExists(path):
                passf = False
                self._setCheckState("error", "文件已存在")
                return
            else:
                try:
                    with open(path, "w", encoding="UTF-8") as file:
                        pass
                    File.delete(path)
                except:
                    passf = False
                    self._setCheckState("error", "文件名无效")
            for item in File.read_opt(File.path(SysPath.CACHE, "local_configuration.dat"), DataType.LIST, "#"):
                if self.ledit_configName.text() == eval(item)[0]:
                    self._setCheckState("warn", "存在同名配置(不会覆盖)")
                    warnf = True
                    break
        if passf:
            self.flag_checkPass = True
            if not warnf: self._setCheckState("pass")

    def btn_save_clicked(self) -> None:
        self.btn_check_clicked()
        if self.flag_checkPass:
            self.flag_accept = True
            self.configName = self.ledit_configName.text()
            self.fileName = self.ledit_fileName.text()
            self.comment = self.tedit_comment.toPlainText()
            self.accept()

    def exec(self) -> bool:
        super().exec()
        return self.flag_accept
