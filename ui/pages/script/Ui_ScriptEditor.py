# 复制并修改自: Ui_ConfigJsonEditor.py
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout)

from ui.widgets import PushButton, TextEdit, ComboBox


class Ui_ScriptEditor:

    def __init__(self, ScriptEditor) -> None:
        self.setupUi(ScriptEditor)

    def setupUi(self, ScriptEditor):
        if not ScriptEditor.objectName():
            ScriptEditor.setObjectName(u"ConfigurationJson")
        self.verticalLayout = QVBoxLayout(ScriptEditor)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout = QHBoxLayout()

        self.btn_back = PushButton(ScriptEditor)
        self.topLayout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.topLayout.addItem(self.horizontalSpacer)

        self.combo_template = ComboBox(ScriptEditor)
        self.combo_template.addItems(["-选择模版-", "Python脚本", "JS脚本"])
        self.topLayout.addWidget(self.combo_template)

        self.btn_default = PushButton(ScriptEditor, type="warning")
        self.topLayout.addWidget(self.btn_default)

        self.btn_test = PushButton(ScriptEditor, type="primary")
        self.btn_test.setObjectName("edit_script_test_btn")
        self.topLayout.addWidget(self.btn_test)

        self.btn_save_as = PushButton(ScriptEditor, type="primary")
        self.topLayout.addWidget(self.btn_save_as)

        self.btn_save = PushButton(ScriptEditor, type="success")
        self.topLayout.addWidget(self.btn_save)

        self.verticalLayout.addLayout(self.topLayout)

        self.tedit_editor = TextEdit(ScriptEditor, fontSize=10, placeHolderText="选择一个模版后开始编辑")
        self.verticalLayout.addWidget(self.tedit_editor)

        self.retranslateUi(ScriptEditor)

        QMetaObject.connectSlotsByName(ScriptEditor)

    # setupUi

    def retranslateUi(self, ScriptEditor):
        self.btn_back.setText(QCoreApplication.translate("ScriptEditor", u"\u8fd4\u56de", None))
        self.btn_default.setText(QCoreApplication.translate("ScriptEditor", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.btn_test.setText(QCoreApplication.translate("ScriptEditor", u"\u6d4b\u8bd5", None))
        self.btn_save_as.setText(QCoreApplication.translate("ScriptEditor", u"\u53e6\u5b58\u4e3a", None))
        self.btn_save.setText(QCoreApplication.translate("ScriptEditor", u"\u4fdd\u5b58", None))

    # retranslateUi
