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
    _borderRadius: int
    _borderSize: int
    _enableShadow: bool

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
        self._borderRadius = 10
        self._borderSize = 2
        self._enableShadow = True

        self._bgColor = self._themes.color["bg_1"]
        self._textColor = self._themes.color["text_foreground"]
        self._fontSize = self._settings.font["text_size"]
        self._fontFamily = self._settings.font["family"]
        self._borderColor = self._themes.color["bg_2"]

        self.c_setStylesheet()

        self.setObjectName("pod_bg_app")
        self.slayout.setContentsMargins(self._margin, self._margin, self._margin, self._margin)
        self.slayout.setSpacing(self._spacing)

        if self._settings.hide_title_bar and self._enableShadow:
            self.shadow = QGraphicsDropShadowEffect()
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 160))
            self.setGraphicsEffect(self.shadow)

    def c_setStylesheet(self, borderRadius=None, borderSize=None) -> None:
        if borderRadius is not None: self._borderRadius = borderRadius
        if borderSize is not None: self._borderSize = borderSize

        self.setStyleSheet(
            self.style.format(bg_color=self._bgColor, border_radius=self._borderRadius, border_size=self._borderSize, border_color=self._borderColor, text_color=self._textColor, font_size=self._fontSize,
                              font_family=self._fontFamily))
