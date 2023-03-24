# 导航栏区域分隔线
# ///////////////////////////////////////////////////////////////
from ui.preload.imp_qt import QFrame, QHBoxLayout, QWidget


class SepLine(QWidget):
    """导航栏区域分隔线
    """

    def __init__(self, color) -> None:
        """初始化分隔线

        Args:
            color (str): RGB颜色字符串,如: #FFFFFF
        """
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(5,0,5,0)
        self.line = QFrame()
        self.line.setStyleSheet(F"background: {color};")
        self.line.setMaximumHeight(1)
        self.line.setMinimumHeight(1)
        self.layout.addWidget(self.line)
        self.setMaximumHeight(1)
