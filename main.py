import os
import sys
import threading

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from core.sys import Settings, Path
from ui.windows.main.MainWindow import MainWindow
import test


class System:
    app: QApplication
    path: Path
    settings: Settings
    window: MainWindow

    def __init__(self) -> None:
        # 调整Qt字体DPI为4K显示器的高刻度
        os.environ["QT_FONT_DPI"] = "96"

        # 初始化静态变量
        self.path = Path()
        self.settings = Settings()
        self.path.update()
        self.path.folder_check()
        self.path.file_check()

        self.app = QApplication(sys.argv)
        self.app.setWindowIcon(QIcon("icon.ico"))

        self.window = MainWindow(self.settings)

    def run(self) -> None:
        self.window.show()


if __name__ == '__main__':
    system: System = System()
    system.run()
    # 调用测试方法
    test.test()
    # 将窗口关闭信号映射到系统退出
    sys.exit(system.app.exec())
