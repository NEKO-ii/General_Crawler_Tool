from ui.preload.imp_qt import QSpinBox, QWheelEvent, Qt

# 样式表
# ///////////////////////////////////////////////////////////////
style = '''
QSpinBox:enabled {{
    color: {_color_enabled};
    background-color: {_background_color_enabled};
    padding: 2px 5px 2px 5px;
    border: 2px solid {_border_color_enabled};
    border-radius: {_radius}px;
}}
QSpinBox:disabled {{
    color: {_color_disabled};
    background-color: {_background_color_disabled};
    padding: 2px 5px 2px 5px;
    border: 2px solid {_border_color_disabled};
    border-radius: {_radius}px;
}}
QSpinBox:focus {{
    border: 2px solid {_border_color_pressed};
    background-color: {_background_color_pressed};
}}
QSpinBox::up-button, QSpinBox::down-button {{
    width: 0px;
}}
'''


class SpinBox(QSpinBox):

    def __init__(self,
                 parent=None,
                 color_enabled="#aaaabb",
                 color_disabled="#4f5b6e",
                 border_color_enabled="#3c4454",
                 border_color_disabled="#343b48",
                 border_color_pressed="#3f6fd1",
                 bg_color_enabled="#1b1e23",
                 bg_color_disabled="#21252d",
                 bg_color_pressed="#1b1e23",
                 radius=4,
                 scroll_parent=None) -> None:
        super().__init__()
        self._scroll_parent = scroll_parent
        self._sp_lock = False
        if scroll_parent:
            self._sp_lock = True
        if parent:
            self.setParent(parent)
        self.setFocusPolicy(Qt.ClickFocus)

        style_format = style.format(_color_enabled=color_enabled,
                                    _color_disabled=color_disabled,
                                    _border_color_enabled=border_color_enabled,
                                    _border_color_disabled=border_color_disabled,
                                    _border_color_pressed=border_color_pressed,
                                    _background_color_enabled=bg_color_enabled,
                                    _background_color_disabled=bg_color_disabled,
                                    _background_color_pressed=bg_color_pressed,
                                    _radius=radius)
        self.setStyleSheet(style_format)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if self.hasFocus() and self.isEnabled():
            return super().wheelEvent(event)
        elif self._scroll_parent:
            self._scroll_parent.setFocus()
            return self._scroll_parent.wheelEvent(event)

    def set_scroll_parent(self, sparent) -> None:
        """设置鼠标滚轮事件传递,若已通过构造函数设置,该函数无效
        Args:
            sparent (QObject): 目标组件
        """
        if self._sp_lock is False:
            self._scroll_parent = sparent
