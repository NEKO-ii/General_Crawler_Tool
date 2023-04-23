# 导航栏UI
# ///////////////////////////////////////////////////////////////
from typing import Any

from core.sys import Themes
from ui.func.iconsetter import IconSetter
from ui.preload.imp_qt import (QCursor, QFrame, QHBoxLayout, QLabel, QSize,
                               QSvgWidget, Qt, QVBoxLayout, QWidget, Signal)

from .sep_line import SepLine
from .title_button import TitleButton


class TitleBar_UI(QWidget):
    """导航栏UI类
    """
    clicked = Signal(object)
    released = Signal(object)

    # 属性
    # ///////////////////////////////////////////////////////////////
    _is_maximized: bool
    _old_size: QSize

    _container: Any  # 存放导航栏的组件
    _central_widget: Any  # 窗口中心组件
    _hide_title_bar: bool  # 是否隐藏系统窗口标题栏
    _radius: int
    _logo_name: str
    _logo_width: int
    _title_size: int
    _font_family: str
    _themes: Themes

    title_bar_layout: QVBoxLayout
    background: QFrame
    bg_layout: QHBoxLayout

    logo: QLabel
    logo_layout: QVBoxLayout
    logo_svg: QSvgWidget

    title: QLabel

    buttons_layout: QHBoxLayout
    btn_minimize: TitleButton
    btn_maximize: TitleButton
    btn_close: TitleButton

    # ///////////////////////////////////////////////////////////////

    def __init__(self, container, central_widget, hide_title_bar, themes) -> None:
        super().__init__()
        self._is_maximized = False
        self._old_size = QSize()

        self._container = container
        self._central_widget = central_widget
        self._hide_title_bar = hide_title_bar
        self._radius = 8
        self._logo_name = "logo_top_100x22.svg"
        self._logo_width = 100
        self._title_size = 10
        self._font_family = "Segoe UI"
        self._themes = themes

        # 自动运行
        self.setup()
        self.btn_connect()

    def setup(self) -> None:
        self.title_bar_layout = QVBoxLayout(self)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        self.background = QFrame()
        self.background.setStyleSheet(F'background-color: {self._themes.color["bg_2"]}; border-radius: {self._radius}px;')
        self.bg_layout = QHBoxLayout(self.background)
        self.bg_layout.setContentsMargins(10, 0, 5, 0)
        self.bg_layout.setSpacing(0)

        self.spl_1 = SepLine(self._themes.color["bg_3"])
        self.spl_2 = SepLine(self._themes.color["bg_3"])
        self.spl_3 = SepLine(self._themes.color["bg_3"])

        self.logo = QLabel()
        self.logo.setMinimumWidth(self._logo_width)
        self.logo.setMaximumWidth(self._logo_width)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_svg = QSvgWidget()
        self.logo_svg.load(IconSetter.setSvgIcon(self._logo_name))
        self.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        self.title = QLabel()
        self.title.setAlignment(Qt.AlignVCenter)
        self.title.setStyleSheet(f'font: {self._title_size}pt "{self._font_family}"')

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_layout.setSpacing(3)

        self.btn_minimize = TitleButton(self._container, self._central_widget, "window_minimize", "最小化", self._themes, IconSetter.setSvgIcon("icon_window_minimize.svg"))
        self.btn_maximize = TitleButton(self._container, self._central_widget, "window_maximize", "最大化", self._themes, IconSetter.setSvgIcon("icon_window_maximize.svg"))
        self.btn_close = TitleButton(self._container, self._central_widget, "window_close", "关闭", self._themes, IconSetter.setSvgIcon("icon_window_close.svg"))

        if self._hide_title_bar:
            self.logo.mouseMoveEvent = self.moveWindow
            self.spl_1.mouseMoveEvent = self.moveWindow
            self.title.mouseMoveEvent = self.moveWindow
            self.spl_2.mouseMoveEvent = self.moveWindow
            self.spl_3.mouseMoveEvent = self.moveWindow

            self.logo.mouseDoubleClickEvent = self.maximize_restore
            self.spl_1.mouseDoubleClickEvent = self.maximize_restore
            self.title.mouseDoubleClickEvent = self.maximize_restore
            self.spl_2.mouseDoubleClickEvent = self.maximize_restore

        self.bg_layout.addWidget(self.logo)
        self.bg_layout.addWidget(self.spl_1)
        self.bg_layout.addWidget(self.title)
        self.bg_layout.addWidget(self.spl_2)
        self.bg_layout.addLayout(self.buttons_layout)
        if self._hide_title_bar:
            self.bg_layout.addWidget(self.btn_minimize)
            self.bg_layout.addWidget(self.btn_maximize)
            self.bg_layout.addWidget(self.btn_close)

        self.title_bar_layout.addWidget(self.background)

    def btn_connect(self) -> None:
        self.btn_minimize.released.connect(lambda: self._container.showMinimized())
        self.btn_maximize.released.connect(lambda: self.maximize_restore())
        self.btn_close.released.connect(lambda: self._container.close())

    # API
    # ///////////////////////////////////////////////////////////////
    def add_menus(self, menus):
        if menus is not None and len(menus) > 0:
            for menu in menus:
                _btn_icon = IconSetter.setSvgIcon(menu['btn_icon'])
                _btn_id = menu['btn_id']
                _btn_tooltip = menu['btn_tooltip']
                _is_active = menu['is_active']

                self.btn = TitleButton(self._container, self._central_widget, btn_id=_btn_id, tooltip_text=_btn_tooltip, themes=self._themes, icon_path=_btn_icon, is_active=_is_active)
                self.btn.clicked.connect(self.btn_clicked)
                self.btn.released.connect(self.btn_released)

                self.buttons_layout.addWidget(self.btn)

            if self._hide_title_bar:
                self.buttons_layout.addWidget(self.spl_3)

    def set_title(self, title):
        self.title.setText(title)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self) -> None:
        self.clicked.emit(self.btn)

    def btn_released(self) -> None:
        self.released.emit(self.btn)

    def change_ui(self) -> None:
        if self._is_maximized:
            self._container.central_widget_layout.setContentsMargins(0, 0, 0, 0)
            self._container.window.set_stylesheet(border_radius=0, border_size=0)
            self.btn_maximize.set_icon(IconSetter.set_svg_icon("icon_window_restore.svg"))
            self.btn_maximize.tooltip.setText("Restore")
        else:
            self._container.central_widget_layout.setContentsMargins(10, 10, 10, 10)
            self._container.window.set_stylesheet(border_radius=10, border_size=2)
            self.btn_maximize.set_icon(IconSetter.set_svg_icon("icon_window_maximize.svg"))
            self.btn_maximize.tooltip.setText("Maximize")

    def maximize_restore(self, e=None) -> None:
        if self._container.isMaximized():
            self._is_maximized = False
            self._container.showNormal()
            self.change_ui()
        else:
            self._is_maximized = True
            self._old_size = QSize(self._container.width(), self._container.height())
            self._container.showMaximized()
            self.change_ui()

    # 方法重写
    # ///////////////////////////////////////////////////////////////
    def moveWindow(self, event):
        if self._container.isMaximized():
            self.maximize_restore()
            curso_x = self._container.pos().x()
            curso_y = event.globalPos().y() - QCursor.pos().y()
            self._container.move(curso_x, curso_y)
        if event.buttons() == Qt.LeftButton:
            self._container.move(self._container.pos() + event.globalPos() - self._container.dragPos)
            self._container.dragPos = event.globalPos()
            event.accept()
