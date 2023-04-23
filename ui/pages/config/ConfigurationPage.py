# 配置编辑主组件
# ///////////////////////////////////////////////////////////////
from .Ui_ConfigurationPage import Ui_ConfigurationPage
from .Function import Func_ConfigPage


class ConfigurationPage:
    """配置编辑组件类
    """
    # 属性
    # ///////////////////////////////////////////////////////////////
    ui: Ui_ConfigurationPage
    func: Func_ConfigPage

    # ///////////////////////////////////////////////////////////////

    def __init__(self, configPageWidget, themes) -> None:
        self.ui = Ui_ConfigurationPage(configPageWidget, themes)
        self.func = Func_ConfigPage(self.ui)
