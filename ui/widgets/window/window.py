# 界面窗口
# ///////////////////////////////////////////////////////////////
from typing import Any
from core.sys import Themes, Settings
from ui.preload.imp_qt import QFrame, QHBoxLayout, QGraphicsDropShadowEffect, QColor


class Window(QFrame):
    """界面窗口类
    """
    style: str = """
    #pod_bg_app {{
        background-color: {bg_color};
        border-radius: {border_radius};
        border: {border_size}px solid {border_color};
    }}
    QFrame {{
        color: {text_color};
        font: {font_size}pt "{font_family}";
    }}
    """

    # 属性
    # ///////////////////////////////////////////////////////////////
    _container: Any
    _themes: Themes
    _settings: Settings
    _margin: int
    _spacing: int
    _border_radius: int
    _border_size: int
    _enable_shadow: bool

    slayout: QHBoxLayout
    shadow: QGraphicsDropShadowEffect

    # ///////////////////////////////////////////////////////////////

    def __init__(self, container, themes: Themes, settings: Settings):
        super().__init__()

        self._container = container
        self.slayout = QHBoxLayout(self)
        self._themes = themes
        self._settings = settings
        self._margin = 0
        self._spacing = 2
        self._border_radius = 10
        self._border_size = 2
        self._enable_shadow = True

        self._bg_color = self._themes.color["bg_1"]
        self._text_color = self._themes.color["text_foreground"]
        self._font_size = self._settings.font["text_size"]
        self._font_family = self._settings.font["family"]
        self._border_color = self._themes.color["bg_2"]

        self.set_stylesheet()

        self.setObjectName("pod_bg_app")
        self.slayout.setContentsMargins(self._margin, self._margin, self._margin, self._margin)
        self.slayout.setSpacing(self._spacing)

        if self._settings.hide_title_bar and self._enable_shadow:
            self.shadow = QGraphicsDropShadowEffect()
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 160))
            self.setGraphicsEffect(self.shadow)

    def set_stylesheet(self, border_radius=None, border_size=None) -> None:
        if border_radius is not None: self._border_radius = border_radius
        if border_size is not None: self._border_size = border_size

        self.setStyleSheet(
            self.style.format(bg_color=self._bg_color, border_radius=self._border_radius, border_size=self._border_size, border_color=self._border_color, text_color=self._text_color, font_size=self._font_size,
                              font_family=self._font_family))
