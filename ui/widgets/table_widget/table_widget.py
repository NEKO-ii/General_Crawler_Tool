from ui.preload.imp_qt import QTableWidget, Qt, QAbstractItemView, QWheelEvent, QTableWidgetItem, QHeaderView, Signal, QColor


class TableWidget(QTableWidget):
    color: dict = {"default": "#aaaabb", "info": "rgb(17, 169, 225)", "warning": "#f0f020", "error": "#ff4040", "success": "#20cc5f"}
    style: str = '''
    QWidget {{
        color: {_color};
        background-color: {_background_color};
    }}
    QWidget:disabled {{
        color: {_color_disabled};
        background-color: {_background_color_disabled};
    }}

    QTableWidget {{
        outline: none;
        border: none;
        border-radius: {_radius}px;
        gridline-color: {_border_color};
        padding: 5px;
        font: {_font_size}pt {_font_family};
        background-color: {_background_color};
    }}
    QTableWidget:enabled {{
        border-color: {_border_color};
        color: {_color};
        background-color: {_background_color};
    }}
    QTableWidget:disabled {{
        border-color: {_border_color_disabled};
        color: {_color_disabled};
        background-color: {_background_color_disabled};
    }}
    QTableWidget::item {{
        border: none;
        margin: 0px;
        padding: 1px 5px 1px 5px;
    }}
    QTableWidget::item:hover {{
        background-color: {_background_color_hover};
        border: 1px solid {_border_color_hover};
    }}
    QTableWidget::item:selected {{
        color: {_color_selected};
        background-color: {_background_color_selection};
    }}
    QTableWidget::item::selected:active {{
        background-color: {_background_color_active};
    }}

    QTableWidget::horizontalHeader {{
        background-color: {_background_color};
    }}
    QTableWidget::verticalHeader {{
        background-color: {_background_color};
    }}

    QHeaderView::section {{
        background-color: {_background_color};
        border: none;
        border-bottom: 1px solid {_border_color};
        border-right: 1px solid {_border_color};
        min-width: 20px;
    }}
    QHeaderView::section:horizontal {{
        border: none;
        border-bottom: 1px solid {_border_color};
        border-right: 1px solid {_border_color};
        background-color: {_header_horizontal_color};
        padding-top: {_header_padding}px;
        padding-bottom: {_header_padding}px;
    }}
    QHeaderView::section:horizontal:disabled {{
        background-color: {_header_horizontal_color_disabled};
    }}
    QHeaderView::section:vertical {{
        color: {_color_active};
        font: {_font_size}pt {_font_family};
        border: none;
        border-bottom: 1px solid {_border_color};
        background-color: {_header_vertical_color};
        padding-left: 5px;
        padding-right: 5px;
    }}
    QHeaderView::section:vertical:disabled {{
        background-color: {_header_vertical_color_disabled};
    }}
    QTableWidget QTableCornerButton::section {{
        border: none;
        border-bottom: 1px solid {_border_color};
        background-color: {_header_horizontal_color};
        border-top-left-radius: {_radius}px;
    }}
    QTableWidget QTableCornerButton::section:disabled {{
        background-color: {_header_horizontal_color_disabled};
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

    sig_data_changed = Signal(object)
    sig_open = Signal(object)
    sig_flush = Signal(object)

    flag_opened: bool = False
    flag_init_complete: bool = False
    _flag_data_change_sig_enable: bool = True

    no_edit_cols: list = []
    no_change_sig_count = 0

    def __init__(self,
                 parent,
                 radius=8,
                 color="#aaaabb",
                 color_disabled="#4f5b6e",
                 color_selected="#f5f6f9",
                 color_active="#6c99f4",
                 bg_color="#21252d",
                 bg_color_disabled="#272c36",
                 bg_color_hover="#2c313c",
                 bg_color_selection="#204070",
                 bg_color_active="#205090",
                 border_color="#3c4454",
                 border_color_disabled="#272c36",
                 border_color_hover="#6c99f4",
                 header_horizontal_color="#1b1e23",
                 header_horizontal_color_disabled="#21252d",
                 header_vertical_color="#3c4454",
                 header_vertical_color_disabled="#2c313c",
                 scroll_bg_color_handle="#568af2",
                 scroll_bg_color_addline="#272c36",
                 scroll_bg_color_subline="#272c36",
                 header_padding=1,
                 default_row_height=20,
                 font_size=9,
                 font_family="JetBrains Mono",
                 height=140,
                 extend_height=False,
                 auto_col_width=False,
                 fixed_col_width=False,
                 show_h_header=True,
                 show_v_header=True,
                 scroll_parent=None):
        """初始化表格控件

        Args:
            parent (_type_): 父组件
            height (int, optional): 设置固定高度(extend_height为True时将被忽略). Defaults to 140.
            extend_height (bool, optional): 高度自动填充. Defaults to False.
            auto_col_width (bool, optional): 自动列宽(将表格宽度平分给每一列且不可改变). Defaults to False.
            fixed_col_width (bool, optional): 固定列宽(设置自动列宽时将被忽略). Defaults to False.
            show_h_header (bool, optional): 显示水平标题. Defaults to True.
            show_v_header (bool, optional): 显示垂直行号. Defaults to True.
            scroll_parent (_type_, optional): 滚动传递组件. Defaults to None.
        """
        super().__init__(parent)
        self._auto_col_width = auto_col_width
        self._default_row_height = default_row_height
        self._scroll_parent = scroll_parent
        self._sp_lock = False
        if scroll_parent:
            self._sp_lock = True
        if auto_col_width:
            self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        elif fixed_col_width:
            self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        if extend_height is False:
            if height: self.setFixedHeight(height)

        self.setFocusPolicy(Qt.ClickFocus)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().setDefaultSectionSize(default_row_height)
        self.horizontalHeader().setVisible(show_h_header)
        self.verticalHeader().setVisible(show_v_header)

        # 设置样式表
        style_format = self.style.format(_radius=radius,
                                         _header_padding=header_padding,
                                         _color=color,
                                         _color_disabled=color_disabled,
                                         _color_selected=color_selected,
                                         _color_active=color_active,
                                         _background_color=bg_color,
                                         _background_color_disabled=bg_color_disabled,
                                         _header_horizontal_color=header_horizontal_color,
                                         _header_horizontal_color_disabled=header_horizontal_color_disabled,
                                         _header_vertical_color=header_vertical_color,
                                         _header_vertical_color_disabled=header_vertical_color_disabled,
                                         _border_color=border_color,
                                         _border_color_disabled=border_color_disabled,
                                         _border_color_hover=border_color_hover,
                                         _background_color_hover=bg_color_hover,
                                         _background_color_selection=bg_color_selection,
                                         _background_color_active=bg_color_active,
                                         _background_color_handle=scroll_bg_color_handle,
                                         _background_color_addline=scroll_bg_color_addline,
                                         _background_color_subline=scroll_bg_color_subline,
                                         _font_size=font_size,
                                         _font_family=font_family)
        self.setStyleSheet(style_format)

    # 当初始化完成后表格数据变化时发出自定义信号: sig_data_changed
    def dataChanged(self, topLeft, bottomRight, roles) -> None:
        if self.flag_init_complete and self._flag_data_change_sig_enable:
            self.sig_data_changed.emit(self.get_current_index())
        return super().dataChanged(topLeft, bottomRight, roles)

    # 当初次打开此表格时发出自定义信号: sig_open, 不是初次打开的时候发出自定义信号: sig_flush
    def showEvent(self, event) -> None:
        if self.flag_opened:
            self.sig_flush.emit(None)
        else:
            self.sig_open.emit(None)
            self.flag_opened = True
        return super().showEvent(event)

    # 滚轮事件发生时,若自身禁用或未拥有焦点则将滚轮事件传递给设置的滚轮事件接收组件
    def wheelEvent(self, event: QWheelEvent) -> None:
        if self.hasFocus() and self.isEnabled():
            return super().wheelEvent(event)
        else:
            if self._scroll_parent:
                self._scroll_parent.setFocus()
                return self._scroll_parent.wheelEvent(event)

    def set_scroll_parent(self, sparent) -> None:
        """设置鼠标滚轮事件传递,若已通过构造函数设置,该函数无效
        Args:
            sparent (QObject): 目标组件
        """
        if self._sp_lock is False:
            self._scroll_parent = sparent

    def set_header(self, header_names: list, stretch_cols: list = []) -> None:
        """设置横向标题栏

        Args:
            header_names (list): 列标题名称列表
            stretch_cols (list, optional): 可随窗口大小改变宽度的列(起始为0),默认为最后一列,当设置自动列宽时该设置将被忽略. Defaults to [].
        """
        if self.columnCount() == 0:
            self.setColumnCount(header_names.__len__())
        col_index: int = 0
        for name in header_names:
            column = QTableWidgetItem(name)
            column.setTextAlignment(Qt.AlignCenter)
            self.setHorizontalHeaderItem(col_index, column)
            col_index += 1
        if self._auto_col_width is False:
            if stretch_cols == []:
                self.horizontalHeader().setSectionResizeMode(col_index - 1, QHeaderView.Stretch)
            else:
                for item in stretch_cols:
                    self.horizontalHeader().setSectionResizeMode(item, QHeaderView.Stretch)
        self.horizontalHeaderItem(0).setToolTip("这是工具提示文字")

    def set_header_tooltip(self, tooltips: list) -> None:
        """设置表头的悬停提示文字,按输入列表从左到右依次设置,多则忽略,少则跳过

        Args:
            tooltips (list): 提示文字列表
        """
        col_count = self.columnCount()
        list_len = tooltips.__len__()
        for i in range(0, col_count):
            if i == list_len: break
            self.horizontalHeaderItem(i).setToolTip(tooltips[i])

    def add_row(self, data: list = []) -> None:
        """添加行,输入数组按由左到右顺序依次添加,多余忽略,不足自动添加空QTableWidgetItem

        Args:
            data (list): 一维数组,数据仅限字符串类型
            no_edit_cols (list): 不可编辑的列
        """
        row_index = self.rowCount()
        self.insertRow(row_index)
        col_count = self.columnCount()
        list_len = data.__len__()
        self._flag_data_change_sig_enable = False
        for i in range(0, col_count):
            if i == col_count - 1:
                self._flag_data_change_sig_enable = True
                self.setCurrentCell(row_index, i)
            if i < list_len:
                item = data[i]
                if item is None: self.setItem(row_index, i, QTableWidgetItem())
                else:
                    if type(item) == str: self.setItem(row_index, i, QTableWidgetItem(item))
                    else: self.setCellWidget(row_index, i, item)
            else: self.setItem(row_index, i, QTableWidgetItem())
            if i in self.no_edit_cols: self.item(row_index, i).setFlags(self.item(row_index, i).flags() & (~Qt.ItemIsEditable))
        self.setCurrentCell(-1, -1)

    def add_rows(self, data: list) -> None:
        """添加多行数据,每行输入数据数组按由左到右顺序依次添加,多余忽略,不足留空

        Args:
            data (list): 二维数组,数据仅限字符串类型
            no_edit_cols (list): 不可编辑的列
        """
        for item in data:
            self.add_row(item)

    def get_data(self, widget_cols: list = [], only_col: list = [], only_selected_rows: bool = False) -> list:
        """获取表格数据列表(二维),最外层固定位列表,若表格为空则不会添加内层列表,只返回一个空列表

        Args:
            widget_cols (list, optional): 标记表格中存在组件的列. Defaults to [].
            only_col (list, optional): 设置输出列,若设置,未在列表中的列的数据将忽略. Defaults to [].
            only_selected_rows (bool, optional): 是否只输出选中行的数据. Defaults to [].

        Returns:
            list: 返回数据列表(二维)
        """
        col_count = self.columnCount()
        row_count = self.rowCount()
        return_data = []
        for rindex in range(0, row_count):
            row = []
            for cindex in range(0, col_count):
                if (only_col != []) and (cindex not in only_col): continue
                if only_selected_rows and (self.item(rindex, cindex).isSelected() is False): continue
                if cindex in widget_cols:
                    item_data = self.cellWidget(rindex, cindex)
                else:
                    item = self.item(rindex, cindex)
                    if item: item_data = item.text()
                    else: item_data = ""
                row.append(item_data)
            if row != []: return_data.append(row)
        return return_data

    def flush(self) -> None:
        """通过设置不可见再设为可见以触发sig_flush信号"""
        self.hide()
        self.show()

    def set_col_width(self, width: list) -> None:
        """设置每列的列宽,根据输入数组从左到右设置列宽,输入数组项数不足以及过多时多余部分忽略,设置了自动列宽时该设置将被忽略

        Args:
            width (list): 列宽数据数组
        """
        if self._auto_col_width is False:
            col_count = self.columnCount()
            list_len = width.__len__()
            for i in range(0, col_count):
                if i == list_len: break
                if width[i] is not None: self.setColumnWidth(i, width[i])

    def delete_selectd_rows(self) -> None:
        """删除所有选中行,注意:当flag_init_complete=True时会触发sig_data_changed信号"""
        while self.selectedItems().__len__() > 0:
            self.removeRow(self.selectedItems()[0].row())
        if self.flag_init_complete and self._flag_data_change_sig_enable:
            self.sig_data_changed.emit(self.get_current_index())

    def clear(self) -> None:
        """清空表格,注意:当flag_init_complete=True时会触发sig_data_changed信号"""
        while self.rowCount() > 0:
            self.removeRow(0)
        if self.flag_init_complete and self._flag_data_change_sig_enable:
            self.sig_data_changed.emit(self.get_current_index())

    def set_cell_color(self, rindex, cindex, color_type: str = "default"):
        """设置单元格文字颜色,只适用于文字单元格,若单元格内添加了组件则可能报错,不会触发sig_data_changed信号

        Args:
            rindex (int): 行坐标
            cindex (int): 列坐标
            color_type (str, optional): 颜色类型[default:默认灰白文字,info:蓝色,warning:黄色,error:红色,success:绿色]. Defaults to "default".
        """
        self._flag_data_change_sig_enable = False
        self.item(rindex, cindex).setForeground(QColor(self.color[color_type.lower()]))
        self._flag_data_change_sig_enable = True

    def set_change_sig_disabled_count(self, num: int) -> int:
        """增加接下来发生表格数据变化时,不发出sig_data_changed信号的次数,并返回当前剩余次数

        Args:
            num (int): 增加次数

        Returns:
            int: 返回当前剩余次数
        """
        if (type(num) == int) and (num > 0): self.no_change_sig_count += num
        return self.no_change_sig_count

    def get_current_index(self) -> list:
        """获取当前活动单元坐标"""
        if self.selectedItems().__len__() > 0:
            crow = self.currentRow()
            ccol = self.currentItem().column() if self.currentItem() else None
            ret = [None if crow == -1 else crow, None if ccol == -1 else ccol]
        else:
            ret = [None, None]
        # print(ret)
        return ret
