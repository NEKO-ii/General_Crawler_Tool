# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CloudReadPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from ui.widgets import PushButton, ComboBox, TextEdit


class Ui_CloudRead(object):

    def setupUi(self, CloudReadPage):
        if not CloudReadPage.objectName():
            CloudReadPage.setObjectName(u"CloudReadPage")
        self.verticalLayout_3 = QVBoxLayout(CloudReadPage)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hly_top = QHBoxLayout()
        self.btn_back = PushButton(CloudReadPage)
        self.hly_top.addWidget(self.btn_back)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_top.addItem(self.hs_1)

        self.combo_selectView = ComboBox(CloudReadPage)
        self.combo_selectView.addItem("")
        self.combo_selectView.addItem("")
        self.hly_top.addWidget(self.combo_selectView)

        self.btn_save = PushButton(CloudReadPage, type="success")
        self.hly_top.addWidget(self.btn_save)

        self.btn_edit = PushButton(CloudReadPage, type="primary")
        self.hly_top.addWidget(self.btn_edit)

        self.verticalLayout_3.addLayout(self.hly_top)

        self.view = QStackedWidget(CloudReadPage)
        self.view_json = QWidget()
        self.verticalLayout_2 = QVBoxLayout(self.view_json)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tedit_json = TextEdit(self.view_json)
        self.verticalLayout_2.addWidget(self.tedit_json)

        self.view.addWidget(self.view_json)
        self.view_comment = QWidget()
        self.verticalLayout = QVBoxLayout(self.view_comment)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tedit_comment = TextEdit(self.view_comment)

        self.verticalLayout.addWidget(self.tedit_comment)

        self.view.addWidget(self.view_comment)

        self.verticalLayout_3.addWidget(self.view)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(CloudReadPage)

    # setupUi

    def retranslateUi(self):
        self.btn_back.setText(QCoreApplication.translate("CloudReadPage", u"\u8fd4\u56de", None))
        self.combo_selectView.setItemText(0, QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u5185\u5bb9", None))
        self.combo_selectView.setItemText(1, QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u8bf4\u660e", None))

        self.btn_save.setText(QCoreApplication.translate("CloudReadPage", u"\u4fdd\u5b58", None))
        self.btn_edit.setText(QCoreApplication.translate("CloudReadPage", u"\u7f16\u8f91", None))

    # retranslateUi
