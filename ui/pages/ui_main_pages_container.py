from core.sys import Themes
from ui.preload.imp_qt import (QCoreApplication, QMetaObject, QStackedWidget,
                               QVBoxLayout, QWidget)

from .config import ConfigPage
from .start import StartPage
from .ui_test_page3 import Ui_test_page3


class Ui_MainPagesContainer:

    def __init__(self, MainPagesContainer, themes: Themes) -> None:
        self._themes = themes
        self.setupUi(MainPagesContainer)

    def setupUi(self, MainPagesContainer):
        if not MainPagesContainer.objectName():
            MainPagesContainer.setObjectName(u"MainPagesContainer")
        self.main_pages_layout = QVBoxLayout(MainPagesContainer)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(MainPagesContainer)
        self.pages.setObjectName(u"pages")

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.page_start = QWidget(self.pages)
        self.page_start_inner = StartPage(self.page_start, self._themes)
        self.pages.addWidget(self.page_start)

        self.page_config = QWidget(self.pages)
        self.page_config_inner = ConfigPage(self.page_config, self._themes)
        self.pages.addWidget(self.page_config)

        self.page_3 = QWidget()
        self.test_page3 = Ui_test_page3()
        self.test_page3.setupUi(self.page_3)
        self.pages.addWidget(self.page_3)

        # ///////////////////////////////////////////////////////////////

        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPagesContainer)

        QMetaObject.connectSlotsByName(MainPagesContainer)

    # setupUi

    def retranslateUi(self, MainPagesContainer):
        MainPagesContainer.setWindowTitle(QCoreApplication.translate("MainPagesContainer", u"Form", None))

    # retranslateUi
