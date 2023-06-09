# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_config_json.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout)

from ui.widgets import PushButton, TextEdit


class Ui_ConfigJsonEditor:

    def __init__(self, ConfigurationJson) -> None:
        self.setupUi(ConfigurationJson)

    def setupUi(self, ConfigurationJson):
        if not ConfigurationJson.objectName():
            ConfigurationJson.setObjectName(u"ConfigurationJson")
        self.verticalLayout = QVBoxLayout(ConfigurationJson)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.jsonTopLayout = QHBoxLayout()
        self.jsonTopLayout.setObjectName(u"json_top_layout")
        self.btn_back = PushButton(ConfigurationJson)
        self.btn_back.setObjectName(u"btn_back")

        self.jsonTopLayout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.jsonTopLayout.addItem(self.horizontalSpacer)

        self.btn_default = PushButton(ConfigurationJson, type="warning")
        self.btn_default.setObjectName(u"btn_default")

        self.jsonTopLayout.addWidget(self.btn_default)

        self.btn_confirm = PushButton(ConfigurationJson, type="success")
        self.btn_confirm.setObjectName(u"btn_confirm")

        self.jsonTopLayout.addWidget(self.btn_confirm)

        self.verticalLayout.addLayout(self.jsonTopLayout)

        self.tedit_editor = TextEdit(ConfigurationJson, fontSize=10)
        self.tedit_editor.setObjectName(u"tedit_editor")

        self.verticalLayout.addWidget(self.tedit_editor)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(ConfigurationJson)

    # setupUi

    def retranslateUi(self):
        self.btn_back.setText(QCoreApplication.translate("ConfigurationJson", u"\u8fd4\u56de", None))
        self.btn_default.setText(QCoreApplication.translate("ConfigurationJson", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.btn_confirm.setText(QCoreApplication.translate("ConfigurationJson", u"完成", None))

    # retranslateUi
