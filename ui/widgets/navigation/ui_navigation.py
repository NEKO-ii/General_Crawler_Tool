# 左侧导航栏界面UI
# ///////////////////////////////////////////////////////////////
from typing import Any

from core.sys import Themes
from ui.preload.imp_qt import (QEasingCurve, QFrame, QPropertyAnimation, QPushButton, Qt, QVBoxLayout, QWidget, Signal)

from .nav_button import NavButton
from .sep_line import SepLine


class Navigation_UI(QWidget):
    """导航栏界面UI类
    """
    # 信号
    clicked = Signal(object)
    released = Signal(object)

    # 属性
    # ///////////////////////////////////////////////////////////////
    _container: Any  # 存放导航栏的组件
    _centralWidget: Any  # 窗口中心组件
    _themes: Themes

    _radius: int
    _iconShow_name: str
    _iconHide_name: str
    _toggleButton_text: str
    _toggleButton_tooltip: str

    layout: QVBoxLayout
    background: QFrame
    topFrame: QFrame
    bottomFrame: QFrame
    bgLayout: QVBoxLayout
    topLayout: QVBoxLayout
    bottomLayout: QVBoxLayout

    toggleButton: NavButton

    # ///////////////////////////////////////////////////////////////

    def __init__(self, container, centralWidget, themes) -> None:
        super().__init__()

        self._container = container
        self._centralWidget = centralWidget
        self._themes = themes
        self._radius = 8
        self._iconShow_name = "icon_nav_show.svg"
        self._iconHide_name = "icon_nav_hide.svg"
        self._toggleButton_id = "btn_nav_toogle"
        self._toggleButton_text = "Hide Navigation"
        self._toggleButton_tooltip = "Show Menu"

        self.setup()
        self._buttonConnect()

    def setup(self) -> None:
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.background = QFrame()
        self.bgLayout = QVBoxLayout(self.background)
        self.bgLayout.setContentsMargins(0, 0, 0, 0)

        self.topFrame = QFrame()
        self.topLayout = QVBoxLayout(self.topFrame)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setSpacing(1)

        self.bottomFrame = QFrame()
        self.bottomLayout = QVBoxLayout(self.bottomFrame)
        self.bottomLayout.setContentsMargins(0, 0, 0, 8)
        self.bottomLayout.setSpacing(1)

        self.bgLayout.addWidget(self.topFrame, 0, Qt.AlignTop)
        self.bgLayout.addWidget(self.bottomFrame, 0, Qt.AlignBottom)

        self.layout.addWidget(self.background)

        self.background.setStyleSheet(F"""
            background: {self._themes.color["dark_1"]};
            border-radius: {self._radius};
        """)

        # 装载按钮

        self.toggleButton = NavButton(self._centralWidget, buttonId=self._toggleButton_id, buttonText=self._toggleButton_text, tooltipText=self._toggleButton_tooltip, themes=self._themes, iconName=self._iconShow_name)
        self.sepline_top = SepLine(self._themes.color["dark_4"])
        self.sepline_bottom = SepLine(self._themes.color["dark_4"])

        self.topLayout.addWidget(self.toggleButton)
        self.topLayout.addWidget(self.sepline_top)
        self.bottomLayout.addWidget(self.sepline_bottom)
        self.sepline_bottom.hide()

    def _buttonConnect(self) -> None:
        self.toggleButton.clicked.connect(self._toggleAnimation)

    # API
    # ///////////////////////////////////////////////////////////////
    def c_addMenus(self, menus):
        if menus is not None:
            for menu in menus:
                _btn_icon = menu['btn_icon']
                _btn_id = menu['btn_id']
                _btn_text = menu['btn_text']
                _btn_tooltip = menu['btn_tooltip']
                _show_top = menu['show_top']
                _is_active = menu['is_active']

                self.btn = NavButton(container=self._centralWidget, buttonText=_btn_text, buttonId=_btn_id, tooltipText=_btn_tooltip, themes=self._themes, iconName=_btn_icon, isActive=_is_active)
                self.btn.clicked.connect(self.btn_clicked)
                self.btn.released.connect(self.btn_released)

                if _show_top:
                    self.topLayout.addWidget(self.btn)
                else:
                    self.sepline_bottom.show()
                    self.bottomLayout.addWidget(self.btn)

    def c_selectOnlyOne(self, widget: str):
        btn: NavButton
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget: btn.c_setActive(True)
            else: btn.c_setActive(False)

    def c_deselectAll(self):
        btn: NavButton
        for btn in self.findChildren(QPushButton):
            btn.c_setActive(False)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def _toggleAnimation(self):
        self.animation = QPropertyAnimation(self._container, b"minimumWidth")
        self.animation.stop()
        if self.width() == self._themes.navigation["minimum_width"]:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._themes.navigation["maximum_width"])
            self.toggleButton.c_setExpand(True)
            self.toggleButton.c_setIcon(self._iconHide_name)
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._themes.navigation["minimum_width"])
            self.toggleButton.c_setExpand(False)
            self.toggleButton.c_setIcon(self._iconShow_name)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(self._themes.time_animation)
        self.animation.start()

    def btn_clicked(self):
        self.clicked.emit(self.btn)

    def btn_released(self):
        self.released.emit(self.btn)
