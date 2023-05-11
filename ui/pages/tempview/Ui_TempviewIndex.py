# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TempviewIndex.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QAbstractItemView, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)

from ui.widgets import ComboBox, LineEdit, PushButton, TableWidget


class Ui_TempviewIndex(object):

    def setupUi(self, Ui_TempviewIndex):
        if not Ui_TempviewIndex.objectName():
            Ui_TempviewIndex.setObjectName(u"Ui_TempviewIndex")
        self.verticalLayout = QVBoxLayout(Ui_TempviewIndex)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()

        self.btn_read = PushButton(Ui_TempviewIndex, type="primary")
        self.horizontalLayout.addWidget(self.btn_read)

        self.btn_export = PushButton(Ui_TempviewIndex, type="primary")
        self.horizontalLayout.addWidget(self.btn_export)

        self.btn_delete = PushButton(Ui_TempviewIndex, type="error")
        self.horizontalLayout.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.combo_chooseView = ComboBox(Ui_TempviewIndex)
        self.combo_chooseView.addItems(["网络请求临时数据", "数据解析临时数据"])
        self.horizontalLayout.addWidget(self.combo_chooseView)

        self.btn_flush = PushButton(Ui_TempviewIndex)
        self.horizontalLayout.addWidget(self.btn_flush)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_clearSelect = PushButton(Ui_TempviewIndex)
        self.horizontalLayout.addWidget(self.btn_clearSelect)

        self.ledit_select = LineEdit(Ui_TempviewIndex, placeHolderText="输入关键词以搜索")
        self.ledit_select.setMinimumWidth(300)
        self.horizontalLayout.addWidget(self.ledit_select)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(Ui_TempviewIndex)
        self.horizontalLayout.addWidget(self.label)

        self.ledit_fileCount = LineEdit(Ui_TempviewIndex)
        self.ledit_fileCount.setMaximumWidth(80)
        self.ledit_fileCount.setFocusPolicy(Qt.NoFocus)
        self.ledit_fileCount.setReadOnly(True)
        self.horizontalLayout.addWidget(self.ledit_fileCount)

        self.label_2 = QLabel(Ui_TempviewIndex)
        self.horizontalLayout.addWidget(self.label_2)

        self.ledit_sizeCount = LineEdit(Ui_TempviewIndex)
        self.ledit_sizeCount.setMaximumWidth(80)
        self.ledit_sizeCount.setFocusPolicy(Qt.NoFocus)
        self.ledit_sizeCount.setReadOnly(True)
        self.horizontalLayout.addWidget(self.ledit_sizeCount)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_overview = TableWidget(Ui_TempviewIndex, extendHeight=True, autoColWidth=True)
        self.table_overview.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.verticalLayout.addWidget(self.table_overview)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(Ui_TempviewIndex)

    # setupUi

    def retranslateUi(self):
        self.btn_read.setText(QCoreApplication.translate("Ui_TempviewIndex", u"\u67e5\u770b", None))
        self.btn_export.setText(QCoreApplication.translate("Ui_TempviewIndex", u"\u5bfc\u51fa", None))
        self.btn_delete.setText(QCoreApplication.translate("Ui_TempviewIndex", u"\u5220\u9664", None))
        self.btn_clearSelect.setText(QCoreApplication.translate("Ui_TempviewIndex", u"\u6e05\u7a7a", None))
        self.btn_flush.setText(QCoreApplication.translate("Ui_TempviewIndex", u"\u5237\u65b0\u5217\u8868", None))
        self.label.setText(QCoreApplication.translate("Ui_TempviewIndex", u"\u6587\u4ef6\u603b\u6570:", None))
        self.label_2.setText(QCoreApplication.translate("Ui_TempviewIndex", u"\u5b58\u50a8\u5360\u7528:", None))

    # retranslateUi
