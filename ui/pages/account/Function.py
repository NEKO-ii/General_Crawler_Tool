# 用户界面操作逻辑模块
# ///////////////////////////////////////////////////////////////
from .Ui_AccountPage import Ui_AccountPage
from ui.dialog.Login import Login


class Func_AccountPage:
    ui: Ui_AccountPage

    def __init__(self, ui: Ui_AccountPage) -> None:
        self.ui = ui
        self._btnConnect()
        self._sigConnect()

    def _btnConnect(self) -> None:
        self.ui.btn_login.clicked.connect(self.solt_login)

    def _sigConnect(self) -> None:
        pass

    # 按钮动作方法定义
    # ///////////////////////////////////////////////////////////////
    def solt_login(self) -> None:
        login = Login()
        login.exec()

    # 信号动作方法定义
    # ///////////////////////////////////////////////////////////////
