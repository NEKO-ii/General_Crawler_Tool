# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_start_run.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)

from core.sys import Themes
from ui.widgets import ComboBox, PushButton, TextEdit


class Ui_ProgramRunner(object):
    def __init__(self, ProgramRunner: QWidget, themes: Themes) -> None:
        self._themes = themes
        self.setupUi(ProgramRunner)

    def setupUi(self, ProgramRunner):
        if not ProgramRunner.objectName():
            ProgramRunner.setObjectName(u"ProgramRunner")
        ProgramRunner.resize(834, 491)
        self.verticalLayout = QVBoxLayout(ProgramRunner)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_layout = QHBoxLayout()
        self.top_layout.setObjectName(u"top_layout")
        self.btn_back = PushButton(ProgramRunner)
        self.btn_back.setObjectName(u"btn_back")

        self.top_layout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_layout.addItem(self.horizontalSpacer)

        self.label = QLabel(ProgramRunner)
        self.label.setObjectName(u"label")

        self.top_layout.addWidget(self.label)

        self.combo_config_select = ComboBox(ProgramRunner, mini_size=[200, 0])
        self.combo_config_select.setObjectName(u"combo_config_select")

        self.top_layout.addWidget(self.combo_config_select)

        self.btn_run = PushButton(ProgramRunner, type="success")
        self.btn_run.setObjectName(u"btn_run")

        self.top_layout.addWidget(self.btn_run)

        self.verticalLayout.addLayout(self.top_layout)

        self.tedit_msg_out = TextEdit(ProgramRunner)
        self.tedit_msg_out.setReadOnly(True)
        # self.tedit_msg_out.setFocusPolicy(Qt.NoFocus)
        self.tedit_msg_out.setObjectName(u"tedit_msg_out")

        self.verticalLayout.addWidget(self.tedit_msg_out)

        self.retranslateUi(ProgramRunner)

        QMetaObject.connectSlotsByName(ProgramRunner)

    # setupUi

    def retranslateUi(self, ProgramRunner):
        ProgramRunner.setWindowTitle(QCoreApplication.translate("ProgramRunner", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("ProgramRunner", u"\u8fd4\u56de", None))
        self.label.setText(QCoreApplication.translate("ProgramRunner", u"\u9009\u62e9\u914d\u7f6e", None))
        self.btn_run.setText(QCoreApplication.translate("ProgramRunner", u"\u8fd0\u884c", None))

    # retranslateUi
