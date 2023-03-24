# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_config_overview.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from core.sys import Themes
from ui.preload.imp_qt import (QCoreApplication, QHBoxLayout, QMetaObject, QSizePolicy, QSpacerItem, QTableWidgetItem, QVBoxLayout)
from ui.widgets import PushButton, TableWidget


class Ui_ConfigurationOverview(object):

    def __init__(self, ConfigurationOverview, themes: Themes) -> None:
        self.setupUi(ConfigurationOverview, themes)

    def setupUi(self, ConfigurationOverview, themes: Themes):
        if not ConfigurationOverview.objectName():
            ConfigurationOverview.setObjectName(u"ConfigurationOverview")
        self.verticalLayout = QVBoxLayout(ConfigurationOverview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.overview_top_layout = QHBoxLayout()
        self.overview_top_layout.setObjectName(u"overview_top_layout")
        self.btn_new_config = PushButton(ConfigurationOverview, type="success")
        self.btn_new_config.setObjectName(u"btn_new_config")

        self.overview_top_layout.addWidget(self.btn_new_config)

        self.btn_import = PushButton(ConfigurationOverview, type="primary")
        self.btn_import.setObjectName(u"btn_import")

        self.overview_top_layout.addWidget(self.btn_import)

        self.btn_edit = PushButton(ConfigurationOverview, type="primary", tooltip="编辑选中的配置文件\n多选时编辑第一个选中配置")
        self.btn_edit.setObjectName(u"btn_edit")

        self.overview_top_layout.addWidget(self.btn_edit)

        self.btn_delete = PushButton(ConfigurationOverview, type="error")
        self.btn_delete.setObjectName(u"btn_delete")

        self.overview_top_layout.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.overview_top_layout.addItem(self.horizontalSpacer)

        self.btn_flush = PushButton(ConfigurationOverview, type="primary", text="刷新列表")
        self.btn_flush.setObjectName(u"btn_flush")

        self.overview_top_layout.addWidget(self.btn_flush)

        self.verticalLayout.addLayout(self.overview_top_layout)

        self.table_overview = TableWidget(ConfigurationOverview, default_row_height=25, header_padding=3, fixed_col_width=True, extend_height=True)
        self.table_overview.setObjectName(u"table_overview")
        self.table_overview.set_header(["名称", "文件位置", "时间", "状态", "备注"], [1])
        self.table_overview.set_header_tooltip([None, "该配置对应的JSON文件路径", "最后修改的时间", "R:可运行网络请求\nP:可运行数据解析\nN:不可运行\nFL:配置文件丢失\nU:未知"])
        self.table_overview.no_edit_cols = [1]
        self.table_overview.set_col_width([240, None, 160, 50, 350])

        self.verticalLayout.addWidget(self.table_overview)

        self.retranslateUi(ConfigurationOverview)

        QMetaObject.connectSlotsByName(ConfigurationOverview)

    # setupUi

    def retranslateUi(self, ConfigurationOverview):
        ConfigurationOverview.setWindowTitle(QCoreApplication.translate("ConfigurationOverview", u"Form", None))
        self.btn_new_config.setText(QCoreApplication.translate("ConfigurationOverview", u"\u65b0\u5efa", None))
        self.btn_import.setText(QCoreApplication.translate("ConfigurationOverview", u"\u5bfc\u5165", None))
        self.btn_edit.setText(QCoreApplication.translate("ConfigurationOverview", u"\u7f16\u8f91", None))
        self.btn_delete.setText(QCoreApplication.translate("ConfigurationOverview", u"\u5220\u9664", None))

    # retranslateUi
