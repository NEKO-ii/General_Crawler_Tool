from ui.preload.imp_qt import QLineEdit, QFont

# 样式表
# ///////////////////////////////////////////////////////////////
style = '''
QLineEdit:enabled {{
    background-color: {_background_color_enabled};
    border: 2px solid {_border_color_enabled};
    border-radius: {_radius}px;
    padding: 2px 5px 2px 5px;
    selection-color: {_selection_color};
    selection-background-color: {_selection_background_color};
    color: {_color_enabled};
}}
QLineEdit:disabled {{
    background-color: {_background_color_disabled};
    border: 2px solid {_border_color_disabled};
    border-radius: {_radius}px;
    padding: 2px 5px 2px 5px;
    color: {_color_disabled};
}}
QLineEdit:focus {{
    border: 2px solid {_border_color_pressed};
    background-color: {_background_color_pressed};
}}
'''


class LineEdit(QLineEdit):

    def __init__(self,
                 parent=None,
                 text="",
                 placeHolderText="",
                 color_enabled="#aaaabb",
                 color_disabled="#4f5b6e",
                 border_color_enabled="#3c4454",
                 border_color_disabled="#343b48",
                 border_color_pressed="#3f6fd1",
                 bg_color_enabled="#1b1e23",
                 bg_color_disabled="#21252d",
                 bg_color_pressed="#1b1e23",
                 selection_color="#f5f6f9",
                 selection_bg_color="#568af2",
                 radius=4,
                 fontFamily="JetBrains Mono") -> None:
        super().__init__()

        if parent:
            self.setParent(parent)
        if text:
            self.setText(text)
        if placeHolderText:
            self.setPlaceholderText(placeHolderText)

        self.setFont(QFont(fontFamily, 9))

        _styleFormat = style.format(_color_enabled=color_enabled,
                                    _color_disabled=color_disabled,
                                    _border_color_enabled=border_color_enabled,
                                    _border_color_disabled=border_color_disabled,
                                    _border_color_pressed=border_color_pressed,
                                    _background_color_enabled=bg_color_enabled,
                                    _background_color_disabled=bg_color_disabled,
                                    _background_color_pressed=bg_color_pressed,
                                    _selection_color=selection_color,
                                    _selection_background_color=selection_bg_color,
                                    _radius=radius,
                                    _font_family=fontFamily)
        self.setStyleSheet(_styleFormat)

    def setColor(self, ctype: str = "default") -> None:
        """切换文字颜色

        Args:
            ctype (str, optional): 颜色类型[default, info, warning, error, success]
        """
        color_enabled = "#aaaabb"
        color_disabled = "#4f5b6e"
        border_color_enabled = "#3c4454"
        border_color_disabled = "#343b48"
        border_color_pressed = "#3f6fd1"
        bg_color_enabled = "#1b1e23"
        bg_color_disabled = "#21252d"
        bg_color_pressed = "#1b1e23"
        selection_color = "#f5f6f9"
        selection_bg_color = "#568af2"
        radius = 4
        fontFamily = "JetBrains Mono"
        if ctype == "success":
            color_enabled = "#20cc5f"
            color_disabled = "#10a05f"
        elif ctype == "info":
            color_enabled = "#568af2"
            color_disabled = "#204070"
        elif ctype == "warning":
            color_enabled = "#f0f020"
            color_disabled = "#d0d040"
        elif ctype == "error":
            color_enabled = "#ff4040"
            color_disabled = "#aa2020"
        _styleFormat = style.format(_color_enabled=color_enabled,
                                    _color_disabled=color_disabled,
                                    _border_color_enabled=border_color_enabled,
                                    _border_color_disabled=border_color_disabled,
                                    _border_color_pressed=border_color_pressed,
                                    _background_color_enabled=bg_color_enabled,
                                    _background_color_disabled=bg_color_disabled,
                                    _background_color_pressed=bg_color_pressed,
                                    _selection_color=selection_color,
                                    _selection_background_color=selection_bg_color,
                                    _radius=radius,
                                    _font_family=fontFamily)
        self.setStyleSheet(_styleFormat)
