from core.sys import Themes
from ui.preload.imp_qt import (QCoreApplication, QMetaObject, QStackedWidget,
                               QVBoxLayout, QWidget)

from .config import ConfigurationPage
from .start import StartPage
from .ui_test_page3 import Ui_test_page3


class Ui_MainPagesContainer:

    def __init__(self, MainPagesContainer) -> None:
        self.setupUi(MainPagesContainer)

    def setupUi(self, MainPagesContainer):
        if not MainPagesContainer.objectName():
            MainPagesContainer.setObjectName(u"MainPagesContainer")
        self.mainPagesLayout = QVBoxLayout(MainPagesContainer)
        self.mainPagesLayout.setSpacing(0)
        self.mainPagesLayout.setObjectName(u"main_pages_layout")
        self.mainPagesLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(MainPagesContainer)
        self.pages.setObjectName(u"pages")

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.startPage = QWidget(self.pages)
        self.startPage_inner = StartPage(self.startPage)
        self.pages.addWidget(self.startPage)

        self.configPage = QWidget(self.pages)
        self.configPage_inner = ConfigurationPage(self.configPage)
        self.pages.addWidget(self.configPage)

        self.page_3 = QWidget()
        self.test_page3 = Ui_test_page3()
        self.test_page3.setupUi(self.page_3)
        self.pages.addWidget(self.page_3)

        # ///////////////////////////////////////////////////////////////

        self.mainPagesLayout.addWidget(self.pages)

        self.retranslateUi(MainPagesContainer)

        QMetaObject.connectSlotsByName(MainPagesContainer)

    # setupUi

    def retranslateUi(self, MainPagesContainer):
        MainPagesContainer.setWindowTitle(QCoreApplication.translate("MainPagesContainer", u"Form", None))

    # retranslateUi
