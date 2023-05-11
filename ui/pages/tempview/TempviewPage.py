# 临时数据管理主组件
# ///////////////////////////////////////////////////////////////
from .Ui_TempviewPage import Ui_TempviewPage
from .Function import Func_TempviewPage


class TempviewPage:
    """配置编辑组件类
    """
    # 属性
    # ///////////////////////////////////////////////////////////////
    ui: Ui_TempviewPage
    func: Func_TempviewPage

    # ///////////////////////////////////////////////////////////////

    def __init__(self, tempviewPageWidget) -> None:
        self.ui = Ui_TempviewPage(tempviewPageWidget)
        self.func = Func_TempviewPage(self.ui)
