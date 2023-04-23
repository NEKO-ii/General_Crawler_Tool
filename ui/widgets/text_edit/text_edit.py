from ui.preload.imp_qt import QTextEdit, QWheelEvent, QTextCursor, QColor,QApplication

# 样式表
# ///////////////////////////////////////////////////////////////
style = '''
QTextEdit:enabled {{
    background-color: {_background_color_enabled};
    border: 2px solid {_border_color_enabled};
    border-radius: {_radius}px;
    padding: 2px 5px 2px 5px;
    selection-color: {_selection_color};
    selection-background-color: {_selection_background_color};
    color: {_color_enabled};
}}
QTextEdit:disabled {{
    background-color: {_background_color_disabled};
    border: 2px solid {_border_color_disabled};
    border-radius: {_radius}px;
    padding: 2px 5px 2px 5px;
    color: {_color_disabled};
}}
QTextEdit:focus {{
    border: 2px solid {_border_color_pressed};
    background-color: {_background_color_pressed};
}}

QScrollBar:horizontal {{
    border: none;
    background-color: {_background_color_enabled};
    height: 4px;
    margin: 0px 3px 0px 3px;
    border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background-color: {_selection_background_color};
    min-width: 25px;
    border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background-color: {_background_color_disabled};
    width: 20px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background-color: {_background_color_disabled};
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
    background-color: {_background_color_enabled};
    width: 4px;
    margin: 3px 0 3px 0;
    border-radius: 0px;
}}
QScrollBar::handle:vertical {{
    background-color: {_selection_background_color};
    min-height: 25px;
    border-radius: 4px
}}
QScrollBar::add-line:vertical {{
    border: none;
    background-color: {_background_color_disabled};
    height: 20px;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
    border: none;
    background-color: {_background_color_disabled};
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


class TextEdit(QTextEdit):
    color: dict = {
        "default": "#aaaabb",
        "success": "#20cc5f",
        "info": "#6c99f4",
        "warning": "#f0f020",
        "error": "#ff4040",
    }

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
                 maxHeight=None,
                 fontSize=9,
                 fontFamily="JetBrains Mono",
                 scrollParent=None) -> None:
        super().__init__()
        self._maxHeight = maxHeight
        self._color_enabled = color_enabled
        self._color_disabled = color_disabled
        self._fontFamily = fontFamily
        self._scrollParent = scrollParent
        self._sp_lock = False
        if scrollParent:
            self._sp_lock = True
        if parent:
            self.setParent(parent)
        if text:
            self.setText(text)
        if placeHolderText:
            self.setPlaceholderText(placeHolderText)
        if maxHeight:
            self.setMaximumHeight(maxHeight)
            self.document().contentsChanged.connect(self.text_area_changed)

        self.setFontPointSize(fontSize)
        self.setFontFamily(fontFamily)
        self.setLineWrapMode(QTextEdit.NoWrap)

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
                                    _radius=radius)
        self.setStyleSheet(_styleFormat)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if self.hasFocus() and self.isEnabled():
            return super().wheelEvent(event)
        else:
            if self._scrollParent:
                self._scrollParent.setFocus()
                return self._scrollParent.wheelEvent(event)

    def text_area_changed(self) -> None:
        self.document().adjustSize()
        new_height = self.document().size().height() + 10
        if new_height != self.height():
            if new_height < self.height(): new_height = self.height()
            if new_height > self._maxHeight: new_height = self._maxHeight
            self.setFixedHeight(new_height)

    def c_setScrollParent(self, sparent) -> None:
        """设置鼠标滚轮事件传递,若已通过构造函数设置,该函数无效
        Args:
            sparent (QObject): 目标组件
        """
        if self._sp_lock is False:
            self._scrollParent = sparent

    def c_addLines(self, data: list) -> None:
        for item in data:
            self.append(item)

    def c_getLines(self) -> list:
        return self.toPlainText().strip().split("\n")

    def c_appendWithColor(self, text: str, ctype="default", pre=None, after=None) -> None:
        """添加一行文本,设置文字颜色类型"""
        if ctype is None: ctype = "default"
        if pre: self.insertPlainText(pre)
        self.setTextColor(QColor(self.color[ctype]))
        self.insertPlainText(text)
        if self.isEnabled(): self.setTextColor(QColor(self._color_enabled))
        else: self.setTextColor(QColor(self._color_disabled))
        if after: self.insertPlainText(after)
        self.append("")
        # QApplication.processEvents()

    def c_insertWithColor(self, text: str, ctype="default", pre=None, after=None) -> None:
        """行末追加文本,设置文字颜色类型"""
        if ctype is None: ctype = "default"
        if pre: self.insertPlainText(pre)
        self.setTextColor(QColor(self.color[ctype]))
        self.insertPlainText(text)
        if self.isEnabled(): self.setTextColor(QColor(self._color_enabled))
        else: self.setTextColor(QColor(self._color_disabled))
        if after: self.insertPlainText(after)
        # QApplication.processEvents()
