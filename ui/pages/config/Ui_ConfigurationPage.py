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

from .Ui_ConfigurationEditor import Ui_ConfigurationEditor
from .Ui_ConfigJsonEditor import Ui_ConfigJsonEditor
from .Ui_ConfigurationOverview import Ui_ConfigurationOverview


class Ui_ConfigurationPage:

    def __init__(self, Configuration) -> None:
        self.setupUi(Configuration)
        self.pages.setCurrentWidget(self.overviewPage)

    def setupUi(self, Configuration):
        if not Configuration.objectName():
            Configuration.setObjectName(u"Configuration")
        self.verticalLayout = QVBoxLayout(Configuration)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(Configuration)

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.overviewPage = QWidget(self.pages)
        self.overviewPage_ui = Ui_ConfigurationOverview(self.overviewPage)
        self.pages.addWidget(self.overviewPage)

        self.editorPage = QWidget(self.pages)
        self.editorPage_ui = Ui_ConfigurationEditor(self.editorPage)
        self.pages.addWidget(self.editorPage)

        self.jsonEditPage = QWidget(self.pages)
        self.jsonEditPage_ui = Ui_ConfigJsonEditor(self.jsonEditPage)
        self.pages.addWidget(self.jsonEditPage)

        self.verticalLayout.addWidget(self.pages)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(Configuration)

    # setupUi

    def retranslateUi(self):
        pass

    # retranslateUi
