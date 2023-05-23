# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigOnlineSearcher.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, Signal)
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import LineEdit, PushButton, TableWidget, TextEdit
from .Notice import Notice
from core.sys.cloud import getSharedConfig, getConfigDoc, getConfigContent, getConfigInfo
from core.sys.file import File, SysPath


class ConfigOnlineSearcher(QDialog):
    sig_tempConfCreated = Signal(str, str)
    rowIndex: int = -1
    configId: int = 0
    userId: int = 0
    configFileName: str = ""
    flag_dataAddComplet: bool = False

    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setupUi()
        self._btnConnect()
        self._sigConnect()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"ConfigOnlineSearcher")
        self.setFixedSize(1180, 450)
        self.verticalLayout = QVBoxLayout(self)
        self.hly_top = QHBoxLayout()

        self.btn_close = PushButton(self, type="error")
        self.hly_top.addWidget(self.btn_close)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_top.addItem(self.hs_1)

        self.label = QLabel(self)
        self.hly_top.addWidget(self.label)

        self.ledit_host = LineEdit(self)
        self.hly_top.addWidget(self.ledit_host)

        self.btn_search = PushButton(self, type="primary")
        self.hly_top.addWidget(self.btn_search)

        self.btn_confirm = PushButton(self, type="success")
        self.hly_top.addWidget(self.btn_confirm)

        self.verticalLayout.addLayout(self.hly_top)

        self.hly_2 = QHBoxLayout()

        self.table_view = TableWidget(self, extendHeight=True)
        self.table_view.c_setHeader(["配置名称", "作者", "更新时间", "注释", "id"], stretchCols=[3, 4])
        self.table_view.setColumnHidden(4, True)
        self.table_view.c_setColWidth([200, 100, 154])
        self.table_view.setEditTriggers(TableWidget.EditTrigger.NoEditTriggers)
        self.table_view.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.hly_2.addWidget(self.table_view)

        self.tedit_doc = TextEdit(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.tedit_doc.setSizePolicy(sizePolicy)
        self.tedit_doc.setFixedWidth(380)
        self.tedit_doc.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.tedit_doc.setReadOnly(True)

        self.hly_2.addWidget(self.tedit_doc)

        self.verticalLayout.addLayout(self.hly_2)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("ConfigOnlineSearcher", u"\u516c\u5f00\u914d\u7f6e\u641c\u7d22", None))
        self.btn_close.setText(QCoreApplication.translate("ConfigOnlineSearcher", u"\u5173\u95ed", None))
        self.label.setText(QCoreApplication.translate("ConfigOnlineSearcher", u"\u76ee\u6807\u57df\u540d:", None))
        self.ledit_host.setPlaceholderText(QCoreApplication.translate("ConfigOnlineSearcher", u"\u8bf7\u8f93\u5165\u76ee\u6807\u7f51\u7ad9\u6839\u57df\u540d", None))
        self.btn_search.setText(QCoreApplication.translate("ConfigOnlineSearcher", u"\u641c\u7d22", None))
        self.btn_confirm.setText(QCoreApplication.translate("ConfigOnlineSearcher", u"\u786e\u8ba4", None))

    def _btnConnect(self) -> None:
        self.btn_close.clicked.connect(self.reject)
        self.btn_search.clicked.connect(self.solt_search)
        self.btn_confirm.clicked.connect(self.solt_confirm)

    def _sigConnect(self) -> None:
        self.table_view.cellClicked.connect(self.solt_get_doc)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def exec(self) -> dict:
        super().exec()
        self.table_view.clear()
        self.ledit_host.clear()
        self.tedit_doc.clear()

    # 按钮响应
    # ///////////////////////////////////////////////////////////////
    def solt_search(self) -> None:
        host = self.ledit_host.text().strip()
        if host == "":
            Notice().exec("提示", "请先输入域名再进行搜索")
        else:
            resp = getSharedConfig(host)
            if resp["flag"]:
                datas = resp["data"]
                self.flag_dataAddComplet = False
                for data in datas:
                    row = [data["configName"], data["username"], data["updateTime"], data["comment"], str(data["configId"])]
                    self.table_view.c_addRow(row)
                self.flag_dataAddComplet = True
            else:
                Notice().exec("错误", F"数据检索失败\n{resp['msg']}")

    def solt_confirm(self) -> None:
        if self.rowIndex != -1:
            content = getConfigContent(self.userId, self.configFileName)["data"]
            path = File.path(SysPath.TEMP, "tmpcc.json")
            File.write(path, content)
            self.sig_tempConfCreated.emit(path, self.table_view.item(self.rowIndex, 0).text())
            self.accept()
        else:
            Notice().exec("提示", "未选中任何配置")

    # 信号响应
    # ///////////////////////////////////////////////////////////////
    def solt_get_doc(self) -> None:
        if self.flag_dataAddComplet:
            nrowindex = self.table_view.selectedIndexes()
            if nrowindex:
                row = nrowindex[0].row()
                if row != self.rowIndex:
                    self.rowIndex = row
                    self.configId = self.table_view.item(row, 4).text()
                    info = getConfigInfo(self.configId)["data"]
                    self.userId = info["userId"]
                    self.configFileName = info["fileName"]
                    docfname = info["docFileName"]
                    if docfname is None or docfname == "":
                        doc = "*该配置无说明文档*"
                    else:
                        doc = getConfigDoc(docfname)["data"]
                    if doc == "":
                        self.tedit_doc.setText("*该配置无说明文档*")
                    else:
                        self.tedit_doc.setText(doc)
            else:
                self.rowIndex = -1
