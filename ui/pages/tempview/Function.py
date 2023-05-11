from .Ui_TempviewPage import Ui_TempviewPage


class Func_TempviewPage:
    ui: Ui_TempviewPage

    def __init__(self, ui) -> None:
        self.ui = ui
        self._createDialog()
        self._btnConnect()
        self._signalConnect()

    def _btnConnect(self) -> None:
        pass

    def _signalConnect(self) -> None:
        pass

    def _createDialog(self) -> None:
        pass

    # 方法
    # ///////////////////////////////////////////////////////////////

    # 按钮动作定义
    # ///////////////////////////////////////////////////////////////

    # 信号动作定义
    # ///////////////////////////////////////////////////////////////
