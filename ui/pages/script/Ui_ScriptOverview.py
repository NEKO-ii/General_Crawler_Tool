# 由Ui_ConfigurationOverview.py复制并修改
# ///////////////////////////////////////////////////////////////
from ui.preload.imp_qt import (QCoreApplication, QHBoxLayout, QMetaObject, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import PushButton, TableWidget, LineEdit


class Ui_ScriptOverview:

    def __init__(self, ScriptOverview) -> None:
        self.setupUi(ScriptOverview)

    def setupUi(self, ScriptOverview):
        if not ScriptOverview.objectName():
            ScriptOverview.setObjectName(u"ScriptOverview")
        self.verticalLayout = QVBoxLayout(ScriptOverview)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.overviewTopLayout = QHBoxLayout()

        self.btn_new = PushButton(ScriptOverview, type="success")
        self.overviewTopLayout.addWidget(self.btn_new)

        self.btn_edit = PushButton(ScriptOverview, type="primary", tooltip="编辑选中的配置文件\n多选时编辑第一个选中配置")
        self.overviewTopLayout.addWidget(self.btn_edit)

        self.btn_import = PushButton(ScriptOverview, type="primary")
        self.overviewTopLayout.addWidget(self.btn_import)

        self.btn_test = PushButton(ScriptOverview, type="primary")
        self.btn_test.setObjectName("overview_script_test_btn")
        self.overviewTopLayout.addWidget(self.btn_test)

        self.btn_delete = PushButton(ScriptOverview, type="error")
        self.overviewTopLayout.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.overviewTopLayout.addItem(self.horizontalSpacer)

        self.ledit_search = LineEdit(ScriptOverview, placeHolderText="输入关键词搜索")
        self.overviewTopLayout.addWidget(self.ledit_search)

        self.btn_clear = PushButton(ScriptOverview)
        self.overviewTopLayout.addWidget(self.btn_clear)

        self.btn_flush = PushButton(ScriptOverview, type="primary", text="刷新列表")
        self.overviewTopLayout.addWidget(self.btn_flush)

        self.verticalLayout.addLayout(self.overviewTopLayout)

        self.table_overview = TableWidget(ScriptOverview, defaultRowHeight=25, headerPadding=3, extendHeight=True)
        self.table_overview.c_setHeader(["名称", "类型", "文件路径", "更新时间", "说明"], [2])
        self.table_overview.c_setHeaderTooltip([None, "脚本文件类型", "绝对路径", "最后修改的时间"])
        self.table_overview.noEditCols = [1, 2, 3]
        self.table_overview.c_setColWidth([240, 50, None, 160, 350])

        self.verticalLayout.addWidget(self.table_overview)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(ScriptOverview)

    # setupUi

    def retranslateUi(self):
        self.btn_new.setText(QCoreApplication.translate("ScriptOverview", u"\u65b0\u5efa", None))
        self.btn_import.setText(QCoreApplication.translate("ScriptOverview", u"\u5bfc\u5165", None))
        self.btn_edit.setText(QCoreApplication.translate("ScriptOverview", u"\u7f16\u8f91", None))
        self.btn_test.setText(QCoreApplication.translate("ScriptOverview", u"\u6d4b\u8bd5", None))
        self.btn_delete.setText(QCoreApplication.translate("ScriptOverview", u"\u5220\u9664", None))
        self.btn_clear.setText(QCoreApplication.translate("ScriptOverview", u"\u6e05\u7a7a", None))

    # retranslateUi
