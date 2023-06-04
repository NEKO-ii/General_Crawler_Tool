# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_Select.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QAbstractItemView, QDialog, QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import PushButton, LineEdit, TableWidget


class Select(QDialog):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("选择")
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setupUi()
        self._btnConnect()
        self._sigConnect()

    def _btnConnect(self) -> None:
        self.btn_close.clicked.connect(self.reject)
        self.btn_clear_search.clicked.connect(self.ledit_search.clear)
        self.btn_confirm.clicked.connect(self.accept)

    def _sigConnect(self) -> None:
        self.ledit_search.textChanged.connect(self.solt_search)

    def _initData(self, data, header, cwidth=[]) -> None:
        self.ledit_search.clear()
        self.table_dataShow.clear()
        if header:
            self.table_dataShow.c_setHeader(header)
            if cwidth != []:
                self.table_dataShow.c_setColWidth(cwidth)
            if data:
                self.table_dataShow.c_addRows(data)

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Dialog_Select")
        self.resize(750, 400)
        self.verticalLayout = QVBoxLayout(self)
        self.horizontalLayout = QHBoxLayout()

        self.btn_close = PushButton(self)
        self.horizontalLayout.addWidget(self.btn_close)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ledit_search = LineEdit(self, placeHolderText="输入关键词搜索")
        self.ledit_search.setMinimumWidth(400)
        self.horizontalLayout.addWidget(self.ledit_search)

        self.btn_clear_search = PushButton(self)
        self.horizontalLayout.addWidget(self.btn_clear_search)

        self.btn_confirm = PushButton(self, type="success")
        self.horizontalLayout.addWidget(self.btn_confirm)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_dataShow = TableWidget(self, extendHeight=True)
        self.table_dataShow.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.verticalLayout.addWidget(self.table_dataShow)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.btn_close.setText(QCoreApplication.translate("Dialog", u"\u5173\u95ed", None))
        self.btn_clear_search.setText(QCoreApplication.translate("Dialog", u"\u6e05\u7a7a", None))
        self.btn_confirm.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9", None))

    # retranslateUi

    def solt_search(self, text) -> None:
        if text == "":
            self.table_dataShow.c_setAllHidden(False)
        else:
            self.table_dataShow.c_search(text)

    def exec(self, header: list, data: list, cwidth=[]) -> None:
        """启动该对话框需要传入表格表头以及数据

        Args:
            header (list): 表头列表,表格列数固定位该列表长度
            data (list): 数据列表(二维数组)
            cwidth(list): 列宽度

        Returns:
            tuple[int, list]: 返回选中的数据(二维数组)
        """
        self._initData(data, header, cwidth)
        code = super().exec()
        data: list = None
        if code:
            data = self.table_dataShow.c_getData(onlySelectedRows=True)
        return (code, data)
