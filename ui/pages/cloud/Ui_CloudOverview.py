# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CloudOverview.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (Qt, QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import PushButton, LineEdit, ComboBox, TableWidget


class Ui_CloudOverview(object):

    def setupUi(self, CloudOverview):
        if not CloudOverview.objectName():
            CloudOverview.setObjectName(u"CloudOverview")
        self.verticalLayout = QVBoxLayout(CloudOverview)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hly_top = QHBoxLayout()
        self.btn_read = PushButton(CloudOverview, type="primary")
        self.hly_top.addWidget(self.btn_read)

        self.btn_download = PushButton(CloudOverview, type="success")
        self.hly_top.addWidget(self.btn_download)

        self.btn_delete = PushButton(CloudOverview, type="error")
        self.hly_top.addWidget(self.btn_delete)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.hly_top.addItem(self.hs_1)

        self.combo_select = ComboBox(CloudOverview)
        self.combo_select.addItem("")
        self.combo_select.addItem("")
        self.combo_select.addItem("")
        self.hly_top.addWidget(self.combo_select)

        self.ledit_fillter = LineEdit(CloudOverview)
        self.ledit_fillter.setFixedWidth(400)
        self.hly_top.addWidget(self.ledit_fillter)

        self.btn_clear = PushButton(CloudOverview)
        self.hly_top.addWidget(self.btn_clear)

        self.hs_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_top.addItem(self.hs_2)

        self.bl_1 = QLabel(CloudOverview)
        self.hly_top.addWidget(self.bl_1)

        self.ledit_count = LineEdit(CloudOverview, color_enabled="#568af2")
        self.ledit_count.setFixedWidth(100)
        self.ledit_count.setReadOnly(True)
        self.ledit_count.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.hly_top.addWidget(self.ledit_count)

        self.verticalLayout.addLayout(self.hly_top)

        self.table_overview = TableWidget(CloudOverview, extendHeight=True)
        self.table_overview.c_setHeader(["配置名称", "文件名称", "位置", "上传时间", "更新时间", "状态", "域名", "注释", "操作", "id"], [6, 7])
        self.table_overview.setColumnHidden(9, True)
        self.table_overview.c_setColWidth([200, 200, 45, 152, 152, 45, None, None, 120])
        self.table_overview.c_setHeaderTooltip(["配置在云端保存的名称", "云端配置文件名称", "配置所在位置", "配置上传到云端的时间", "配置在云端最后更新的时间", "配置共享状态", "共享后的搜索域名\n其他人将根据该域名搜索到本共享配置"])
        self.verticalLayout.addWidget(self.table_overview)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(CloudOverview)

    # setupUi

    def retranslateUi(self):
        self.btn_read.setText(QCoreApplication.translate("CloudOverview", u"\u67e5\u770b", None))
        self.btn_download.setText(QCoreApplication.translate("CloudOverview", u"\u4e0b\u8f7d", None))
        self.btn_delete.setText(QCoreApplication.translate("CloudOverview", u"\u5220\u9664", None))
        self.combo_select.setItemText(0, QCoreApplication.translate("CloudOverview", u"\u6240\u6709", None))
        self.combo_select.setItemText(1, QCoreApplication.translate("CloudOverview", u"\u79c1\u4eba", None))
        self.combo_select.setItemText(2, QCoreApplication.translate("CloudOverview", u"\u5171\u4eab", None))

        self.ledit_fillter.setPlaceholderText(QCoreApplication.translate("CloudOverview", u"\u8f93\u5165\u5173\u952e\u8bcd\u68c0\u7d22", None))
        self.btn_clear.setText(QCoreApplication.translate("CloudOverview", u"\u6e05\u7a7a", None))
        self.bl_1.setText(QCoreApplication.translate("CloudOverview", u"\u5df2\u7528\u5bb9\u91cf", None))

    # retranslateUi
