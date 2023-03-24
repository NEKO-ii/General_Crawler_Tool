# 导航栏按钮
# ///////////////////////////////////////////////////////////////
from typing import Any

from core.sys import Themes
from ui.func.icon_setter import IconSetter
from ui.preload.imp_qt import (QColor, QEvent, QPainter, QPixmap, QPoint, QPushButton, QRect, Qt, Signal)

from .tooltip import ToolTip


class NavButton(QPushButton):
    """导航栏按钮
    """
    # 信号
    clicked = Signal(object)
    released = Signal(object)

    # 属性
    # ///////////////////////////////////////////////////////////////
    tooltip: ToolTip

    _container: Any
    _themes: Themes
    _icon_active: str
    _icon: str

    _set_icon_color: str
    _set_bg_color: str

    _is_active: bool
    _is_active_tab: bool
    _is_expand: bool

    # ///////////////////////////////////////////////////////////////

    def __init__(self, container, button_id, button_text, tooltip_text, themes, icon_name, is_active=False) -> None:
        super().__init__()

        self._container = container
        self._tooltip_text = tooltip_text
        self._themes = themes
        self._icon_active = IconSetter.set_svg_icon("icon_nav_button_active.svg")
        self._icon = IconSetter.set_svg_icon(icon_name)
        self._is_active = is_active
        self._is_active_tab = False
        self._is_expand = False
        self._set_icon_color = self._themes.color["icon_color"]
        self._set_bg_color = self._themes.color["dark_1"]

        self.setObjectName(button_id)
        self.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.setText(button_text)
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.setCursor(Qt.PointingHandCursor)

        self.tooltip = ToolTip(self._container, tooltip_text, self._themes.color["dark_1"], self._themes.color["text_foreground"], self._themes.color["context_color"])
        self.tooltip.hide()

    # API
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        if is_active is False:
            self._set_icon_color = self._themes.color["icon_color"]
            self._set_bg_color = self._themes.color["dark_1"]
        self.repaint()

    def set_active_tab(self, is_active):
        self._is_active_tab = is_active
        if not is_active:
            self._set_icon_color = self._themes.color["icon_color"]
            self._set_bg_color = self._themes.color["dark_1"]
        self.repaint()

    def is_active(self):
        return self._is_active

    def is_active_tab(self):
        return self._is_active_tab

    def set_expand(self, is_expand: bool):
        self.is_expand = is_expand

    def set_icon(self, icon_name):
        self._icon = IconSetter.set_svg_icon(icon_name)
        self.repaint()

    def change_style(self, event):
        if event == QEvent.Enter:
            if self._is_active is False:
                self._set_icon_color = self._themes.color["icon_hover"]
                self._set_bg_color = self._themes.color["dark_3"]
            self.repaint()
        elif event == QEvent.Leave:
            if self._is_active is False:
                self._set_icon_color = self._themes.color["icon_color"]
                self._set_bg_color = self._themes.color["dark_1"]
            self.repaint()
        elif event == QEvent.MouseButtonPress:
            if self._is_active is False:
                self._set_icon_color = self._themes.color["context_color"]
                self._set_bg_color = self._themes.color["dark_4"]
            self.repaint()
        elif event == QEvent.MouseButtonRelease:
            if self._is_active is False:
                self._set_icon_color = self._themes.color["icon_hover"]
                self._set_bg_color = self._themes.color["dark_3"]
            self.repaint()

    # 重写父类方法
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setFont(self.font())

        rect = QRect(4, 5, self.width(), self.height() - 10)
        rect_inside = QRect(4, 5, self.width() - 8, self.height() - 10)
        rect_icon = QRect(0, 0, 50, self.height())
        rect_blue = QRect(4, 5, 20, self.height() - 10)
        rect_inside_active = QRect(7, 5, self.width(), self.height() - 10)
        rect_text = QRect(45, 0, self.width() - 50, self.height())

        if self._is_active:
            painter.setBrush(QColor(self._themes.color["context_color"]))
            painter.drawRoundedRect(rect_blue, 8, 8)
            painter.setBrush(QColor(self._themes.color["bg_1"]))
            painter.drawRoundedRect(rect_inside_active, 8, 8)
            self._set_icon_color = self._themes.color["icon_active"]
            self.icon_active(painter, self._icon_active, self.width())
            painter.setPen(QColor(self._themes.color["text_active"]))
            painter.drawText(rect_text, Qt.AlignVCenter, self.text())
            self.icon_paint(painter, self._icon, rect_icon, self._set_icon_color)
        elif self._is_active_tab:
            painter.setBrush(QColor(self._themes.color["dark_4"]))
            painter.drawRoundedRect(rect_blue, 8, 8)
            painter.setBrush(QColor(self._themes.color["bg_1"]))
            painter.drawRoundedRect(rect_inside_active, 8, 8)
            self._set_icon_color = self._themes.color["icon_active"]
            self.icon_active(painter, self._icon, self.width())
            painter.setPen(QColor(self._themes.color["text_active"]))
            painter.drawText(rect_text, Qt.AlignVCenter, self.text())
            self.icon_paint(painter, self._icon, rect_icon, self._set_icon_color)
        elif self._is_expand:
            painter.setBrush(QColor(self._themes.color["dark_3"]))
            painter.drawRoundedRect(rect_inside, 8, 8)
            painter.setPen(QColor(self._themes.color["text_foreground"]))
            painter.drawText(rect_text, Qt.AlignVCenter, self.text())
            self.icon_paint(painter, self._icon, rect_icon, self._themes.color["context_color"])
        else:
            painter.setBrush(QColor(self._set_bg_color))
            painter.drawRoundedRect(rect_inside, 8, 8)
            painter.setPen(QColor(self._themes.color["text_foreground"]))
            painter.drawText(rect_text, Qt.AlignVCenter, self.text())
            self.icon_paint(painter, self._icon, rect_icon, self._set_icon_color)
        painter.end()

    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        if self.width() == 50 and self._tooltip_text:
            self.move_tooltip()
            self.tooltip.show()

    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        self.tooltip.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            self.tooltip.hide()
            return self.clicked.emit(self)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            return self.released.emit(self)

    # 私有方法
    # ///////////////////////////////////////////////////////////////
    def icon_active(self, qp: QPainter, icon, width):
        icon = QPixmap(icon)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._themes.color["bg_1"])
        qp.drawPixmap(width - 5, 0, icon)
        painter.end()

    def icon_paint(self, qp: QPainter, icon, rect: QRect, color):
        icon = QPixmap(icon)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap((rect.width() - icon.width()) / 2, (rect.height() - icon.height()) / 2, icon)
        painter.end()

    def move_tooltip(self):
        gp = self.mapToGlobal(QPoint(0, 0))
        pos = self._container.mapFromGlobal(gp)
        pos_x = pos.x() + self.width() + 5
        pos_y = pos.y() + (self.width() - self.tooltip.height()) // 2
        self.tooltip.move(pos_x, pos_y)
