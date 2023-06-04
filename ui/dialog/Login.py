# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, Signal)
from PySide6.QtWidgets import (QDialog, QFormLayout, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from PySide6.QtGui import QFont
from ui.widgets import PushButton, LineEdit
from core.sys.emails import Emails
from core.sys.cloud import login, signup, isUserExists, updatePassword
from core.sys.globalv import Globalv, GlvKey
from core.sys.accountstate import AccountState
from .Notice import Notice
from re import match


class Login(QDialog):
    sig_loginSucceed = Signal(dict)
    sig_passwordUpdated = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setupUi(self)
        self._btnConnect()
        self._sigConnect()
        self.setWindowTitle("登陆")
        self.page.setCurrentIndex(0)
        self.accountState: AccountState = Globalv.get(GlvKey.ACCOUNT_STATE)

    def _btnConnect(self) -> None:
        self.btn_reject.clicked.connect(self.reject)
        self.btn_retrieve.clicked.connect(self.solt_to_retrieve_page)
        self.btn_signup.clicked.connect(self.solt_to_signup_page)
        self.btn_login.clicked.connect(self.solt_login)

        self.btn_sendvcode_su.clicked.connect(self.solt_sendvcode)
        self.btn_back_su.clicked.connect(lambda: self.page.setCurrentIndex(0))
        self.btn_check_su.clicked.connect(self.solt_check_signup_form)
        self.btn_signup_su.clicked.connect(self.solt_signup)

        self.btn_back_rt.clicked.connect(lambda: self.page.setCurrentIndex(0))
        self.btn_check_rt.clicked.connect(self.solt_check_retrieve_form)
        self.btn_retrieve_rt.clicked.connect(self.solt_retrieve)
        self.btn_sendvcode_rt.clicked.connect(self.solt_sendvcode)

    def _sigConnect(self) -> None:
        self.page.currentChanged.connect(self.solt_set_window_title)

    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(450, 200)
        self.horizontalLayout_3 = QHBoxLayout(Login)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page = QStackedWidget(Login)
        self.page_login = QWidget()
        self.verticalLayout = QVBoxLayout(self.page_login)
        self.formLayout = QFormLayout()
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setVerticalSpacing(15)

        self.label = QLabel(self.page_login)
        self.label.setFont(QFont(["JetBrains Mono", "微软雅黑"], 13))
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ledit_username = LineEdit(self.page_login)
        self.ledit_username.setMinimumHeight(40)
        self.ledit_username.setFont(QFont(["JetBrains Mono", "微软雅黑"], 13))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ledit_username)

        self.label_2 = QLabel(self.page_login)
        self.label_2.setFont(QFont(["JetBrains Mono", "微软雅黑"], 13))
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.ledit_password = LineEdit(self.page_login)
        self.ledit_password.setMinimumHeight(40)
        font = QFont(["JetBrains Mono", "微软雅黑"], 13)
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 5.0)
        self.ledit_password.setFont(font)
        self.ledit_password.setEchoMode(LineEdit.EchoMode.Password)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ledit_password)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_loginMsg = QLabel(self.page_login)
        self.label_loginMsg.setStyleSheet("color: red;")
        self.horizontalLayout_2.addWidget(self.label_loginMsg)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.btn_reject = PushButton(self.page_login)
        self.horizontalLayout.addWidget(self.btn_reject)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_retrieve = PushButton(self.page_login, type="primary")
        self.horizontalLayout.addWidget(self.btn_retrieve)

        self.btn_signup = PushButton(self.page_login, type="primary")
        self.horizontalLayout.addWidget(self.btn_signup)

        self.btn_login = PushButton(self.page_login, type="success")
        self.horizontalLayout.addWidget(self.btn_login)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.page.addWidget(self.page_login)

        self.page_signup = QWidget()
        self.verticalLayout_2 = QVBoxLayout(self.page_signup)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setLabelAlignment(Qt.AlignRight)
        self.label_4 = QLabel(self.page_signup)
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.ledit_username_su = LineEdit(self.page_signup)
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.ledit_username_su)

        self.label_5 = QLabel(self.page_signup)
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.ledit_password_su = LineEdit(self.page_signup)
        self.ledit_password_su.setEchoMode(LineEdit.EchoMode.Password)
        font = QFont(["JetBrains Mono", "微软雅黑"], 9)
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 2.0)
        self.ledit_password_su.setFont(font)
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.ledit_password_su)

        self.label_6 = QLabel(self.page_signup)
        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.page_signup)
        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.ledit_vcode_su = LineEdit(self.page_signup)
        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.ledit_vcode_su)

        self.horizontalLayout_5 = QHBoxLayout()
        self.ledit_email_su = LineEdit(self.page_signup)
        self.horizontalLayout_5.addWidget(self.ledit_email_su)

        self.btn_sendvcode_su = PushButton(self.page_signup, type="primary")
        self.btn_sendvcode_su.setObjectName("svcsu")
        self.horizontalLayout_5.addWidget(self.btn_sendvcode_su)

        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.lable_check_su = QLabel(self.page_signup)
        self.lable_check_su.setStyleSheet("color: red;")
        self.horizontalLayout_6.addWidget(self.lable_check_su)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.btn_back_su = PushButton(self.page_signup)
        self.horizontalLayout_4.addWidget(self.btn_back_su)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_check_su = PushButton(self.page_signup, type="primary")
        self.horizontalLayout_4.addWidget(self.btn_check_su)

        self.btn_signup_su = PushButton(self.page_signup, type="success")
        self.horizontalLayout_4.addWidget(self.btn_signup_su)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.page.addWidget(self.page_signup)

        self.page_retrieve = QWidget()
        self.verticalLayout_3 = QVBoxLayout(self.page_retrieve)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setLabelAlignment(Qt.AlignRight)
        self.label_8 = QLabel(self.page_retrieve)
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.ledit_username_rt = LineEdit(self.page_retrieve)
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.ledit_username_rt)

        self.label_9 = QLabel(self.page_retrieve)
        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.ledit_email_rt = LineEdit(self.page_retrieve)
        self.horizontalLayout_7.addWidget(self.ledit_email_rt)

        self.btn_sendvcode_rt = PushButton(self.page_retrieve, type="primary")
        self.btn_sendvcode_rt.setObjectName("svcrt")
        self.horizontalLayout_7.addWidget(self.btn_sendvcode_rt)

        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_10 = QLabel(self.page_retrieve)
        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.ledit_vcode_rt = LineEdit(self.page_retrieve)
        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.ledit_vcode_rt)

        self.label_11 = QLabel(self.page_retrieve)
        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.ledit_password_rt = LineEdit(self.page_retrieve)
        self.ledit_password_rt.setEchoMode(LineEdit.EchoMode.Password)
        self.ledit_password_rt.setFont(font)
        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.ledit_password_rt)

        self.label_12 = QLabel(self.page_retrieve)
        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_12)

        self.ledit_password_re_rt = LineEdit(self.page_retrieve)
        self.ledit_password_re_rt.setEchoMode(LineEdit.EchoMode.Password)
        self.ledit_password_re_rt.setFont(font)
        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.ledit_password_re_rt)

        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.lable_check_rt = QLabel(self.page_retrieve)
        self.lable_check_rt.setStyleSheet("color: red;")
        self.horizontalLayout_8.addWidget(self.lable_check_rt)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.btn_back_rt = PushButton(self.page_retrieve)
        self.horizontalLayout_9.addWidget(self.btn_back_rt)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.btn_check_rt = PushButton(self.page_retrieve, type="primary")
        self.horizontalLayout_9.addWidget(self.btn_check_rt)

        self.btn_retrieve_rt = PushButton(self.page_retrieve, type="success")
        self.horizontalLayout_9.addWidget(self.btn_retrieve_rt)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.page.addWidget(self.page_retrieve)

        self.horizontalLayout_3.addWidget(self.page)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"\u767b\u9646", None))
        self.label.setText(QCoreApplication.translate("Login", u"\u7528\u6237\u540d:", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"\u5bc6\u3000\u7801:", None))
        self.label_loginMsg.setText(QCoreApplication.translate("Login", u"msg", None))
        self.btn_reject.setText(QCoreApplication.translate("Login", u"\u53d6\u6d88", None))
        self.btn_retrieve.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801\u627e\u56de", None))
        self.btn_signup.setText(QCoreApplication.translate("Login", u"\u6ce8\u518c", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"\u767b\u9646", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"\u7528\u6237\u540d:", None))
        self.label_5.setText(QCoreApplication.translate("Login", u"\u5bc6\u3000\u7801:", None))
        self.label_6.setText(QCoreApplication.translate("Login", u"\u90ae\u3000\u7bb1:", None))
        self.label_7.setText(QCoreApplication.translate("Login", u"\u9a8c\u8bc1\u7801:", None))
        self.btn_sendvcode_su.setText(QCoreApplication.translate("Login", u"\u83b7\u53d6\u9a8c\u8bc1\u7801", None))
        self.lable_check_su.setText(QCoreApplication.translate("Login", u"\u672a\u68c0\u6d4b", None))
        self.btn_back_su.setText(QCoreApplication.translate("Login", u"\u8fd4\u56de", None))
        self.btn_check_su.setText(QCoreApplication.translate("Login", u"\u68c0\u67e5", None))
        self.btn_signup_su.setText(QCoreApplication.translate("Login", u"\u6ce8\u518c", None))
        self.label_8.setText(QCoreApplication.translate("Login", u"\u7528\u6237\u540d:", None))
        self.label_9.setText(QCoreApplication.translate("Login", u"\u90ae\u3000\u7bb1:", None))
        self.label_10.setText(QCoreApplication.translate("Login", u"\u9a8c\u8bc1\u7801:", None))
        self.label_11.setText(QCoreApplication.translate("Login", u"\u65b0\u5bc6\u7801:", None))
        self.label_12.setText(QCoreApplication.translate("Login", u"\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801:", None))
        self.lable_check_rt.setText(QCoreApplication.translate("Login", u"\u672a\u68c0\u67e5", None))
        self.btn_back_rt.setText(QCoreApplication.translate("Login", u"\u8fd4\u56de", None))
        self.btn_check_rt.setText(QCoreApplication.translate("Login", u"\u68c0\u67e5", None))
        self.btn_retrieve_rt.setText(QCoreApplication.translate("Login", u"\u786e\u8ba4", None))
        self.btn_sendvcode_rt.setText(QCoreApplication.translate("Login", u"\u53d1\u9001\u9a8c\u8bc1\u7801", None))

    def checkEmailAddr(self, email) -> bool:
        """检查邮件地址格式是否合法

        Args:
            email (str): 邮件地址

        Returns:
            bool: 返回布尔值
        """
        pattern = r'^([a-zA-Z0-9._+-]+)@([a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+)$'
        return match(pattern, email) is not None

    # 槽函数
    # ///////////////////////////////////////////////////////////////
    def solt_login(self) -> None:
        resp = login(self.ledit_username.text().strip(), self.ledit_password.text().strip())
        flag: bool = resp["flag"]
        data: dict = resp["data"]
        msg: str = resp["msg"]
        if flag:
            self.sig_loginSucceed.emit(data)
            self.accountState._isLoginSucceed = True
            self.accept()
        else:
            self.label_loginMsg.setText(msg)
            self.label_loginMsg.show()

    def solt_sendvcode(self, objname) -> None:
        # emailAddrs = self.ledit_email_su.text()
        # emails = Emails()
        # if emails.flag_connect:
        #     flag, code, msg = emails.sendVerificationCode(emailAddrs)
        #     emails.close()
        #     print(F"{flag}, {code}, {msg}")
        #     if flag:
        #         pass
        #     else:
        #         pass
        # else:
        #     print(emails.errmsg)
        emailAddrs = self.ledit_email_su.text()
        emails = Emails()
        flag, code, msg = emails.sendVerificationCode(emailAddrs)
        if objname == "svcsu":
            self.ledit_vcode_su.setText(code)
        elif objname == "svcrt":
            self.ledit_vcode_rt.setText(code)

    def solt_check_signup_form(self) -> bool:
        username = self.ledit_username_su.text().strip()
        password = self.ledit_password_su.text().strip()
        email = self.ledit_email_su.text().strip()
        vcode = self.ledit_vcode_su.text().strip()
        flag = True
        if username == "":
            flag = False
            self.lable_check_su.setText("用户名不能为空")
        if flag:
            if password == "":
                flag = False
                self.lable_check_su.setText("密码不能为空")
            elif len(password) < 6:
                flag = False
                self.lable_check_su.setText("密码长度最小为6")
            elif password.find(" ") != -1:
                flag = False
                self.lable_check_su.setText("密码不能包含空格")
        if flag:
            if email == "":
                flag = False
                self.lable_check_su.setText("邮箱不能为空")
            elif self.checkEmailAddr(email) is False:
                flag = False
                self.lable_check_su.setText("邮箱地址错误")
        if flag:
            if vcode == "":
                flag = False
                self.lable_check_su.setText("请输入验证码")
        if flag:
            if isUserExists("username", username)["flag"]:
                flag = False
                self.lable_check_su.setText("用户名已被注册")

        if flag:
            self.lable_check_su.setStyleSheet("color: green;")
            self.lable_check_su.setText("数据可用")
        else:
            self.lable_check_su.setStyleSheet("color: red;")

    def solt_signup(self) -> None:
        if self.solt_check_signup_form():
            username = self.ledit_username_su.text().strip()
            password = self.ledit_password_su.text().strip()
            email = self.ledit_email_su.text().strip()
            resp = signup(username, password, email)
            flag = resp["flag"]
            if flag:
                self.accept()
            else:
                Notice().exec("错误", F"账户注册失败\n{resp['msg']}")

    def solt_check_retrieve_form(self) -> bool:
        flag: bool = False
        username = self.ledit_username_rt.text().strip()
        # email = self.ledit_email_rt.text().strip()
        # vcode = self.ledit_vcode_rt.text().strip()
        # TODO: 验证码邮箱验证
        passw1 = self.ledit_password_rt.text().strip()
        passw2 = self.ledit_password_re_rt.text().strip()
        if username == "":
            self.lable_check_rt.setText("用户名不能为空")
        else:
            if passw1 == "" and passw2 == "":
                self.lable_check_rt.setText("密码不能为空")
            else:
                if passw1 == self.accountState._password:
                    self.lable_check_rt.setText("不能使用当前密码")
                else:
                    if passw1 != passw2:
                        self.lable_check_rt.setText("两次密码输入不一致")
                    else:
                        resp = isUserExists("username", username)
                        if resp["flag"]:
                            flag = True
                        else:
                            self.lable_check_rt.setText("用户名不存在")
        if flag:
            self.lable_check_rt.setStyleSheet("color: green;")
            self.lable_check_rt.setText("数据可用")
        else:
            self.lable_check_rt.setStyleSheet("color: red;")

        return flag

    def solt_retrieve(self) -> None:
        if self.solt_check_retrieve_form():
            username = self.ledit_username_rt.text().strip()
            passw1 = self.ledit_password_rt.text().strip()
            resp = updatePassword(username, passw1)
            if resp["flag"]:
                self.hide()
                self.sig_passwordUpdated.emit()
                self.accept()
            else:
                self.lable_check_rt.setText("密码更新失败")

    def solt_to_signup_page(self) -> None:
        self.solt_clear_signup_page()
        self.page.setCurrentIndex(1)

    def solt_to_retrieve_page(self) -> None:
        self.solt_clear_retrieve_page()
        self.page.setCurrentIndex(2)

    def solt_clear_signup_page(self) -> None:
        self.ledit_username_su.clear()
        self.ledit_password_su.clear()
        self.ledit_email_su.clear()
        self.ledit_vcode_su.clear()
        self.lable_check_su.setText("未检查")
        self.lable_check_su.setStyleSheet("color: #aaaabb;")

    def solt_clear_retrieve_page(self) -> None:
        self.ledit_username_rt.clear()
        self.ledit_email_rt.clear()
        self.ledit_vcode_rt.clear()
        self.ledit_password_rt.clear()
        self.ledit_password_re_rt.clear()
        self.lable_check_rt.setText("未检查")
        self.lable_check_rt.setStyleSheet("color: #aaaabb;")

    def solt_set_window_title(self) -> None:
        if self.page.currentIndex() == 0:
            self.setWindowTitle("登陆")
        elif self.page.currentIndex() == 1:
            self.setWindowTitle("注册账户")
        elif self.page.currentIndex() == 2:
            self.setWindowTitle("修改密码")

    def exec(self) -> None:
        self.label_loginMsg.hide()
        super().exec()
