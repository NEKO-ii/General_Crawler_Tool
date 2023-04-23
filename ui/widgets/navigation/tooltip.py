# 按钮提示框
# ///////////////////////////////////////////////////////////////
from ui.preload.imp_qt import QLabel, QGraphicsDropShadowEffect, QColor


class ToolTip(QLabel):
    """按钮提示框
    """
    # 样式表
    style: str = """
    QLabel {{
        background-color: {_background};
        color: {_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        border-left: 2px solid {_border_color};
        font: 500 9pt "Microsoft YaHei UI";
    }}
    """

    def __init__(self, container, text, bg_color, fg_color, border_color) -> None:
        QLabel.__init__(self)

        self._container = container
        self._text = text
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.border_color = border_color

        self.setObjectName("tooltip")
        self.setup()

    def setup(self) -> None:
        self.setStyleSheet(self.style.format(_background=self.bg_color, _foreground=self.fg_color, _border_color=self.border_color))
        self.setMinimumHeight(34)
        self.setParent(self._container)
        self.setText(self._text)
        self.adjustSize()  # 根据文本长度自适应大小

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)  # 阴影模糊半径
        self.shadow.setXOffset(0)  # X偏移
        self.shadow.setYOffset(0)  # Y偏移
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)
