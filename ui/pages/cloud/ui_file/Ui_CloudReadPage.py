# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CloudReadPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_CloudReadPage(object):
    def setupUi(self, CloudReadPage):
        if not CloudReadPage.objectName():
            CloudReadPage.setObjectName(u"CloudReadPage")
        CloudReadPage.resize(1031, 548)
        self.verticalLayout_3 = QVBoxLayout(CloudReadPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hly_top = QHBoxLayout()
        self.hly_top.setObjectName(u"hly_top")
        self.btn_back = QPushButton(CloudReadPage)
        self.btn_back.setObjectName(u"btn_back")

        self.hly_top.addWidget(self.btn_back)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_top.addItem(self.hs_1)

        self.combo_selectView = QComboBox(CloudReadPage)
        self.combo_selectView.addItem("")
        self.combo_selectView.addItem("")
        self.combo_selectView.setObjectName(u"combo_selectView")

        self.hly_top.addWidget(self.combo_selectView)

        self.btn_save = QPushButton(CloudReadPage)
        self.btn_save.setObjectName(u"btn_save")

        self.hly_top.addWidget(self.btn_save)

        self.btn_edit = QPushButton(CloudReadPage)
        self.btn_edit.setObjectName(u"btn_edit")

        self.hly_top.addWidget(self.btn_edit)


        self.verticalLayout_3.addLayout(self.hly_top)

        self.view = QStackedWidget(CloudReadPage)
        self.view.setObjectName(u"view")
        self.view_json = QWidget()
        self.view_json.setObjectName(u"view_json")
        self.verticalLayout_2 = QVBoxLayout(self.view_json)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tedit_json = QTextEdit(self.view_json)
        self.tedit_json.setObjectName(u"tedit_json")

        self.verticalLayout_2.addWidget(self.tedit_json)

        self.view.addWidget(self.view_json)
        self.view_comment = QWidget()
        self.view_comment.setObjectName(u"view_comment")
        self.horizontalLayout = QHBoxLayout(self.view_comment)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tedit_comment = QTextEdit(self.view_comment)
        self.tedit_comment.setObjectName(u"tedit_comment")

        self.horizontalLayout.addWidget(self.tedit_comment)

        self.vly = QVBoxLayout()
        self.vly.setObjectName(u"vly")
        self.fly_comment = QFormLayout()
        self.fly_comment.setObjectName(u"fly_comment")
        self.fly_comment.setHorizontalSpacing(5)
        self.fly_comment.setVerticalSpacing(10)
        self.lb_configName = QLabel(self.view_comment)
        self.lb_configName.setObjectName(u"lb_configName")

        self.fly_comment.setWidget(1, QFormLayout.LabelRole, self.lb_configName)

        self.ledit_configName = QLineEdit(self.view_comment)
        self.ledit_configName.setObjectName(u"ledit_configName")

        self.fly_comment.setWidget(1, QFormLayout.FieldRole, self.ledit_configName)

        self.lb_fileName = QLabel(self.view_comment)
        self.lb_fileName.setObjectName(u"lb_fileName")

        self.fly_comment.setWidget(2, QFormLayout.LabelRole, self.lb_fileName)

        self.ledit_fileName = QLineEdit(self.view_comment)
        self.ledit_fileName.setObjectName(u"ledit_fileName")

        self.fly_comment.setWidget(2, QFormLayout.FieldRole, self.ledit_fileName)

        self.lb_comment = QLabel(self.view_comment)
        self.lb_comment.setObjectName(u"lb_comment")

        self.fly_comment.setWidget(3, QFormLayout.LabelRole, self.lb_comment)

        self.ledit_comment = QLineEdit(self.view_comment)
        self.ledit_comment.setObjectName(u"ledit_comment")

        self.fly_comment.setWidget(3, QFormLayout.FieldRole, self.ledit_comment)

        self.lb_host = QLabel(self.view_comment)
        self.lb_host.setObjectName(u"lb_host")

        self.fly_comment.setWidget(4, QFormLayout.LabelRole, self.lb_host)

        self.ledit_host = QLineEdit(self.view_comment)
        self.ledit_host.setObjectName(u"ledit_host")

        self.fly_comment.setWidget(4, QFormLayout.FieldRole, self.ledit_host)

        self.lb_uploadTime = QLabel(self.view_comment)
        self.lb_uploadTime.setObjectName(u"lb_uploadTime")

        self.fly_comment.setWidget(5, QFormLayout.LabelRole, self.lb_uploadTime)

        self.ledit_uploadTime = QLineEdit(self.view_comment)
        self.ledit_uploadTime.setObjectName(u"ledit_uploadTime")

        self.fly_comment.setWidget(5, QFormLayout.FieldRole, self.ledit_uploadTime)

        self.lb_updateTime = QLabel(self.view_comment)
        self.lb_updateTime.setObjectName(u"lb_updateTime")

        self.fly_comment.setWidget(6, QFormLayout.LabelRole, self.lb_updateTime)

        self.ledit_updateTime = QLineEdit(self.view_comment)
        self.ledit_updateTime.setObjectName(u"ledit_updateTime")

        self.fly_comment.setWidget(6, QFormLayout.FieldRole, self.ledit_updateTime)

        self.lb_configId = QLabel(self.view_comment)
        self.lb_configId.setObjectName(u"lb_configId")

        self.fly_comment.setWidget(0, QFormLayout.LabelRole, self.lb_configId)

        self.ledit_configId = QLineEdit(self.view_comment)
        self.ledit_configId.setObjectName(u"ledit_configId")

        self.fly_comment.setWidget(0, QFormLayout.FieldRole, self.ledit_configId)

        self.lb_state = QLabel(self.view_comment)
        self.lb_state.setObjectName(u"lb_state")

        self.fly_comment.setWidget(7, QFormLayout.LabelRole, self.lb_state)

        self.hly_2 = QHBoxLayout()
        self.hly_2.setSpacing(5)
        self.hly_2.setObjectName(u"hly_2")
        self.ledit_state = QLineEdit(self.view_comment)
        self.ledit_state.setObjectName(u"ledit_state")

        self.hly_2.addWidget(self.ledit_state)

        self.btn_stateChange = QPushButton(self.view_comment)
        self.btn_stateChange.setObjectName(u"btn_stateChange")

        self.hly_2.addWidget(self.btn_stateChange)


        self.fly_comment.setLayout(7, QFormLayout.FieldRole, self.hly_2)


        self.vly.addLayout(self.fly_comment)

        self.hly_3 = QHBoxLayout()
        self.hly_3.setObjectName(u"hly_3")
        self.hs_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_3.addItem(self.hs_2)

        self.lb_check = QLabel(self.view_comment)
        self.lb_check.setObjectName(u"lb_check")

        self.hly_3.addWidget(self.lb_check)


        self.vly.addLayout(self.hly_3)

        self.vs_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vly.addItem(self.vs_1)


        self.horizontalLayout.addLayout(self.vly)

        self.view.addWidget(self.view_comment)

        self.verticalLayout_3.addWidget(self.view)


        self.retranslateUi(CloudReadPage)

        self.view.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(CloudReadPage)
    # setupUi

    def retranslateUi(self, CloudReadPage):
        CloudReadPage.setWindowTitle(QCoreApplication.translate("CloudReadPage", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("CloudReadPage", u"\u8fd4\u56de", None))
        self.combo_selectView.setItemText(0, QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u8bf4\u660e", None))
        self.combo_selectView.setItemText(1, QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u5185\u5bb9", None))

        self.btn_save.setText(QCoreApplication.translate("CloudReadPage", u"\u4fdd\u5b58", None))
        self.btn_edit.setText(QCoreApplication.translate("CloudReadPage", u"\u7f16\u8f91", None))
        self.lb_configName.setText(QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u540d\u79f0:", None))
        self.lb_fileName.setText(QCoreApplication.translate("CloudReadPage", u"\u6587\u4ef6\u540d\u79f0:", None))
        self.lb_comment.setText(QCoreApplication.translate("CloudReadPage", u"\u6ce8\u91ca:", None))
        self.lb_host.setText(QCoreApplication.translate("CloudReadPage", u"\u57df\u540d:", None))
        self.lb_uploadTime.setText(QCoreApplication.translate("CloudReadPage", u"\u4e0a\u4f20\u65f6\u95f4:", None))
        self.lb_updateTime.setText(QCoreApplication.translate("CloudReadPage", u"\u66f4\u65b0\u65f6\u95f4:", None))
        self.lb_configId.setText(QCoreApplication.translate("CloudReadPage", u"\u914d\u7f6e\u7f16\u53f7:", None))
        self.lb_state.setText(QCoreApplication.translate("CloudReadPage", u"\u72b6\u6001:", None))
        self.btn_stateChange.setText(QCoreApplication.translate("CloudReadPage", u"\u5171\u4eab\u6b64\u914d\u7f6e", None))
        self.lb_check.setText(QCoreApplication.translate("CloudReadPage", u"\u672a\u68c0\u67e5", None))
    # retranslateUi

