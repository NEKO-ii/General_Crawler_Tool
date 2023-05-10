# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_start_run.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from ui.widgets import ComboBox, PushButton, TextEdit


class Ui_ProgramRunner(object):

    def __init__(self, ProgramRunner: QWidget) -> None:
        self.setupUi(ProgramRunner)

    def setupUi(self, ProgramRunner):
        if not ProgramRunner.objectName():
            ProgramRunner.setObjectName(u"ProgramRunner")
        ProgramRunner.resize(834, 491)
        self.verticalLayout = QVBoxLayout(ProgramRunner)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"top_layout")
        self.btn_back = PushButton(ProgramRunner)
        self.btn_back.setObjectName(u"btn_back")

        self.topLayout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(ProgramRunner)
        self.label.setObjectName(u"label")

        self.topLayout.addWidget(self.label)

        self.combo_configSelector = ComboBox(ProgramRunner, minimumSize=[200, 0])
        self.combo_configSelector.setObjectName(u"combo_config_select")

        self.topLayout.addWidget(self.combo_configSelector)

        self.btn_run = PushButton(ProgramRunner, type="success")
        self.btn_run.setObjectName(u"btn_run")

        self.topLayout.addWidget(self.btn_run)

        self.verticalLayout.addLayout(self.topLayout)

        self.tedit_msgOutput = TextEdit(ProgramRunner)
        self.tedit_msgOutput.setReadOnly(True)
        # self.tedit_msg_out.setFocusPolicy(Qt.NoFocus)
        self.tedit_msgOutput.setObjectName(u"tedit_msg_out")

        self.verticalLayout.addWidget(self.tedit_msgOutput)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(ProgramRunner)

    # setupUi

    def retranslateUi(self):
        self.btn_back.setText(QCoreApplication.translate("ProgramRunner", u"\u8fd4\u56de", None))
        self.label.setText(QCoreApplication.translate("ProgramRunner", u"\u9009\u62e9\u914d\u7f6e", None))
        self.btn_run.setText(QCoreApplication.translate("ProgramRunner", u"\u8fd0\u884c", None))

    # retranslateUi
