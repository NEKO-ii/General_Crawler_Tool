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
    _central_widget: Any  # 窗口中心组件
    _themes: Themes
    _btn_id: str
    _tooltip_text: str
    _icon_path: str
    _is_active: bool

    _width: int
    _height: int
    _radius: int
    _top_margin: int

    tooltip: ToolTip

    _set_bg_color: str
    _set_icon_color: str
    _set_icon_path: str
    _set_border_radius: int

    # ///////////////////////////////////////////////////////////////
    def __init__(self, container, central_widget, btn_id, tooltip_text, themes, icon_path, is_active=False) -> None:
        super().__init__()
        self._container = container
        self._central_widget = central_widget
        self._btn_id = btn_id
        self._tooltip_text = tooltip_text
        self._themes = themes
        self._icon_path = icon_path
        self._is_active = is_active

        self._width = 30
        self._height = 30
        self._radius = 6

        self._set_bg_color = self._themes.color["bg_2"]
        self._set_icon_color = self._themes.color["icon_color"]
        self._set_icon_path = self._icon_path
        self._set_border_radius = self._radius

        self.setObjectName(btn_id)
        self.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.setFixedSize(self._width, self._height)
        self.setCursor(Qt.PointingHandCursor)

        self._top_margin = self.height() + 6

        self.setup()

    def setup(self) -> None:
        self.tooltip = ToolTip(self._central_widget, self._tooltip_text, self._themes.color["dark_1"], self._themes.color["text_foreground"], self._themes.color["context_color"])
        self.tooltip.hide()

    # API
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        self.repaint()

    def is_active(self):
        return self._is_active

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def change_style(self, event):
        if event == QEvent.Enter:
            self._set_bg_color = self._themes.color["bg_1"]
            self._set_icon_color = self._themes.color["icon_hover"]
            self.repaint()
        elif event == QEvent.Leave:
            self._set_bg_color = self._themes.color["bg_2"]
            self._set_icon_color = self._themes.color["icon_color"]
            self.repaint()
        elif event == QEvent.MouseButtonPress:
            self._set_bg_color = self._themes.color["bg_1"]
            self._set_icon_color = self._themes.color["icon_pressed"]
            self.repaint()
        elif event == QEvent.MouseButtonRelease:
            self._set_bg_color = self._themes.color["bg_2"]
            self._set_icon_color = self._themes.color["icon_hover"]
            self.repaint()

    def set_icon(self, icon_path):
        self._set_icon_path = icon_path
        self.repaint()

    def icon_paint(self, qp: QPainter, icon, rect: QRect):
        icon = QPixmap(icon)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        if self._is_active: painter.fillRect(icon.rect(), self._themes["icon_active"])
        else: painter.fillRect(icon.rect(), self._set_icon_color)
        qp.drawPixmap((rect.width() - icon.width()) / 2, (rect.height() - icon.height()) / 2, icon)
        painter.end()

    def move_tooltip(self):
        gp = self.mapToGlobal(QPoint(0, 0))
        pos = self._container.mapFromGlobal(gp)
        pos_x = (pos.x() - self.tooltip.width()) + self.width() + 5
        pos_y = pos.y() + self._top_margin
        self.tooltip.move(pos_x, pos_y)

    # 方法重写
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self._is_active: brush = QBrush(QColor(self._themes.color["context_color"]))
        else: brush = QBrush(QColor(self._set_bg_color))

        rect = QRect(0, 0, self.width(), self.height())
        painter.setPen(Qt.NoPen)
        painter.setBrush(brush)
        painter.drawRoundedRect(rect, self._set_border_radius, self._set_border_radius)

        self.icon_paint(painter, self._set_icon_path, rect)
        painter.end()

    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        self.move_tooltip()
        self.tooltip.show()

    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        self.move_tooltip()
        self.tooltip.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            self.setFocus()
            return self.clicked.emit(self)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            return self.released.emit(self)
