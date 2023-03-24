# 主窗口
# ///////////////////////////////////////////////////////////////
from core.sys import Settings, Themes
from core.static import Define
from .ui_main_window import Ui_MainWindow
from .func_main_window import MainWindow_Func


class MainWindow:
    """主窗口类
    """

    # 属性
    # ///////////////////////////////////////////////////////////////
    settings: Settings
    themes: Themes
    ui: Ui_MainWindow
    func: MainWindow_Func

    # ///////////////////////////////////////////////////////////////

    def __init__(self, settings) -> None:
        """创建主窗口并初始化

        Args:
            settings (Settings): 设置封装对象
        """
        self.settings = settings
        self.themes = Themes(self.settings.theme_name)
        self.ui = Ui_MainWindow(self.settings, self.themes)
        self.ui.setWindowTitle(Define.APP_NAME)
        self.ui.setObjectName("window_main")
        self.func = MainWindow_Func(self.ui)

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
