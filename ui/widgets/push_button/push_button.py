from ui.preload.imp_qt import Qt, QPushButton, Signal

style = '''
QPushButton:enabled {{
    border: {_border_width}px solid {_border_color_enabled};
    padding: 3px 15px 3px 15px;
    color: {_color_enabled};
    border-radius: {_radius}px;
    background-color: {_background_color_enabled};
    font: {_font_size}pt \"Microsoft YaHei UI\";
}}
QPushButton:disabled {{
    border: {_border_width}px solid {_border_color_disabled};
    padding: 3px 15px 3px 15px;
    color: {_color_disabled};
    border-radius: {_radius}px;
    background-color: {_background_color_disabled};
    font: {_font_size}pt \"Microsoft YaHei UI\";
}}
QPushButton:hover {{
    border-color: {_border_color_hover};
    background-color: {_background_color_hover};
}}
QPushButton:pressed {{
    color: {_color_pressed};
    border-color: {_border_color_pressed};
    background-color: {_background_color_pressed};
}}
'''


class PushButton(QPushButton):
    clicked = Signal(object)
    released = Signal(object)

    def __init__(self,
                 parent=None,
                 text=None,
                 tooltip=None,
                 color_enabled="#aaaabb",
                 color_disabled="#4f5b6e",
                 color_pressed="#3f6fd1",
                 border_color_enabled="#3c4454",
                 border_color_disabled="#343b48",
                 border_color_hover="#6c99f4",
                 border_color_pressed="#3f6fd1",
                 bg_color_enabled="#1b1e23",
                 bg_color_disabled="#21252d",
                 bg_color_hover="#21252d",
                 bg_color_pressed="#1b1e23",
                 border_width=1,
                 font_size=9,
                 radius=3,
                 mini_size=None,
                 type=None) -> None:
        """按钮初始化

        Args:
            parent (_type_, optional): 父组件 Defaults to None.
            text (_type_, optional): 按钮文字 Defaults to None.
            tooltip (_type_, optional): 按钮提示 Defaults to None.
            color_enabled (str, optional):  Defaults to "#aaaabb".
            color_disabled (str, optional):  Defaults to "#4f5b6e".
            color_pressed (str, optional):  Defaults to "#3f6fd1".
            border_color_enabled (str, optional):  Defaults to "#3c4454".
            border_color_disabled (str, optional):  Defaults to "#343b48".
            border_color_hover (str, optional):  Defaults to "#6c99f4".
            border_color_pressed (str, optional):  Defaults to "#3f6fd1".
            bg_color_enabled (str, optional):  Defaults to "#1b1e23".
            bg_color_disabled (str, optional):  Defaults to "#21252d".
            bg_color_hover (str, optional):  Defaults to "#21252d".
            bg_color_pressed (str, optional):  Defaults to "#1b1e23".
            border_width (int, optional):  Defaults to 1.
            font_size (int, optional):  Defaults to 9.
            radius (int, optional): 圆角半径 Defaults to 3.
            mini_size (list, optional): 最小尺寸[width, height] Defaults to None.
            type (str, optional): 按钮样式[success, primary, warning, error] Defaults to None(default dark).
        """
        super().__init__()

        self.setText(text)
        if parent:
            self.setParent(parent)
        if mini_size:
            self.setMinimumSize(mini_size[0], mini_size[1])
        if tooltip:
            self.setToolTip(tooltip)

        # 主题类型更改
        if type == "success":
            bg_color_enabled = "#20b05f"
            bg_color_hover = "#20cc5f"
            bg_color_pressed = "#20b05f"
            border_color_hover = "#dce1ec"
            color_enabled = "#222222"
            color_pressed = "#aaaaaa"
        elif type == "primary":
            bg_color_enabled = "#205090"
            bg_color_hover = "#3070a0"
            bg_color_pressed = "#205090"
            border_color_hover = "#aaaabb"
        elif type == "warning":
            bg_color_enabled = "#d0d040"
            bg_color_hover = "#f0f020"
            bg_color_pressed = "#d0d040"
            border_color_hover = "#f5f6f9"
            border_color_pressed = "#666666"
            color_enabled = "#222222"
            color_pressed = "#666666"
        elif type == "error":
            bg_color_enabled = "#cc3030"
            bg_color_hover = "#ff4040"
            bg_color_pressed = "#cc3030"
            border_color_hover = "#dce1ec"
            color_enabled = "#222222"
            color_pressed = "#aaaaaa"

        self.setCursor(Qt.PointingHandCursor)

        custom_style = style.format(_color_enabled=color_enabled,
                                    _color_disabled=color_disabled,
                                    _color_pressed=color_pressed,
                                    _border_color_enabled=border_color_enabled,
                                    _border_color_disabled=border_color_disabled,
                                    _border_color_hover=border_color_hover,
                                    _border_color_pressed=border_color_pressed,
                                    _background_color_enabled=bg_color_enabled,
                                    _background_color_disabled=bg_color_disabled,
                                    _background_color_hover=bg_color_hover,
                                    _background_color_pressed=bg_color_pressed,
                                    _border_width=border_width,
                                    _radius=radius,
                                    _font_size=font_size)
        self.setStyleSheet(custom_style)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.objectName())
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.released.emit(self.objectName())
        return super().mouseReleaseEvent(event)
