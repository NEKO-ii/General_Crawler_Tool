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
    _isMaximized: bool
    _oldSize: QSize

    _container: Any  # 存放导航栏的组件
    _centralWidget: Any  # 窗口中心组件
    _hideTitleBar: bool  # 是否隐藏系统窗口标题栏
    _radius: int
    _logoName: str
    _logoWidth: int
    _titleSize: int
    _fontFamily: str
    _themes: Themes

    titleBarLayout: QVBoxLayout
    background: QFrame
    bgLayout: QHBoxLayout

    logo: QLabel
    logoLayout: QVBoxLayout
    logoSvg: QSvgWidget

    title: QLabel

    buttonsLayout: QHBoxLayout
    btn_minimize: TitleButton
    btn_maximize: TitleButton
    btn_close: TitleButton

    # ///////////////////////////////////////////////////////////////

    def __init__(self, container, central_widget, hide_title_bar, themes) -> None:
        super().__init__()
        self._isMaximized = False
        self._oldSize = QSize()

        self._container = container
        self._centralWidget = central_widget
        self._hideTitleBar = hide_title_bar
        self._radius = 8
        self._logoName = "logo_top_100x22.svg"
        self._logoWidth = 100
        self._titleSize = 10
        self._fontFamily = "Segoe UI"
        self._themes = themes

        # 自动运行
        self.setup()
        self.btn_connect()

    def setup(self) -> None:
        self.titleBarLayout = QVBoxLayout(self)
        self.titleBarLayout.setContentsMargins(0, 0, 0, 0)

        self.background = QFrame()
        self.background.setStyleSheet(F'background-color: {self._themes.color["bg_2"]}; border-radius: {self._radius}px;')
        self.bgLayout = QHBoxLayout(self.background)
        self.bgLayout.setContentsMargins(10, 0, 5, 0)
        self.bgLayout.setSpacing(0)

        self.spl_1 = SepLine(self._themes.color["bg_3"])
        self.spl_2 = SepLine(self._themes.color["bg_3"])
        self.spl_3 = SepLine(self._themes.color["bg_3"])

        self.logo = QLabel()
        self.logo.setMinimumWidth(self._logoWidth)
        self.logo.setMaximumWidth(self._logoWidth)
        self.logoLayout = QVBoxLayout(self.logo)
        self.logoLayout.setContentsMargins(0, 0, 0, 0)
        self.logoSvg = QSvgWidget()
        self.logoSvg.load(IconSetter.setSvgIcon(self._logoName))
        self.logoLayout.addWidget(self.logoSvg, Qt.AlignCenter, Qt.AlignCenter)

        self.title = QLabel()
        self.title.setAlignment(Qt.AlignVCenter)
        self.title.setStyleSheet(f'font: {self._titleSize}pt "{self._fontFamily}"')

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonsLayout.setSpacing(3)

        self.btn_minimize = TitleButton(self._container, self._centralWidget, "window_minimize", "最小化", self._themes, IconSetter.setSvgIcon("icon_window_minimize.svg"))
        self.btn_maximize = TitleButton(self._container, self._centralWidget, "window_maximize", "最大化", self._themes, IconSetter.setSvgIcon("icon_window_maximize.svg"))
        self.btn_close = TitleButton(self._container, self._centralWidget, "window_close", "关闭", self._themes, IconSetter.setSvgIcon("icon_window_close.svg"))

        if self._hideTitleBar:
            self.logo.mouseMoveEvent = self.moveWindow
            self.spl_1.mouseMoveEvent = self.moveWindow
            self.title.mouseMoveEvent = self.moveWindow
            self.spl_2.mouseMoveEvent = self.moveWindow
            self.spl_3.mouseMoveEvent = self.moveWindow

            self.logo.mouseDoubleClickEvent = self.maximize_restore
            self.spl_1.mouseDoubleClickEvent = self.maximize_restore
            self.title.mouseDoubleClickEvent = self.maximize_restore
            self.spl_2.mouseDoubleClickEvent = self.maximize_restore

        self.bgLayout.addWidget(self.logo)
        self.bgLayout.addWidget(self.spl_1)
        self.bgLayout.addWidget(self.title)
        self.bgLayout.addWidget(self.spl_2)
        self.bgLayout.addLayout(self.buttonsLayout)
        if self._hideTitleBar:
            self.bgLayout.addWidget(self.btn_minimize)
            self.bgLayout.addWidget(self.btn_maximize)
            self.bgLayout.addWidget(self.btn_close)

        self.titleBarLayout.addWidget(self.background)

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

                self.btn = TitleButton(self._container, self._centralWidget, buttonId=_btn_id, tooltipText=_btn_tooltip, themes=self._themes, iconPath=_btn_icon, isActive=_is_active)
                self.btn.clicked.connect(self.btn_clicked)
                self.btn.released.connect(self.btn_released)

                self.buttonsLayout.addWidget(self.btn)

            if self._hideTitleBar:
                self.buttonsLayout.addWidget(self.spl_3)

    def set_title(self, title):
        self.title.setText(title)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self) -> None:
        self.clicked.emit(self.btn)

    def btn_released(self) -> None:
        self.released.emit(self.btn)

    def change_ui(self) -> None:
        if self._isMaximized:
            self._container.centralWidgetLayout.setContentsMargins(0, 0, 0, 0)
            self._container.window.c_setStylesheet(borderRadius=0, borderSize=0)
            self.btn_maximize._setIcon(IconSetter.setSvgIcon("icon_window_restore.svg"))
            self.btn_maximize.tooltip.setText("恢复")
        else:
            self._container.centralWidgetLayout.setContentsMargins(10, 10, 10, 10)
            self._container.window.c_setStylesheet(borderRadius=10, borderSize=2)
            self.btn_maximize._setIcon(IconSetter.setSvgIcon("icon_window_maximize.svg"))
            self.btn_maximize.tooltip.setText("最大化")

    def maximize_restore(self, e=None) -> None:
        if self._container.isMaximized():
            self._isMaximized = False
            self._container.showNormal()
            self.change_ui()
        else:
            self._isMaximized = True
            self._oldSize = QSize(self._container.width(), self._container.height())
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
