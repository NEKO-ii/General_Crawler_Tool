# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AccountPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import PushButton


class Ui_AccountPage(object):
    def __init__(self, AccountPage) -> None:
        self.setupUi(AccountPage)

    def setupUi(self, AccountPage):
        if not AccountPage.objectName():
            AccountPage.setObjectName(u"AccountPage")
        self.verticalLayout = QVBoxLayout(AccountPage)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hly_top = QHBoxLayout()
        self.hly_top.setContentsMargins(10, -1, -1, -1)
        self.lb_pageTitle = QLabel(AccountPage)
        font = QFont()
        font.setPointSize(15)
        self.lb_pageTitle.setFont(font)
        self.hly_top.addWidget(self.lb_pageTitle)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_top.addItem(self.hs_1)

        self.btn_login = PushButton(AccountPage, type="primary")
        self.hly_top.addWidget(self.btn_login)

        self.verticalLayout.addLayout(self.hly_top)

        self.hly_accmsg = QHBoxLayout()
        self.hly_accmsg.setSpacing(5)
        self.hly_accmsg.setContentsMargins(10, 0, -1, -1)
        self.lb_image = QLabel(AccountPage)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_image.sizePolicy().hasHeightForWidth())
        self.lb_image.setSizePolicy(sizePolicy)
        self.lb_image.setMinimumSize(QSize(100, 100))
        self.lb_image.setStyleSheet(u"QLabel{\n"
                                    "border: 2px solid #FFFFFF;\n"
                                    "border-radius: 50px;\n"
                                    "}")

        self.hly_accmsg.addWidget(self.lb_image)

        self.vly_usrMsgView = QVBoxLayout()
        self.vly_usrMsgView.setSpacing(5)
        self.vly_usrMsgView.setContentsMargins(10, 20, 10, 20)

        self.lb_username = QLabel(AccountPage)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_username.sizePolicy().hasHeightForWidth())
        self.lb_username.setSizePolicy(sizePolicy1)
        self.vly_usrMsgView.addWidget(self.lb_username)

        self.lb_email = QLabel(AccountPage)
        self.vly_usrMsgView.addWidget(self.lb_email)

        self.lb_uid = QLabel(AccountPage)
        self.vly_usrMsgView.addWidget(self.lb_uid)

        self.hly_accmsg.addLayout(self.vly_usrMsgView)
        self.verticalLayout.addLayout(self.hly_accmsg)

        self.vs_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.vs_1)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(AccountPage)

    # setupUi

    def retranslateUi(self):
        self.lb_pageTitle.setText(QCoreApplication.translate("AccountPage", u"\u8d26\u6237", None))
        self.btn_login.setText(QCoreApplication.translate("AccountPage", u"\u767b\u9646", None))
        self.lb_image.setText(QCoreApplication.translate("AccountPage", u"image", None))
        self.lb_username.setText(QCoreApplication.translate("AccountPage", u"--", None))
        self.lb_email.setText(QCoreApplication.translate("AccountPage", u"--", None))
        self.lb_uid.setText(QCoreApplication.translate("AccountPage", u"--", None))

    # retranslateUi
