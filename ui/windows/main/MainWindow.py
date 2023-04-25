# 主窗口
# ///////////////////////////////////////////////////////////////
from core.sys import Settings, Themes
from core.static import Define
from .Ui_MainWindow import Ui_MainWindow
from .Function import Func_MainWindow


class MainWindow:
    """主窗口类
    """

    # 属性
    # ///////////////////////////////////////////////////////////////
    ui: Ui_MainWindow
    func: Func_MainWindow

    # ///////////////////////////////////////////////////////////////

    def __init__(self) -> None:
        """创建主窗口并初始化

        Args:
            settings (Settings): 设置封装对象
        """
        self.ui = Ui_MainWindow()
        self.ui.setWindowTitle(Define.APP_NAME)
        self.ui.setObjectName("window_main")
        self.func = Func_MainWindow(self.ui)

    # API
    # ///////////////////////////////////////////////////////////////
    def show(self) -> None:
        """显示主窗口
        """
        self.ui.show()

    def hide(self) -> None:
        """隐藏主窗口
        """
        self.ui.hide()
