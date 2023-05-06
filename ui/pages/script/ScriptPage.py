# 用户脚本管理主组件
# ///////////////////////////////////////////////////////////////
from .Ui_ScriptPage import Ui_ScriptPage
from .Function import Func_ScriptPage


class ScriptPage:
    """配置编辑组件类
    """
    # 属性
    # ///////////////////////////////////////////////////////////////
    ui: Ui_ScriptPage
    func: Func_ScriptPage

    # ///////////////////////////////////////////////////////////////

    def __init__(self, scriptPageWidget) -> None:
        self.ui = Ui_ScriptPage(scriptPageWidget)
        self.func = Func_ScriptPage()
