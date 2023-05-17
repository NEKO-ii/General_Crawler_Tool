from .Ui_AccountPage import Ui_AccountPage
from .Function import Func_AccountPage


class AccountPage:

    ui: Ui_AccountPage
    func: Func_AccountPage

    def __init__(self, AccountPage) -> None:
        self.ui = Ui_AccountPage(AccountPage)
        self.func = Func_AccountPage(self.ui)
