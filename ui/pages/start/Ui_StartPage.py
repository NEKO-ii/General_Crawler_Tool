# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_config.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

from core.sys import Themes

from .Ui_StartPageBtn import Ui_StartPageBtn
from .Ui_ProgramRunner import Ui_ProgramRunner


class Ui_StartPage(object):

    def __init__(self, StartPage) -> None:
        self.setupUi(StartPage)
        self.pages.setCurrentWidget(self.btnPage)

    def setupUi(self, StartPage):
        if not StartPage.objectName():
            StartPage.setObjectName(u"StartPage")
        self.verticalLayout = QVBoxLayout(StartPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(StartPage)
        self.pages.setObjectName(u"pages")

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.btnPage = QWidget(self.pages)
        self.btnPage_ui = Ui_StartPageBtn(self.btnPage)
        self.pages.addWidget(self.btnPage)

        self.runPage = QWidget(self.pages)
        self.runPage_ui = Ui_ProgramRunner(self.runPage)
        self.pages.addWidget(self.runPage)

        self.verticalLayout.addWidget(self.pages)

        self.retranslateUi(StartPage)

        QMetaObject.connectSlotsByName(StartPage)

    # setupUi

    def retranslateUi(self, StartPage):
        StartPage.setWindowTitle(QCoreApplication.translate("StartPage", u"Form", None))

    # retranslateUi
