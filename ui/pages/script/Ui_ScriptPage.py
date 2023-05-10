# 复制并修改自Ui_ConfigurationPage.py
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

from .Ui_ScriptEditor import Ui_ScriptEditor
from .Ui_ScriptOverview import Ui_ScriptOverview


class Ui_ScriptPage:

    def __init__(self, Script) -> None:
        self.setupUi(Script)
        self.pages.setCurrentWidget(self.overview)

    def setupUi(self, Script):
        if not Script.objectName():
            Script.setObjectName(u"Script")
        self.verticalLayout = QVBoxLayout(Script)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(Script)

        # 添加页面
        # ///////////////////////////////////////////////////////////////
        self.overview = QWidget(self.pages)
        self.overview_ui = Ui_ScriptOverview(self.overview)
        self.pages.addWidget(self.overview)

        self.editor = QWidget(self.pages)
        self.editor_ui = Ui_ScriptEditor(self.editor)
        self.pages.addWidget(self.editor)

        self.verticalLayout.addWidget(self.pages)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(Script)

    # setupUi

    def retranslateUi(self):
        pass

    # retranslateUi
