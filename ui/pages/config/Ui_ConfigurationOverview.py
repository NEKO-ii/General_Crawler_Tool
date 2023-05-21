# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_config_overview.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from ui.preload.imp_qt import (QCoreApplication, QHBoxLayout, QMetaObject, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import PushButton, TableWidget, LineEdit


class Ui_ConfigurationOverview:

    def __init__(self, ConfigurationOverview) -> None:
        self.setupUi(ConfigurationOverview)

    def setupUi(self, ConfigurationOverview):
        if not ConfigurationOverview.objectName():
            ConfigurationOverview.setObjectName(u"ConfigurationOverview")
        self.verticalLayout = QVBoxLayout(ConfigurationOverview)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.overviewTopLayout = QHBoxLayout()
        self.btn_newConfig = PushButton(ConfigurationOverview, type="success")
        self.overviewTopLayout.addWidget(self.btn_newConfig)

        self.btn_edit = PushButton(ConfigurationOverview, type="primary", tooltip="编辑选中的配置文件\n多选时编辑第一个选中配置")
        self.overviewTopLayout.addWidget(self.btn_edit)

        self.btn_import = PushButton(ConfigurationOverview, type="primary")
        self.overviewTopLayout.addWidget(self.btn_import)

        self.btn_upload = PushButton(ConfigurationOverview, type="primary")
        self.overviewTopLayout.addWidget(self.btn_upload)

        self.btn_delete = PushButton(ConfigurationOverview, type="error")
        self.overviewTopLayout.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.overviewTopLayout.addItem(self.horizontalSpacer)

        self.ledit_search = LineEdit(ConfigurationOverview, placeHolderText="输入关键词搜索")
        self.ledit_search.setMinimumWidth(400)
        self.overviewTopLayout.addWidget(self.ledit_search)

        self.btn_clear = PushButton(ConfigurationOverview)
        self.overviewTopLayout.addWidget(self.btn_clear)

        self.btn_flush = PushButton(ConfigurationOverview, type="primary", text="刷新列表")
        self.overviewTopLayout.addWidget(self.btn_flush)

        self.verticalLayout.addLayout(self.overviewTopLayout)

        self.table_overview = TableWidget(ConfigurationOverview, defaultRowHeight=25, headerPadding=3, extendHeight=True)
        self.table_overview.c_setHeader(["名称", "文件位置", "更新时间", "状态", "备注"], [1])
        self.table_overview.c_setHeaderTooltip([None, "该配置对应的JSON文件路径", "最后修改的时间", "R:可运行网络请求\nP:可运行数据解析\nN:不可运行\nFL:配置文件丢失\nU:未知"])
        self.table_overview.noEditCols = [1, 2]
        self.table_overview.c_setColWidth([240, None, 152, 50, 350])

        self.verticalLayout.addWidget(self.table_overview)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(ConfigurationOverview)

    # setupUi

    def retranslateUi(self):
        self.btn_newConfig.setText(QCoreApplication.translate("ConfigurationOverview", u"\u65b0\u5efa", None))
        self.btn_import.setText(QCoreApplication.translate("ConfigurationOverview", u"\u5bfc\u5165", None))
        self.btn_edit.setText(QCoreApplication.translate("ConfigurationOverview", u"\u7f16\u8f91", None))
        self.btn_upload.setText(QCoreApplication.translate("ConfigurationOverview", u"\u4e0a\u4f20", None))
        self.btn_delete.setText(QCoreApplication.translate("ConfigurationOverview", u"\u5220\u9664", None))
        self.btn_clear.setText(QCoreApplication.translate("ConfigurationOverview", u"\u6e05\u7a7a", None))

    # retranslateUi
