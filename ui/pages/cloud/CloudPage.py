from .Ui_CloudPage import Ui_CloudPage
from .Function import Func_CloudPage


class CloudPage:
    ui: Ui_CloudPage
    func: Func_CloudPage

    def __init__(self, cloudPageWidget) -> None:
        self.ui = Ui_CloudPage(cloudPageWidget)
        self.func = Func_CloudPage(self.ui)
