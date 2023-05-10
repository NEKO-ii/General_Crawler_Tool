# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_page.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QLayout, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from core.sys.themes import Themes
from core.sys.globalv import Globalv, GlvKey
from ui.widgets import PushButton


class Ui_StartPageBtn(object):

    def __init__(self, StartPageBtn: QWidget) -> None:
        self._themes: Themes = Globalv.get(GlvKey.THEMES)
        self._color_green_1 = self._themes.color["green"]
        self._color_green_2 = self._themes.color["green_2"]
        self.setupUi(StartPageBtn)
        self.setup()

    def setup(self) -> None:
        # 添加按钮
        # ///////////////////////////////////////////////////////////////
        self.btn_config = PushButton(text="编辑配置文件", minimumSize=[250, 60], radius=8, fontSize=11)
        self.btn_container_1.addWidget(self.btn_config)
        self.btn_help = PushButton(text="查看帮助文档", minimumSize=[250, 60], radius=8, fontSize=11)
        self.btn_container_2.addWidget(self.btn_help)
        self.btn_run = PushButton(text="执行自动运行", minimumSize=[250, 60], radius=8, fontSize=11, type="success")
        self.btn_container_3.addWidget(self.btn_run)

    def setupUi(self, StartPageBtn):
        if not StartPageBtn.objectName():
            StartPageBtn.setObjectName(u"StartPageBtn")
        StartPageBtn.resize(657, 434)
        self.verticalLayout = QVBoxLayout(StartPageBtn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_top = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_top)

        self.line_top = QFrame(StartPageBtn)
        self.line_top.setObjectName(u"line_top")
        self.line_top.setStyleSheet("background-color: #3c4454")
        self.line_top.setFrameShape(QFrame.HLine)
        self.line_top.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_top)

        self.label_welcome = QLabel(StartPageBtn)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";")
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_welcome)

        self.line_bottom = QFrame(StartPageBtn)
        self.line_bottom.setObjectName(u"line_bottom")
        self.line_bottom.setStyleSheet("background-color: #3c4454")
        self.line_bottom.setFrameShape(QFrame.HLine)
        self.line_bottom.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_bottom)

        self.container = QHBoxLayout()
        self.container.setObjectName(u"container")
        self.container.setContentsMargins(0, 20, 0, 0)

        self.horizontalSpacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container.addItem(self.horizontalSpacer_left)

        self.col1 = QVBoxLayout()
        self.col1.setObjectName(u"col1")
        self.col1.setSizeConstraint(QLayout.SetMinimumSize)
        self.col1.setContentsMargins(20, 0, 20, 0)
        self.btn_container_1 = QVBoxLayout()
        self.btn_container_1.setObjectName(u"btn_container_1")

        self.col1.addLayout(self.btn_container_1)

        self.tip_1 = QLabel(StartPageBtn)
        self.tip_1.setObjectName(u"tip_1")
        self.tip_1.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.tip_1.setMinimumSize(QSize(260, 60))
        self.tip_1.setTextFormat(Qt.AutoText)
        self.tip_1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.tip_1.setWordWrap(True)
        self.tip_1.setMargin(0)

        self.col1.addWidget(self.tip_1)

        self.container.addLayout(self.col1)

        self.col2 = QVBoxLayout()
        self.col2.setObjectName(u"col2")
        self.col2.setSizeConstraint(QLayout.SetMinimumSize)
        self.col2.setContentsMargins(20, 0, 20, 0)
        self.btn_container_2 = QVBoxLayout()
        self.btn_container_2.setObjectName(u"btn_container_2")

        self.col2.addLayout(self.btn_container_2)

        self.tip_2 = QLabel(StartPageBtn)
        self.tip_2.setObjectName(u"tip_2")
        self.tip_2.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.tip_2.setMinimumSize(QSize(260, 60))
        self.tip_2.setTextFormat(Qt.AutoText)
        self.tip_2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.tip_2.setWordWrap(True)
        self.tip_2.setMargin(0)

        self.col2.addWidget(self.tip_2)

        self.container.addLayout(self.col2)

        self.col3 = QVBoxLayout()
        self.col3.setObjectName(u"col3")
        self.col3.setSizeConstraint(QLayout.SetMinimumSize)
        self.col3.setContentsMargins(20, 0, 20, 0)
        self.btn_container_3 = QVBoxLayout()
        self.btn_container_3.setObjectName(u"btn_container_3")

        self.col3.addLayout(self.btn_container_3)

        self.tip_3 = QLabel(StartPageBtn)
        self.tip_3.setObjectName(u"tip_3")
        self.tip_3.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.tip_3.setMinimumSize(QSize(260, 60))
        self.tip_3.setTextFormat(Qt.AutoText)
        self.tip_3.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.tip_3.setWordWrap(True)
        self.tip_3.setMargin(0)

        self.col3.addWidget(self.tip_3)

        self.container.addLayout(self.col3)

        self.horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container.addItem(self.horizontalSpacer_right)

        self.verticalLayout.addLayout(self.container)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_bottom)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(StartPageBtn)

    # setupUi

    def retranslateUi(self):
        self.label_welcome.setText(QCoreApplication.translate("StartPageBtn", u"\u6b22\u8fce\u4f7f\u7528\u901a\u7528\u81ea\u52a8\u5316\u722c\u866b\u7a0b\u5e8f", None))
        self.tip_1.setText(
            QCoreApplication.translate(
                "StartPageBtn", u"\u81ea\u52a8\u5316\u8fd0\u884c\u9700\u8981\u4f9d\u8d56\u914d\u7f6e\u6587\u4ef6\n"
                "\u82e5\u5df2\u62e5\u6709\u914d\u7f6e\u6587\u4ef6\u53ef\u76f4\u63a5\u8fd0\u884c\n"
                "\u82e5\u672a\u62e5\u6709\u5219\u9700\u8981\u65b0\u5efa\u6216\u5bfc\u5165", None))
        self.tip_2.setText(QCoreApplication.translate("StartPageBtn", u"\u5e2e\u52a9\u6587\u6863\u8be6\u7ec6\u8bf4\u660e\u4e86\u914d\u7f6e\u6587\u4ef6\n"
                                                      "\u7684\u5404\u9879\u5c5e\u6027,\u67e5\u9605\u4ee5\u4e86\u89e3\u7ec6\u8282", None))
        self.tip_3.setText(
            QCoreApplication.translate(
                "StartPageBtn", u"\u81ea\u52a8\u5316\u8fd0\u884c\u9700\u8981\u62e5\u6709\u914d\u7f6e\u6587\u4ef6\n"
                "\u5e76\u4fdd\u8bc1\u914d\u7f6e\u6587\u4ef6\u7684\u6b63\u786e\u6027,\u5426\u5219\n"
                "\u65e0\u6cd5\u5f97\u5230\u6b63\u786e\u7684\u6570\u636e", None))

    # retranslateUi
