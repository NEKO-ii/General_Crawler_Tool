from .Ui_AnalysisPage import Ui_AnalysisPage
from .Function import Func_AnalysisPage


class AnalysisPage:
    ui: Ui_AnalysisPage
    func: Func_AnalysisPage

    def __init__(self, AnalysisPage) -> None:
        self.ui = Ui_AnalysisPage()
        self.ui.setupUi(AnalysisPage)
        self.func = Func_AnalysisPage(self.ui)
