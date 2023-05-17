# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AccountPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)


class Ui_AccountPage(object):

    def setupUi(self, AccountPage):
        if not AccountPage.objectName():
            AccountPage.setObjectName(u"AccountPage")
        AccountPage.resize(1012, 516)
        self.verticalLayout = QVBoxLayout(AccountPage)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hly_top = QHBoxLayout()
        self.hly_top.setObjectName(u"hly_top")
        self.hly_top.setContentsMargins(10, -1, -1, -1)
        self.lb_pageTitle = QLabel(AccountPage)
        self.lb_pageTitle.setObjectName(u"lb_pageTitle")
        font = QFont()
        font.setPointSize(15)
        self.lb_pageTitle.setFont(font)

        self.hly_top.addWidget(self.lb_pageTitle)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_top.addItem(self.hs_1)

        self.btn_login = QPushButton(AccountPage)
        self.btn_login.setObjectName(u"btn_login")

        self.hly_top.addWidget(self.btn_login)

        self.verticalLayout.addLayout(self.hly_top)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, -1, -1)
        self.lb_image = QLabel(AccountPage)
        self.lb_image.setObjectName(u"lb_image")
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

        self.horizontalLayout.addWidget(self.lb_image)

        self.vly_usrMsgView = QVBoxLayout()
        self.vly_usrMsgView.setSpacing(5)
        self.vly_usrMsgView.setObjectName(u"vly_usrMsgView")
        self.vly_usrMsgView.setContentsMargins(10, 20, 10, 20)
        self.lb_username = QLabel(AccountPage)
        self.lb_username.setObjectName(u"lb_username")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_username.sizePolicy().hasHeightForWidth())
        self.lb_username.setSizePolicy(sizePolicy1)
        self.lb_username.setMinimumSize(QSize(200, 0))
        self.lb_username.setMaximumSize(QSize(16777215, 16777215))

        self.vly_usrMsgView.addWidget(self.lb_username)

        self.lb_email = QLabel(AccountPage)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(0, 0))
        self.lb_email.setMaximumSize(QSize(16777215, 16777215))

        self.vly_usrMsgView.addWidget(self.lb_email)

        self.lb_uid = QLabel(AccountPage)
        self.lb_uid.setObjectName(u"lb_uid")
        self.lb_uid.setMinimumSize(QSize(0, 0))
        self.lb_uid.setMaximumSize(QSize(16777215, 16777215))

        self.vly_usrMsgView.addWidget(self.lb_uid)

        self.horizontalLayout.addLayout(self.vly_usrMsgView)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vs_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.vs_1)

        self.retranslateUi(AccountPage)

        QMetaObject.connectSlotsByName(AccountPage)

    # setupUi

    def retranslateUi(self, AccountPage):
        AccountPage.setWindowTitle(QCoreApplication.translate("AccountPage", u"Form", None))
        self.lb_pageTitle.setText(QCoreApplication.translate("AccountPage", u"\u8d26\u6237", None))
        self.btn_login.setText(QCoreApplication.translate("AccountPage", u"\u767b\u9646", None))
        self.lb_image.setText(QCoreApplication.translate("AccountPage", u"image", None))
        self.lb_username.setText(QCoreApplication.translate("AccountPage", u"--", None))
        self.lb_email.setText(QCoreApplication.translate("AccountPage", u"--", None))
        self.lb_uid.setText(QCoreApplication.translate("AccountPage", u"--", None))

    # retranslateUi
