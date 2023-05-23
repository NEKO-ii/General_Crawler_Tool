# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_start_run.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from ui.widgets import LineEdit, PushButton, TextEdit


class Ui_ProgramRunner(object):

    def __init__(self, ProgramRunner: QWidget) -> None:
        self.setupUi(ProgramRunner)

    def setupUi(self, ProgramRunner):
        if not ProgramRunner.objectName():
            ProgramRunner.setObjectName(u"ProgramRunner")
        ProgramRunner.resize(834, 491)
        self.verticalLayout = QVBoxLayout(ProgramRunner)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout = QHBoxLayout()
        self.btn_back = PushButton(ProgramRunner)
        self.topLayout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.topLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(ProgramRunner)
        self.topLayout.addWidget(self.label)

        self.ledit_configShow = LineEdit(ProgramRunner, placeHolderText="未选择任何配置")
        self.ledit_configShow.setReadOnly(True)
        self.ledit_configShow.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.topLayout.addWidget(self.ledit_configShow)

        self.btn_searchOnline = PushButton(ProgramRunner, type="primary")
        self.topLayout.addWidget(self.btn_searchOnline)

        self.btn_configSelector = PushButton(ProgramRunner, type="primary")
        self.topLayout.addWidget(self.btn_configSelector)

        self.btn_remove = PushButton(ProgramRunner, type="error")
        self.topLayout.addWidget(self.btn_remove)

        self.btn_run = PushButton(ProgramRunner, type="success")
        self.topLayout.addWidget(self.btn_run)

        self.verticalLayout.addLayout(self.topLayout)

        self.tedit_msgOutput = TextEdit(ProgramRunner)
        self.tedit_msgOutput.setReadOnly(True)
        self.verticalLayout.addWidget(self.tedit_msgOutput)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(ProgramRunner)

    # setupUi

    def retranslateUi(self):
        self.btn_back.setText(QCoreApplication.translate("ProgramRunner", u"\u8fd4\u56de", None))
        self.label.setText(QCoreApplication.translate("ProgramRunner", u"\u9009\u62e9\u914d\u7f6e", None))
        self.btn_run.setText(QCoreApplication.translate("ProgramRunner", u"\u8fd0\u884c", None))
        self.btn_configSelector.setText(QCoreApplication.translate("ProgramRunner", u"\u672c\u5730\u914d\u7f6e", None))
        self.btn_searchOnline.setText(QCoreApplication.translate("ProgramRunner", u"\u4e91\u7aef\u641c\u7d22", None))
        self.btn_remove.setText(QCoreApplication.translate("ProgramRunner", u"\u6e05\u9664\u914d\u7f6e", None))

    # retranslateUi
