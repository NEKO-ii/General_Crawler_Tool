# 自定义滚动窗口
# ///////////////////////////////////////////////////////////////

from ui.preload.imp_qt import QScrollArea, QWidget, Qt, QWheelEvent

# 样式表
# ///////////////////////////////////////////////////////////////
style: str = '''
QScrollArea {{
    border: none;
}}
QScrollBar:horizontal {{
    border: none;
    background-color: {_background_color};
    height: 4px;
    margin: 0px 3px 0px 3px;
    border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background-color: {_background_color_handle};
    min-width: 25px;
    border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background-color: {_background_color_addline};
    width: 20px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background-color: {_background_color_subline};
    width: 20px;
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
    background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
    background: none;
}}

QScrollBar:vertical {{
    border: none;
    background-color: {_background_color};
    width: 4px;
    margin: 3px 0 3px 0;
    border-radius: 0px;
}}
QScrollBar::handle:vertical {{
    background-color: {_background_color_handle};
    min-height: 25px;
    border-radius: 4px
}}
QScrollBar::add-line:vertical {{
    border: none;
    background-color: {_background_color_addline};
    height: 20px;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
    border: none;
    background-color: {_background_color_subline};
    height: 20px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
    background: none;
}}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
    background: none;
}}
'''


class ScrollArea(QScrollArea):

    def __init__(self, parent: QWidget, bg_color="#2c313c", bg_color_handle="#568af2", bg_color_addline="#272c36", bg_color_subline="#272c36") -> None:
        super().__init__(parent)
        self.setFocusPolicy(Qt.WheelFocus)

        style_format = style.format(_background_color=bg_color, _background_color_handle=bg_color_handle, _background_color_addline=bg_color_addline, _background_color_subline=bg_color_subline)
        self.setStyleSheet(style_format)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if self.hasFocus():
            return super().wheelEvent(event)
