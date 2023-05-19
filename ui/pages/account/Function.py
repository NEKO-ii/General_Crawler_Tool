# 用户界面操作逻辑模块
# ///////////////////////////////////////////////////////////////
from copy import deepcopy
from core.sys.cloud import getHeadImage, deleteAccount
from core.sys.file import File, SysPath
from core.sys.globalv import Globalv, GlvKey
from core.sys.accountstate import AccountState
from ui.dialog.Login import Login
from ui.dialog.Question import Question
from ui.dialog.Notice import Notice
from ui.func.iconsetter import IconSetter
from ui.preload.imp_qt import QPainter, QPainterPath, QPixmap, Qt

from .Ui_AccountPage import Ui_AccountPage


class Func_AccountPage:
    ui: Ui_AccountPage

    userinfo: dict

    def __init__(self, ui: Ui_AccountPage) -> None:
        self.ui = ui
        self.login = Login()
        self.accountState: AccountState = Globalv.get(GlvKey.ACCOUNT_STATE)
        self._btnConnect()
        self._sigConnect()

    def _btnConnect(self) -> None:
        self.ui.btn_login.clicked.connect(self.solt_show_login_dialog)
        self.ui.btn_delAccount.clicked.connect(self.solt_delAccount)
        self.ui.btn_logout.clicked.connect(self.solt_logout)
        self.ui.btn_updateAccount.clicked.connect(self.solt_updateAccount)

    def _sigConnect(self) -> None:
        self.login.sig_loginSucceed.connect(self.solt_set_user_info)
        self.login.sig_passwordUpdated.connect(self.solt_password_updated)

    # 按钮动作方法定义
    # ///////////////////////////////////////////////////////////////
    def solt_show_login_dialog(self) -> None:
        self.login.page.setCurrentIndex(0)
        self.login.ledit_username.clear()
        self.login.ledit_password.clear()
        self.login.exec()

    def solt_logout(self) -> None:
        self.accountState._isLoginSucceed = False
        self.accountState.clear()
        self.ui.btn_delAccount.hide()
        self.ui.btn_updateAccount.hide()
        self.ui.btn_logout.hide()
        self.ui.btn_login.show()
        self.ui.lb_username.setText("未登录")
        self.ui.lb_username.setStyleSheet("font: 13pt; color: orange;")
        self.ui.lb_email.setText("--")
        self.ui.lb_uid.setText("--")
        pix = QPixmap(IconSetter.setSvgIcon("icon_account.svg"))
        pix.scaled(self.ui.lb_image.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.ui.lb_image.setPixmap(pix)

        self.ui.ledit_requestCount.clear()
        self.ui.ledit_configCount.clear()
        self.ui.ledit_ctime.clear()
        self.ui.ledit_utime.clear()
        self.ui.ledit_email.clear()
        self.ui.ledit_password.clear()

    def solt_delAccount(self) -> None:
        global USER_INFO
        question: Question = Question()
        if question.exec("警告", "删除账户将从数据库中删除此账户全部信息,包括所有云数据\n是否继续?", "warn", "warn"):
            resp = deleteAccount(USER_INFO["userId"])
            flag = resp["flag"]
            msg = resp["msg"]
            notice = Notice()
            if flag:
                notice.exec("提示", msg)
            else:
                notice.exec("提示", msg)
        else:
            pass

    def solt_updateAccount(self) -> None:
        self.login.solt_to_retrieve_page()
        self.login.btn_back_rt.hide()
        self.login.exec()
        self.login.btn_back_rt.show()

    def solt_password_updated(self) -> None:
        notice = Notice()
        self.solt_logout()
        notice.exec("提示", "密码更新成功, 请重新登录")

    # 信号动作方法定义
    # ///////////////////////////////////////////////////////////////
    def solt_set_user_info(self, data: dict) -> None:
        self.accountState.update(data)
        uid = str(self.accountState._userId).rjust(10, '0')
        self.ui.lb_username.setText(self.accountState._username)
        self.ui.lb_username.setStyleSheet("font: 13pt; color: green;")
        self.ui.lb_email.setText(self.accountState._email)
        self.ui.lb_uid.setText(F"UID: {uid}")
        self.ui.btn_login.hide()
        self.ui.btn_delAccount.show()
        self.ui.btn_updateAccount.show()
        self.ui.btn_logout.show()

        self.ui.ledit_requestCount.setText(F"{self.accountState._requestCount} / 200")
        self.ui.ledit_configCount.setText(F"{self.accountState._configSaveCount} / 80")
        self.ui.ledit_ctime.setText(self.accountState._createTime)
        self.ui.ledit_utime.setText(self.accountState._updateTime)
        self.ui.ledit_email.setText(self.accountState._email)
        self.ui.ledit_password.setText(self.accountState._password)

        resp = getHeadImage(uid, self.accountState._headImageType)
        if resp["flag"]:
            bl = resp["data"]
            imgbytes = bytes([b + 256 if b < 0 else b for b in bl])
            himgname = resp["msg"]
            path = File.path(SysPath.BASE, "ui\\resources\\head_images", himgname)
            with open(path, "wb") as file:
                file.write(imgbytes)
            pix = QPixmap(path)
            pix.scaled(self.ui.lb_image.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
            width = self.ui.lb_image.size().width()
            height = self.ui.lb_image.size().height()
            image = QPixmap(width, height)
            image.fill(Qt.transparent)
            pp = QPainterPath()
            pp.addEllipse(0, 0, width, height)
            painter = QPainter(image)
            painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            painter.setClipPath(pp)
            painter.drawPixmap(0, 0, width, height, pix)
            painter.end()
            self.ui.lb_image.setPixmap(image)
