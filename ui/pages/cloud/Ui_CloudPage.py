from .Ui_CloudOverview import Ui_CloudOverview
from .Ui_CloudRead import Ui_CloudRead
from PySide6.QtCore import QMetaObject
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget


class Ui_CloudPage:

    def __init__(self, cloudPageWidget) -> None:
        self.setupUi(cloudPageWidget)
        self.pages.setCurrentWidget(self.overviewPage)

    def setupUi(self, cloudPageWidget):
        if not cloudPageWidget.objectName():
            cloudPageWidget.setObjectName(u"cloudPageWidget")
        self.verticalLayout = QVBoxLayout(cloudPageWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(cloudPageWidget)

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.overviewPage = QWidget(self.pages)
        self.overviewPage_ui = Ui_CloudOverview()
        self.overviewPage_ui.setupUi(self.overviewPage)
        self.pages.addWidget(self.overviewPage)

        self.readPage = QWidget(self.pages)
        self.readPage_ui = Ui_CloudRead()
        self.readPage_ui.setupUi(self.readPage)
        self.pages.addWidget(self.readPage)

        self.verticalLayout.addWidget(self.pages)

        QMetaObject.connectSlotsByName(cloudPageWidget)
