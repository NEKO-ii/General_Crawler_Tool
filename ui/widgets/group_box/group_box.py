from ui.preload.imp_qt import QGroupBox, Qt

style: str = '''
QGroupBox {{
    border: 1px solid {_border_color};
    border-radius: 4px;
    margin: 7px 5px 5px 5px;
    padding: 10px 0px 0px 0px;
}}
QGroupBox:title {{
    color: {_color};
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0px;
    left: 15px;
}}
QGroupBox:disabled {{
    color: {_color_disabled};
}}
'''


class GroupBox(QGroupBox):

    def __init__(self, parent=None, color="#aaaabb", color_disabled="#4f5b6e", border_color="#3c4454", scrollParent=None) -> None:
        super().__init__(parent)
        self._scrollParent = scrollParent
        self._sp_lock = False
        if scrollParent:
            self._sp_lock = True

        self.setFocusPolicy(Qt.NoFocus)

        style_format = style.format(_color=color, _color_disabled=color_disabled, _border_color=border_color)
        self.setStyleSheet(style_format)
