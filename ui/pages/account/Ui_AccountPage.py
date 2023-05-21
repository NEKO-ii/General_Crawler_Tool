# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AccountPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (Qt, QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QGridLayout)
from ui.widgets import PushButton, LineEdit
from ui.func.iconsetter import IconSetter


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
        self.lb_pageTitle.setStyleSheet("font: 15pt")
        self.hly_top.addWidget(self.lb_pageTitle)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_top.addItem(self.hs_1)

        self.btn_delAccount = PushButton(AccountPage, type="error")
        self.hly_top.addWidget(self.btn_delAccount)
        self.btn_delAccount.hide()

        self.btn_updateAccount = PushButton(AccountPage, type="primary")
        self.hly_top.addWidget(self.btn_updateAccount)
        self.btn_updateAccount.hide()

        self.btn_logout = PushButton(AccountPage, type="warning")
        self.hly_top.addWidget(self.btn_logout)
        self.btn_logout.hide()

        self.btn_login = PushButton(AccountPage, type="primary")
        self.hly_top.addWidget(self.btn_login)

        self.verticalLayout.addLayout(self.hly_top)

        self.hly_accmsg = QHBoxLayout()
        self.hly_accmsg.setSpacing(5)
        self.hly_accmsg.setContentsMargins(10, 0, -1, -1)
        self.lb_image = QLabel(AccountPage)
        self.lb_image.setFixedSize(100, 100)
        self.lb_image.setStyleSheet(u"QLabel{\n"
                                    "border: 2px solid #FFFFFF;\n"
                                    "border-radius: 50px;\n"
                                    "}")
        pix = QPixmap(IconSetter.setSvgIcon("icon_account.svg"))
        pix.scaled(self.lb_image.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.lb_image.setScaledContents(True)
        self.lb_image.setPixmap(pix)

        self.hly_accmsg.addWidget(self.lb_image)

        self.vly_usrMsgView = QVBoxLayout()
        self.vly_usrMsgView.setSpacing(5)
        self.vly_usrMsgView.setContentsMargins(10, 20, 10, 20)

        self.lb_username = QLabel(AccountPage)
        self.lb_username.setStyleSheet("font: 13pt; color: orange;")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_username.sizePolicy().hasHeightForWidth())
        self.lb_username.setSizePolicy(sizePolicy1)
        self.vly_usrMsgView.addWidget(self.lb_username)

        self.lb_email = QLabel(AccountPage)
        self.lb_email.setStyleSheet("font: 12pt; color: lightblue;")
        self.vly_usrMsgView.addWidget(self.lb_email)

        self.lb_uid = QLabel(AccountPage)
        self.lb_uid.setStyleSheet("font: 10pt; color: lightblue;")
        self.vly_usrMsgView.addWidget(self.lb_uid)

        self.hly_accmsg.addLayout(self.vly_usrMsgView)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_accmsg.addItem(self.horizontalSpacer)

        self.gly_editplace = QGridLayout()
        self.lb_utime = QLabel(AccountPage)
        self.gly_editplace.addWidget(self.lb_utime, 1, 2, 1, 1)

        self.lb_configCount = QLabel(AccountPage)
        self.gly_editplace.addWidget(self.lb_configCount, 0, 2, 1, 1)

        self.ledit_ctime = LineEdit(AccountPage)
        self.ledit_ctime.setReadOnly(True)
        self.ledit_ctime.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gly_editplace.addWidget(self.ledit_ctime, 1, 1, 1, 1)

        self.ledit_configCount = LineEdit(AccountPage, color_enabled="#568af2")
        self.ledit_configCount.setReadOnly(True)
        self.ledit_configCount.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gly_editplace.addWidget(self.ledit_configCount, 0, 3, 1, 1)

        self.ledit_utime = LineEdit(AccountPage)
        self.ledit_utime.setReadOnly(True)
        self.ledit_utime.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gly_editplace.addWidget(self.ledit_utime, 1, 3, 1, 1)

        self.lb_ctime = QLabel(AccountPage)
        self.gly_editplace.addWidget(self.lb_ctime, 1, 0, 1, 1)

        self.lb_requestCount = QLabel(AccountPage)
        self.gly_editplace.addWidget(self.lb_requestCount, 0, 0, 1, 1)

        self.ledit_requestCount = LineEdit(AccountPage, color_enabled="#568af2")
        self.ledit_requestCount.setReadOnly(True)
        self.ledit_requestCount.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gly_editplace.addWidget(self.ledit_requestCount, 0, 1, 1, 1)

        self.lb_email_edit = QLabel(AccountPage)
        self.gly_editplace.addWidget(self.lb_email_edit, 2, 0, 1, 1)

        self.ledit_email = LineEdit(AccountPage)
        self.ledit_email.setReadOnly(True)
        self.ledit_email.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gly_editplace.addWidget(self.ledit_email, 2, 1, 1, 1)

        self.lb_password = QLabel(AccountPage)
        self.gly_editplace.addWidget(self.lb_password, 2, 2, 1, 1)

        self.ledit_password = LineEdit(AccountPage)
        self.ledit_password.setReadOnly(True)
        self.ledit_password.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ledit_password.setEchoMode(LineEdit.EchoMode.Password)
        font = QFont(["JetBrains Mono", "微软雅黑"], 10)
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 3.0)
        self.ledit_password.setFont(font)
        self.gly_editplace.addWidget(self.ledit_password, 2, 3, 1, 1)

        self.hly_accmsg.addLayout(self.gly_editplace)

        self.verticalLayout.addLayout(self.hly_accmsg)

        self.vs_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.vs_1)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(AccountPage)

    # setupUi

    def retranslateUi(self):
        self.lb_pageTitle.setText(QCoreApplication.translate("AccountPage", u"\u8d26\u6237", None))
        self.btn_delAccount.setText(QCoreApplication.translate("AccountPage", u"\u5220\u9664\u8d26\u6237", None))
        self.btn_updateAccount.setText(QCoreApplication.translate("AccountPage", u"\u4fee\u6539\u5bc6\u7801", None))
        self.btn_logout.setText(QCoreApplication.translate("AccountPage", u"\u9000\u51fa\u767b\u5f55", None))
        self.btn_login.setText(QCoreApplication.translate("AccountPage", u"\u767b\u9646", None))
        self.lb_username.setText(QCoreApplication.translate("AccountPage", u"\u672a\u767b\u5f55", None))
        self.lb_email.setText(QCoreApplication.translate("AccountPage", u"--", None))
        self.lb_uid.setText(QCoreApplication.translate("AccountPage", u"--", None))
        self.lb_utime.setText(QCoreApplication.translate("AccountPage", u"\u66f4\u65b0\u65f6\u95f4:", None))
        self.lb_configCount.setText(QCoreApplication.translate("AccountPage", u"\u914d\u7f6e\u6570\u91cf:", None))
        self.lb_ctime.setText(QCoreApplication.translate("AccountPage", u"\u521b\u5efa\u65f6\u95f4:", None))
        self.lb_requestCount.setText(QCoreApplication.translate("AccountPage", u"\u8bf7\u6c42\u6b21\u6570:", None))
        self.lb_email_edit.setText(QCoreApplication.translate("AccountPage", u"\u7ed1\u5b9a\u90ae\u7bb1:", None))
        self.lb_password.setText(QCoreApplication.translate("AccountPage", u"\u767b\u9646\u5bc6\u7801:", None))

    # retranslateUi
