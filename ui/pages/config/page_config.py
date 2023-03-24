# 配置编辑主组件
# ///////////////////////////////////////////////////////////////
from .ui_page_config import Ui_Configuration
from .func_page_config import Func_ConfigPage


class ConfigPage:
    """配置编辑组件类
    """
    # 属性
    # ///////////////////////////////////////////////////////////////
    ui: Ui_Configuration
    func: Func_ConfigPage

    # ///////////////////////////////////////////////////////////////

    def __init__(self, page_config_widget, themes) -> None:
        self.ui = Ui_Configuration(page_config_widget, themes)
        self.func = Func_ConfigPage(self.ui)
