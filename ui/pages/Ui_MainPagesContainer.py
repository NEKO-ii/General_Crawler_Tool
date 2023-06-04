from ui.preload.imp_qt import (QCoreApplication, QMetaObject, QStackedWidget, QVBoxLayout, QWidget)

from .config import ConfigurationPage
from .start import StartPage
from .script import ScriptPage
from .tempview import TempviewPage
from .account import AccountPage
from .cloud import CloudPage
from .analysis import AnalysisPage


class Ui_MainPagesContainer:

    def __init__(self, MainPagesContainer) -> None:
        self.setupUi(MainPagesContainer)

    def setupUi(self, MainPagesContainer):
        if not MainPagesContainer.objectName():
            MainPagesContainer.setObjectName(u"MainPagesContainer")
        self.mainPagesLayout = QVBoxLayout(MainPagesContainer)
        self.mainPagesLayout.setSpacing(0)
        self.mainPagesLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(MainPagesContainer)

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.startPage = QWidget(self.pages)
        self.startPage_inner = StartPage(self.startPage)
        self.pages.addWidget(self.startPage)

        self.configPage = QWidget(self.pages)
        self.configPage_inner = ConfigurationPage(self.configPage)
        self.pages.addWidget(self.configPage)

        self.scriptPage = QWidget(self.pages)
        self.scriptPage_inner = ScriptPage(self.scriptPage)
        self.pages.addWidget(self.scriptPage)

        self.tempviewPage = QWidget(self.pages)
        self.tempviewPage_inner = TempviewPage(self.tempviewPage)
        self.pages.addWidget(self.tempviewPage)

        self.accountPage = QWidget(self.pages)
        self.accountPage_inner = AccountPage(self.accountPage)
        self.pages.addWidget(self.accountPage)

        self.cloudPage = QWidget(self.pages)
        self.cloudPage_inner = CloudPage(self.cloudPage)
        self.pages.addWidget(self.cloudPage)

        self.analysisPage = QWidget(self.pages)
        self.analysisPage_inner = AnalysisPage(self.analysisPage)
        self.pages.addWidget(self.analysisPage)

        # ///////////////////////////////////////////////////////////////

        self.mainPagesLayout.addWidget(self.pages)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(MainPagesContainer)

    # setupUi

    def retranslateUi(self):
        pass

    # retranslateUi
