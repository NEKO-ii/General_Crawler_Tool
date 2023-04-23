# 标题栏按钮
# ///////////////////////////////////////////////////////////////
from typing import Any

from core.sys import Themes
from ui.preload.imp_qt import (QBrush, QColor, QEvent, QPainter, QPixmap,
                               QPoint, QPushButton, QRect, Qt, Signal)

from .tooltip import ToolTip


# PY TITLE BUTTON
# ///////////////////////////////////////////////////////////////
class TitleButton(QPushButton):
    """标题栏按钮类
    """
    # 信号
    clicked = Signal(object)
    released = Signal(object)

    # 属性
    # ///////////////////////////////////////////////////////////////
    _container: Any  # 存放导航栏的组件
    _centralWidget: Any  # 窗口中心组件
    _themes: Themes
    _buttonId: str
    _tooltipText: str
    _iconPath: str
    _isActive: bool

    _width: int
    _height: int
    _radius: int
    _topMargin: int

    tooltip: ToolTip

    _set_bgColor: str
    _set_iconColor: str
    _set_iconPath: str
    _set_borderRadius: int

    # ///////////////////////////////////////////////////////////////
    def __init__(self, container, centralWidget, buttonId, tooltipText, themes, iconPath, isActive=False) -> None:
        super().__init__()
        self._container = container
        self._centralWidget = centralWidget
        self._buttonId = buttonId
        self._tooltipText = tooltipText
        self._themes = themes
        self._iconPath = iconPath
        self._isActive = isActive

        self._width = 30
        self._height = 30
        self._radius = 6

        self._set_bgColor = self._themes.color["bg_2"]
        self._set_iconColor = self._themes.color["icon_color"]
        self._set_iconPath = self._iconPath
        self._set_borderRadius = self._radius

        self.setObjectName(buttonId)
        self.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.setFixedSize(self._width, self._height)
        self.setCursor(Qt.PointingHandCursor)

        self._topMargin = self.height() + 6

        self.setup()

    def setup(self) -> None:
        self.tooltip = ToolTip(self._centralWidget, self._tooltipText, self._themes.color["dark_1"], self._themes.color["text_foreground"], self._themes.color["context_color"])
        self.tooltip.hide()

    # API
    # ///////////////////////////////////////////////////////////////
    def c_setActive(self, is_active):
        self._isActive = is_active
        self.repaint()

    def c_isActive(self):
        return self._isActive

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def _changeStyle(self, event):
        if event == QEvent.Enter:
            self._set_bgColor = self._themes.color["bg_1"]
            self._set_iconColor = self._themes.color["icon_hover"]
            self.repaint()
        elif event == QEvent.Leave:
            self._set_bgColor = self._themes.color["bg_2"]
            self._set_iconColor = self._themes.color["icon_color"]
            self.repaint()
        elif event == QEvent.MouseButtonPress:
            self._set_bgColor = self._themes.color["bg_1"]
            self._set_iconColor = self._themes.color["icon_pressed"]
            self.repaint()
        elif event == QEvent.MouseButtonRelease:
            self._set_bgColor = self._themes.color["bg_2"]
            self._set_iconColor = self._themes.color["icon_hover"]
            self.repaint()

    def _setIcon(self, icon_path):
        self._set_iconPath = icon_path
        self.repaint()

    def _iconPaint(self, qp: QPainter, icon, rect: QRect):
        icon = QPixmap(icon)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        if self._isActive: painter.fillRect(icon.rect(), self._themes["icon_active"])
        else: painter.fillRect(icon.rect(), self._set_iconColor)
        qp.drawPixmap((rect.width() - icon.width()) / 2, (rect.height() - icon.height()) / 2, icon)
        painter.end()

    def _moveTooltip(self):
        gp = self.mapToGlobal(QPoint(0, 0))
        pos = self._container.mapFromGlobal(gp)
        pos_x = (pos.x() - self.tooltip.width()) + self.width() + 5
        pos_y = pos.y() + self._topMargin
        self.tooltip.move(pos_x, pos_y)

    # 方法重写
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self._isActive: brush = QBrush(QColor(self._themes.color["context_color"]))
        else: brush = QBrush(QColor(self._set_bgColor))

        rect = QRect(0, 0, self.width(), self.height())
        painter.setPen(Qt.NoPen)
        painter.setBrush(brush)
        painter.drawRoundedRect(rect, self._set_borderRadius, self._set_borderRadius)

        self._iconPaint(painter, self._set_iconPath, rect)
        painter.end()

    def enterEvent(self, event):
        self._changeStyle(QEvent.Enter)
        self._moveTooltip()
        self.tooltip.show()

    def leaveEvent(self, event):
        self._changeStyle(QEvent.Leave)
        self._moveTooltip()
        self.tooltip.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._changeStyle(QEvent.MouseButtonPress)
            self.setFocus()
            return self.clicked.emit(self)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._changeStyle(QEvent.MouseButtonRelease)
            return self.released.emit(self)
