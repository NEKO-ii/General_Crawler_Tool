from .ui_page_start import Ui_StartPage
from .func_page_start import Func_StartPage


class StartPage:
    ui: Ui_StartPage
    func: Func_StartPage

    def __init__(self, page_start_widget, themes) -> None:
        self.ui = Ui_StartPage(page_start_widget, themes)
        self.func = Func_StartPage(self.ui)
