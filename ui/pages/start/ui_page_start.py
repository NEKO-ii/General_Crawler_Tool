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

from .ui_page_start_btn import Ui_StartPageBtn
from .ui_page_start_run import Ui_ProgramRunner


class Ui_StartPage(object):

    def __init__(self, StartPage, themes: Themes) -> None:
        self._themes = themes
        self.setupUi(StartPage)
        self.pages.setCurrentWidget(self.page_btn)

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
        self.page_btn = QWidget(self.pages)
        self.page_btn_ui = Ui_StartPageBtn(self.page_btn, self._themes)
        self.pages.addWidget(self.page_btn)

        self.page_run = QWidget(self.pages)
        self.page_run_ui = Ui_ProgramRunner(self.page_run, self._themes)
        self.pages.addWidget(self.page_run)

        self.verticalLayout.addWidget(self.pages)

        self.retranslateUi(StartPage)

        QMetaObject.connectSlotsByName(StartPage)

    # setupUi

    def retranslateUi(self, StartPage):
        StartPage.setWindowTitle(QCoreApplication.translate("StartPage", u"Form", None))

    # retranslateUi
