# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CloudReadPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (Qt, QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout, QWidget, QLabel, QFormLayout)
from ui.widgets import PushButton, ComboBox, TextEdit, LineEdit


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

        self.btn_reject = PushButton(CloudReadPage, type="error")
        self.hly_top.addWidget(self.btn_reject)

        self.btn_check = PushButton(CloudReadPage, type="primary")
        self.hly_top.addWidget(self.btn_check)

        self.btn_save = PushButton(CloudReadPage, type="success")
        self.hly_top.addWidget(self.btn_save)

        self.btn_edit = PushButton(CloudReadPage, type="primary")
        self.hly_top.addWidget(self.btn_edit)

        self.verticalLayout_3.addLayout(self.hly_top)

        self.view = QStackedWidget(CloudReadPage)
        self.view_doc = QWidget()
        self.horizontalLayout = QHBoxLayout(self.view_doc)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tedit_doc = TextEdit(self.view_doc)
        self.tedit_doc.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.tedit_doc.setPlaceholderText("此处填写共享配置的说明文档")
        sp = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sp.setHorizontalStretch(1)
        self.tedit_doc.setSizePolicy(sp)

        self.horizontalLayout.addWidget(self.tedit_doc)

        self.vly = QVBoxLayout()
        self.fly_comment = QFormLayout()
        self.fly_comment.setHorizontalSpacing(5)
        self.fly_comment.setVerticalSpacing(10)

        self.lb_configId = QLabel(self.view_doc)
        self.fly_comment.setWidget(0, QFormLayout.LabelRole, self.lb_configId)

        self.ledit_configId = LineEdit(self.view_doc)
        self.ledit_configId.setReadOnly(True)
        self.ledit_configId.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.fly_comment.setWidget(0, QFormLayout.FieldRole, self.ledit_configId)

        self.lb_configName = QLabel(self.view_doc)
        self.fly_comment.setWidget(1, QFormLayout.LabelRole, self.lb_configName)

        self.ledit_configName = LineEdit(self.view_doc)
        self.ledit_configName.setPlaceholderText("请输入配置名称")
        self.fly_comment.setWidget(1, QFormLayout.FieldRole, self.ledit_configName)

        self.lb_fileName = QLabel(self.view_doc)
        self.fly_comment.setWidget(2, QFormLayout.LabelRole, self.lb_fileName)

        self.ledit_fileName = LineEdit(self.view_doc)
        self.ledit_fileName.setPlaceholderText("请输入文件名称")
        self.fly_comment.setWidget(2, QFormLayout.FieldRole, self.ledit_fileName)

        self.lb_comment = QLabel(self.view_doc)
        self.fly_comment.setWidget(3, QFormLayout.LabelRole, self.lb_comment)

        self.ledit_comment = LineEdit(self.view_doc)
        self.ledit_comment.setPlaceholderText("请输入配置注释")
        self.fly_comment.setWidget(3, QFormLayout.FieldRole, self.ledit_comment)

        self.lb_host = QLabel(self.view_doc)
        self.fly_comment.setWidget(4, QFormLayout.LabelRole, self.lb_host)

        self.ledit_host = LineEdit(self.view_doc)
        self.ledit_host.setPlaceholderText("请输入搜索根域名")
        self.fly_comment.setWidget(4, QFormLayout.FieldRole, self.ledit_host)

        self.lb_uploadTime = QLabel(self.view_doc)
        self.fly_comment.setWidget(5, QFormLayout.LabelRole, self.lb_uploadTime)

        self.ledit_uploadTime = LineEdit(self.view_doc)
        self.ledit_uploadTime.setReadOnly(True)
        self.ledit_uploadTime.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.fly_comment.setWidget(5, QFormLayout.FieldRole, self.ledit_uploadTime)

        self.lb_updateTime = QLabel(self.view_doc)
        self.fly_comment.setWidget(6, QFormLayout.LabelRole, self.lb_updateTime)

        self.ledit_updateTime = LineEdit(self.view_doc)
        self.ledit_updateTime.setReadOnly(True)
        self.ledit_updateTime.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.fly_comment.setWidget(6, QFormLayout.FieldRole, self.ledit_updateTime)

        self.lb_state = QLabel(self.view_doc)
        self.fly_comment.setWidget(7, QFormLayout.LabelRole, self.lb_state)

        self.hly_2 = QHBoxLayout()
        self.hly_2.setSpacing(5)
        self.ledit_state = LineEdit(self.view_doc)
        self.ledit_state.setReadOnly(True)
        self.ledit_state.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.hly_2.addWidget(self.ledit_state)
        self.btn_stateChange = PushButton(self.view_doc)
        self.hly_2.addWidget(self.btn_stateChange)

        self.fly_comment.setLayout(7, QFormLayout.FieldRole, self.hly_2)

        self.vly.addLayout(self.fly_comment)

        self.hly_3 = QHBoxLayout()
        self.hs_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_3.addItem(self.hs_2)

        self.lb_check = QLabel(self.view_doc)

        self.hly_3.addWidget(self.lb_check)

        self.vly.addLayout(self.hly_3)

        self.vs_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vly.addItem(self.vs_1)

        self.horizontalLayout.addLayout(self.vly)

        self.view.addWidget(self.view_doc)

        self.view_json = QWidget()
        self.verticalLayout_2 = QVBoxLayout(self.view_json)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tedit_json = TextEdit(self.view_json)
        self.tedit_json.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.tedit_json.setPlaceholderText("此处编写配置文件")
        self.verticalLayout_2.addWidget(self.tedit_json)

        self.view.addWidget(self.view_json)

        self.verticalLayout_3.addWidget(self.view)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(CloudReadPage)

    # setupUi

    def retranslateUi(self):
        self.btn_back.setText(QCoreApplication.translate("CloudReadPage", u"\u8fd4\u56de", None))
        self.combo_selectView.setItemText(0, QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u8bf4\u660e", None))
        self.combo_selectView.setItemText(1, QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u5185\u5bb9", None))

        self.btn_reject.setText(QCoreApplication.translate("CloudReadPage", u"\u53d6\u6d88", None))
        self.btn_check.setText(QCoreApplication.translate("CloudReadPage", u"\u68c0\u67e5", None))
        self.btn_save.setText(QCoreApplication.translate("CloudReadPage", u"\u4fdd\u5b58", None))
        self.btn_edit.setText(QCoreApplication.translate("CloudReadPage", u"\u7f16\u8f91", None))
        self.lb_configName.setText(QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u540d\u79f0:", None))
        self.lb_fileName.setText(QCoreApplication.translate("CloudReadPage", u"\u6587\u4ef6\u540d\u79f0:", None))
        self.lb_comment.setText(QCoreApplication.translate("CloudReadPage", u"\u6ce8\u3000\u3000\u91ca:", None))
        self.lb_host.setText(QCoreApplication.translate("CloudReadPage", u"\u57df\u3000\u3000\u540d:", None))
        self.lb_uploadTime.setText(QCoreApplication.translate("CloudReadPage", u"\u4e0a\u4f20\u65f6\u95f4:", None))
        self.lb_updateTime.setText(QCoreApplication.translate("CloudReadPage", u"\u66f4\u65b0\u65f6\u95f4:", None))
        self.lb_configId.setText(QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u7f16\u53f7:", None))
        self.lb_state.setText(QCoreApplication.translate("CloudReadPage", u"\u72b6\u3000\u3000\u6001:", None))
        self.btn_stateChange.setText(QCoreApplication.translate("CloudReadPage", u"\u5171\u4eab\u6b64\u914d\u7f6e", None))
        self.lb_check.setText(QCoreApplication.translate("CloudReadPage", u"\u672a\u68c0\u67e5", None))

    # retranslateUi
