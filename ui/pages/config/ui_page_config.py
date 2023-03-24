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

from .ui_page_config_editor import Ui_ConfigurationEditor
from .ui_page_config_json import Ui_ConfigurationJson
from .ui_page_config_overview import Ui_ConfigurationOverview


class Ui_Configuration(object):

    def __init__(self, Configuration, themes: Themes) -> None:
        self._themes = themes
        self.setupUi(Configuration)
        self.pages.setCurrentWidget(self.page_overview)

    def setupUi(self, Configuration):
        if not Configuration.objectName():
            Configuration.setObjectName(u"Configuration")
        self.verticalLayout = QVBoxLayout(Configuration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(Configuration)
        self.pages.setObjectName(u"pages")

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.page_overview = QWidget(self.pages)
        self.page_overview_ui = Ui_ConfigurationOverview(self.page_overview, self._themes)
        self.pages.addWidget(self.page_overview)

        self.page_editor = QWidget(self.pages)
        self.page_editor_ui = Ui_ConfigurationEditor(self.page_editor, self._themes)
        self.pages.addWidget(self.page_editor)

        self.page_json = QWidget(self.pages)
        self.page_json_ui = Ui_ConfigurationJson(self.page_json, self._themes)
        self.pages.addWidget(self.page_json)

        self.verticalLayout.addWidget(self.pages)

        self.retranslateUi(Configuration)

        QMetaObject.connectSlotsByName(Configuration)

    # setupUi

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(QCoreApplication.translate("Configuration", u"Form", None))

    # retranslateUi
