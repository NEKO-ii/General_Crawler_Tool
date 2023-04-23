# 自定义列表组件
# ///////////////////////////////////////////////////////////////

from ui.preload.imp_qt import QListWidget, QAbstractItemView, Qt, QModelIndex, QWheelEvent, QKeyEvent, QListWidgetItem

# 样式表
# ///////////////////////////////////////////////////////////////
style: str = '''
QListWidget {{
    background-color: {_background_color};
    color: {_color};
    border: 1px solid {_border_color};
    border-radius: 5px;
    outline: 0px;
    padding: 5px;
    font: {_font_size}pt {_font_family};
}}
QListWidget:disabled {{
    background-color: {_background_color_disabled};
    color: {_color_disabled};
    border: 1px solid {_border_color_disabled};
    border-radius: 5px;
    outline: 0px;
    padding: 5px;
    font: {_font_size}pt {_font_family};
}}
QListWidget::item {{
    border: none;
    border-radius: {_radius}px;
    margin: 1px 5px 1px 0px;
    padding: {_padding} 0px {_padding} 0px;
}}
QListWidget::item:hover {{
    background-color: {_background_color_hover};
    border: 1px solid {_border_color_hover};
    border-radius: {_radius}px;
}}
QListWidget::item:selected {{
    color: {_color_selected};
    background-color: {_background_color_selected};
    border: none;
    border-radius: {_radius}px;
}}
QListWidget::item::selected:active {{
    color: {_color_selected};
    background-color: {_background_color_active};
    border: none;
    border-radius: {_radius}px;
}}
'''


class List(QListWidget):

    def __init__(self,
                 parent=None,
                 color="#aaaabb",
                 color_disabled="#4f5b6e",
                 color_selected="#f5f6f9",
                 bg_color="#1e2229",
                 bg_color_disabled="#21252d",
                 bg_color_hover="#2c313c",
                 bg_color_selected="#204070",
                 bg_color_active="#205090",
                 border_color="#3c4454",
                 border_color_disabled="#272c36",
                 border_color_hover="#6c99f4",
                 enableEdit: bool = True,
                 enableDropDrag: bool = False,
                 radius=2,
                 padding=1,
                 fontSize=9,
                 fontFamily="JetBrains Mono",
                 scrollParent=None) -> None:
        """padding仅为每一项上下的padding,左右已经固定
        """
        super().__init__()
        self._scrollParent = scrollParent
        self._sp_lock = False
        if scrollParent:
            self._sp_lock = True
        if parent:
            self.setParent(parent)

        self.setFocusPolicy(Qt.ClickFocus)
        # 启用自定义多选
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # 拖放设定
        if enableDropDrag is True:
            self.setAcceptDrops(True)
            self.setDragEnabled(True)
            self.setDragDropMode(QAbstractItemView.InternalMove)
            # self.setDefaultDropAction(Qt.CopyAction)
        # 双击编辑设定
        if enableEdit is True:
            self.editingItem = self.currentItem()
            self.closeFlag = True
            self.doubleClicked.connect(self.item_double_clicked)

        _styleFormat = style.format(_color=color,
                                    _color_disabled=color_disabled,
                                    _border_color=border_color,
                                    _border_color_disabled=border_color_disabled,
                                    _border_color_hover=border_color_hover,
                                    _background_color=bg_color,
                                    _background_color_disabled=bg_color_disabled,
                                    _background_color_hover=bg_color_hover,
                                    _background_color_selected=bg_color_selected,
                                    _background_color_active=bg_color_active,
                                    _color_selected=color_selected,
                                    _radius=radius,
                                    _padding=padding,
                                    _font_size=fontSize,
                                    _font_family=fontFamily)
        self.setStyleSheet(_styleFormat)

    # def dropEvent(self, event: QDropEvent) -> None:
    #     source_widget: QListWidget = event.source()
    #     items = source_widget.selectedItems()
    #     for item in items:
    #         source_widget.takeItem(source_widget.indexFromItem(item).row())
    #         self.addItem(item)

    # 设置滚动传递
    def wheelEvent(self, event: QWheelEvent) -> None:
        if self.hasFocus() and self.isEnabled():
            return super().wheelEvent(event)
        else:
            if self._scrollParent:
                self._scrollParent.setFocus()
                return self._scrollParent.wheelEvent(event)

    # 当前选中行发生改变时关闭编辑框
    def currentChanged(self, current: QModelIndex, previous: QModelIndex) -> None:
        self._closeEdit()
        return super().currentChanged(current, previous)

    # 按下回车键关闭编辑框
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter:
            self._closeEdit()
        return super().keyPressEvent(event)

    def item_double_clicked(self, modelIndex: QModelIndex) -> None:
        """双击时打开编辑器"""
        self._closeEdit()
        item = self.item(modelIndex.row())
        self.editingItem = item
        self.openPersistentEditor(item)
        self.editItem(item)

    def _closeEdit(self, *_) -> None:
        if self.editingItem and self.isPersistentEditorOpen(self.editingItem):
            self.closePersistentEditor(self.editingItem)

    def c_setScrollParent(self, sparent) -> None:
        """设置鼠标滚轮事件传递,若已通过构造函数设置,该函数无效
        Args:
            sparent (QObject): 目标组件
        """
        if self._sp_lock is False:
            self._scrollParent = sparent

    def c_addRows(self, data: list) -> None:
        """添加数据"""
        for item in data:
            self.addItem(QListWidgetItem(item))

    def c_getData(self) -> list:
        """获取列表数据"""
        returnList = []
        for i in range(0, self.count()):
            returnList.append(self.item(i).text())
        return returnList

    def c_deleteSelectdRows(self) -> None:
        """删除所有选中行"""
        while self.selectedIndexes().__len__() > 0:
            self.takeItem(self.selectedIndexes()[0].row())
