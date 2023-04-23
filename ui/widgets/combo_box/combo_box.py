from ui.preload.imp_qt import QComboBox, QWheelEvent, Signal

style: str = '''
QComboBox:enabled {{
    border: 1px solid {_border_color_enabled};
    border-radius: {_radius};
    padding: 2px 5px 2px 5px;
    color: {_color_enabled};
    background-color: {_background_color_enabled};
}}
QComboBox:disabled {{
    border: 1px solid {_border_color_disabled};
    border-radius: {_radius};
    padding: 2px 5px 2px 5px;
    color: {_color_disabled};
    background-color: {_background_color_disabled};
}}
QComboBox:hover {{
    border-color: {_border_color_hover};
    background-color: {_background_color_hover};
}}
QComboBox:on {{
    border-color: {_border_color_pressed};
    background-color: {_background_color_pressed};
    color: {_color_pressed};
}}
QComboBox QAbstractItemView {{
    outline: none;
    border: 1px solid {_border_color_pressed};
    color: {_color_enabled};
    background-color: {_background_color_enabled};
    selection-background-color: {_background_color_pressed};
}}
QComboBox::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    background-color: transparent;
    border-left: 0px solid {_border_color_enabled};
    border-top-right-radius: {_radius};
    border-bottom-right-radius: {_radius};
}}
QComboBox::down-arrow {{
    width: 20px;
    padding: 0px 0px 0px 0px;
    image: url(ui/resources/icons/icon_arrow_down.png);
}}
'''


class ComboBox(QComboBox):
    sig_currentTextChanged = Signal(object)
    sig_currentIndexChanged = Signal(object)

    def __init__(self,
                 parent=None,
                 tooltip: str = None,
                 color_enabled="#aaaabb",
                 color_disabled="#4f5b6e",
                 color_pressed="#568af2",
                 border_color_enabled="#3c4454",
                 border_color_disabled="#343b48",
                 border_color_hover="#6c99f4",
                 border_color_pressed="#3f6fd1",
                 bg_color_enabled="#1b1e23",
                 bg_color_disabled="#272c36",
                 bg_color_hover="#21252d",
                 bg_color_pressed="#21252d",
                 radius=3,
                 minimumSize=None,
                 scrollParent=None) -> None:
        super().__init__()
        self._scrollParent = scrollParent
        self._sp_lock = False
        if scrollParent:
            self._sp_lock = True
        if parent:
            self.setParent(parent)
        if minimumSize:
            self.setMinimumSize(minimumSize[0], minimumSize[1])
        if tooltip:
            self.setToolTip(tooltip)

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
                                    _radius=radius)
        self.setStyleSheet(custom_style)

        self.currentTextChanged.connect(self.textChanged)
        self.currentIndexChanged.connect(self.indexChanged)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if self._scrollParent:
            self._scrollParent.setFocus()
            return self._scrollParent.wheelEvent(event)

    # 当前文本变化时发送自定义信号: current_text_changed
    def textChanged(self) -> None:
        self.sig_currentTextChanged.emit(self.currentText())

    # 当前索引变化时发送自定义信号: current_index_changed
    def indexChanged(self) -> None:
        self.sig_currentIndexChanged.emit(self.currentIndex())

    def c_setScrollParent(self, sparent) -> None:
        """设置鼠标滚轮事件传递,若已通过构造函数设置,该函数无效
        Args:
            sparent (QObject): 目标组件
        """
        if self._sp_lock is False:
            self._scrollParent = sparent
