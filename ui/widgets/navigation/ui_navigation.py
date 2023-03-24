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
    _central_widget: Any  # 窗口中心组件
    _themes: Themes

    _radius: int
    _icon_show_name: str
    _icon_hide_name: str
    _toggle_button_text: str
    _toggle_button_tooltip: str

    layout: QVBoxLayout
    background: QFrame
    top_frame: QFrame
    bottom_frame: QFrame
    bg_layout: QVBoxLayout
    top_layout: QVBoxLayout
    bottom_layout: QVBoxLayout

    toggle_button: NavButton

    # ///////////////////////////////////////////////////////////////

    def __init__(self, container, central_widget, themes) -> None:
        super().__init__()

        self._container = container
        self._central_widget = central_widget
        self._themes = themes
        self._radius = 8
        self._icon_show_name = "icon_nav_show.svg"
        self._icon_hide_name = "icon_nav_hide.svg"
        self._toggle_btn_id = "btn_nav_toogle"
        self._toggle_button_text = "Hide Navigation"
        self._toggle_button_tooltip = "Show Menu"

        self.setup()
        self.button_connect()

    def setup(self) -> None:
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.background = QFrame()
        self.bg_layout = QVBoxLayout(self.background)
        self.bg_layout.setContentsMargins(0, 0, 0, 0)

        self.top_frame = QFrame()
        self.top_layout = QVBoxLayout(self.top_frame)
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout.setSpacing(1)

        self.bottom_frame = QFrame()
        self.bottom_layout = QVBoxLayout(self.bottom_frame)
        self.bottom_layout.setContentsMargins(0, 0, 0, 8)
        self.bottom_layout.setSpacing(1)

        self.bg_layout.addWidget(self.top_frame, 0, Qt.AlignTop)
        self.bg_layout.addWidget(self.bottom_frame, 0, Qt.AlignBottom)

        self.layout.addWidget(self.background)

        self.background.setStyleSheet(F"""
            background: {self._themes.color["dark_1"]};
            border-radius: {self._radius};
        """)

        # 装载按钮

        self.toggle_button = NavButton(self._central_widget, button_id=self._toggle_btn_id, button_text=self._toggle_button_text, tooltip_text=self._toggle_button_tooltip, themes=self._themes, icon_name=self._icon_show_name)
        self.sepline_top = SepLine(self._themes.color["dark_4"])
        self.sepline_bottom = SepLine(self._themes.color["dark_4"])

        self.top_layout.addWidget(self.toggle_button)
        self.top_layout.addWidget(self.sepline_top)
        self.bottom_layout.addWidget(self.sepline_bottom)
        self.sepline_bottom.hide()

    def button_connect(self) -> None:
        self.toggle_button.clicked.connect(self.toggle_animation)

    # API
    # ///////////////////////////////////////////////////////////////
    def add_menus(self, menus):
        if menus is not None:
            for menu in menus:
                _btn_icon = menu['btn_icon']
                _btn_id = menu['btn_id']
                _btn_text = menu['btn_text']
                _btn_tooltip = menu['btn_tooltip']
                _show_top = menu['show_top']
                _is_active = menu['is_active']

                self.btn = NavButton(container=self._central_widget, button_text=_btn_text, button_id=_btn_id, tooltip_text=_btn_tooltip, themes=self._themes, icon_name=_btn_icon, is_active=_is_active)
                self.btn.clicked.connect(self.btn_clicked)
                self.btn.released.connect(self.btn_released)

                if _show_top:
                    self.top_layout.addWidget(self.btn)
                else:
                    self.sepline_bottom.show()
                    self.bottom_layout.addWidget(self.btn)

    def select_only_one(self, widget: str):
        btn: NavButton
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget: btn.set_active(True)
            else: btn.set_active(False)

    def deselect_all(self):
        btn: NavButton
        for btn in self.findChildren(QPushButton):
            btn.set_active(False)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def toggle_animation(self):
        self.animation = QPropertyAnimation(self._container, b"minimumWidth")
        self.animation.stop()
        if self.width() == self._themes.navigation["minimum_width"]:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._themes.navigation["maximum_width"])
            self.toggle_button.set_expand(True)
            self.toggle_button.set_icon(self._icon_hide_name)
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._themes.navigation["minimum_width"])
            self.toggle_button.set_expand(False)
            self.toggle_button.set_icon(self._icon_show_name)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(self._themes.time_animation)
        self.animation.start()

    def btn_clicked(self):
        self.clicked.emit(self.btn)

    def btn_released(self):
        self.released.emit(self.btn)
