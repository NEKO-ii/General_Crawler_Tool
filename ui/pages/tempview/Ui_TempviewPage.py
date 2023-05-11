from PySide6.QtCore import QMetaObject
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

from .Ui_TemoviewRead import Ui_TempviewRead
from .Ui_TempviewIndex import Ui_TempviewIndex


class Ui_TempviewPage(object):

    def __init__(self, TempviewPage) -> None:
        self.setupUi(TempviewPage)
        self.pages.setCurrentWidget(self.indexPage)

    def setupUi(self, TempviewPage):
        if not TempviewPage.objectName():
            TempviewPage.setObjectName(u"TempviewPage")
        self.verticalLayout = QVBoxLayout(TempviewPage)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(TempviewPage)

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.indexPage = QWidget(self.pages)
        self.indexPage_ui = Ui_TempviewIndex()
        self.indexPage_ui.setupUi(self.indexPage)
        self.pages.addWidget(self.indexPage)

        self.readPage = QWidget(self.pages)
        self.readPage_ui = Ui_TempviewRead()
        self.readPage_ui.setupUi(self.readPage)
        self.pages.addWidget(self.readPage)

        self.verticalLayout.addWidget(self.pages)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(TempviewPage)

    # setupUi

    def retranslateUi(self):
        pass

    # retranslateUi
