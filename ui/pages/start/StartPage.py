from .Ui_StartPage import Ui_StartPage
from .Function import Func_StartPage


class StartPage:
    ui: Ui_StartPage
    func: Func_StartPage

    def __init__(self, startPageWidget) -> None:
        self.ui = Ui_StartPage(startPageWidget)
        self.func = Func_StartPage(self.ui)
