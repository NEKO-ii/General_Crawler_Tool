import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from core.sys.settings import Settings
from core.sys.themes import Themes
from core.sys.path import Path
from core.sys.globalv import Globalv, GlvKey
from ui.windows.main.MainWindow import MainWindow


class System:
    app: QApplication
    window: MainWindow

    def __init__(self) -> None:
        # 调整Qt字体DPI为4K显示器的高刻度
        os.environ["QT_FONT_DPI"] = "96"

        # 初始化全局变量
        Globalv.init()
        Globalv.set(GlvKey.SETTINGS, Settings())
        Globalv.set(GlvKey.THEMES, Themes(Globalv.get(GlvKey.SETTINGS).theme_name))
        Globalv.set(GlvKey.PATH, Path())

        self.app = QApplication(sys.argv)
        self.app.setWindowIcon(QIcon("icon.ico"))

        self.window = MainWindow()

    def run(self) -> None:
        self.window.show()


if __name__ == '__main__':
    system: System = System()
    system.run()
    # 调用测试方法
    # test.test()
    # 将窗口关闭信号映射到系统退出
    sys.exit(system.app.exec())
