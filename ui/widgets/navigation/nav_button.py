# 导航栏按钮
# ///////////////////////////////////////////////////////////////
from typing import Any

from core.sys.themes import Themes
from ui.func.iconsetter import IconSetter
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
    _iconActive: str
    _icon: str

    _set_icon_color: str
    _set_bg_color: str

    _isActive: bool
    _isActive_tab: bool
    _isExpand: bool

    # ///////////////////////////////////////////////////////////////

    def __init__(self, container, buttonId, buttonText, tooltipText, themes, iconName, isActive=False) -> None:
        super().__init__()

        self._container = container
        self._tooltipText = tooltipText
        self._themes = themes
        self._iconActive = IconSetter.setSvgIcon("icon_nav_button_active.svg")
        self._icon = IconSetter.setSvgIcon(iconName)
        self._isActive = isActive
        self._isActive_tab = False
        self._isExpand = False
        self._set_icon_color = self._themes.color["icon_color"]
        self._set_bg_color = self._themes.color["dark_1"]

        self.setObjectName(buttonId)
        self.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.setText(buttonText)
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.setCursor(Qt.PointingHandCursor)

        self.tooltip = ToolTip(self._container, tooltipText, self._themes.color["dark_1"], self._themes.color["text_foreground"], self._themes.color["context_color"])
        self.tooltip.hide()

    # API
    # ///////////////////////////////////////////////////////////////
    def c_setActive(self, isActive):
        self._isActive = isActive
        if isActive is False:
            self._set_icon_color = self._themes.color["icon_color"]
            self._set_bg_color = self._themes.color["dark_1"]
        self.repaint()

    def c_setActiveTab(self, isActive):
        self._isActive_tab = isActive
        if not isActive:
            self._set_icon_color = self._themes.color["icon_color"]
            self._set_bg_color = self._themes.color["dark_1"]
        self.repaint()

    def c_isActive(self):
        return self._isActive

    def c_isActive_tab(self):
        return self._isActive_tab

    def c_setExpand(self, isExpand: bool):
        self._isExpand = isExpand

    def c_setIcon(self, iconName):
        self._icon = IconSetter.setSvgIcon(iconName)
        self.repaint()

    def _changeStyle(self, event):
        if event == QEvent.Enter:
            if self._isActive is False:
                self._set_icon_color = self._themes.color["icon_hover"]
                self._set_bg_color = self._themes.color["dark_3"]
            self.repaint()
        elif event == QEvent.Leave:
            if self._isActive is False:
                self._set_icon_color = self._themes.color["icon_color"]
                self._set_bg_color = self._themes.color["dark_1"]
            self.repaint()
        elif event == QEvent.MouseButtonPress:
            if self._isActive is False:
                self._set_icon_color = self._themes.color["context_color"]
                self._set_bg_color = self._themes.color["dark_4"]
            self.repaint()
        elif event == QEvent.MouseButtonRelease:
            if self._isActive is False:
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

        if self._isActive:
            painter.setBrush(QColor(self._themes.color["context_color"]))
            painter.drawRoundedRect(rect_blue, 8, 8)
            painter.setBrush(QColor(self._themes.color["bg_1"]))
            painter.drawRoundedRect(rect_inside_active, 8, 8)
            self._set_icon_color = self._themes.color["icon_active"]
            self._setIconActive(painter, self._iconActive, self.width())
            painter.setPen(QColor(self._themes.color["text_active"]))
            painter.drawText(rect_text, Qt.AlignVCenter, self.text())
            self._iconPaint(painter, self._icon, rect_icon, self._set_icon_color)
        elif self._isActive_tab:
            painter.setBrush(QColor(self._themes.color["dark_4"]))
            painter.drawRoundedRect(rect_blue, 8, 8)
            painter.setBrush(QColor(self._themes.color["bg_1"]))
            painter.drawRoundedRect(rect_inside_active, 8, 8)
            self._set_icon_color = self._themes.color["icon_active"]
            self._setIconActive(painter, self._icon, self.width())
            painter.setPen(QColor(self._themes.color["text_active"]))
            painter.drawText(rect_text, Qt.AlignVCenter, self.text())
            self._iconPaint(painter, self._icon, rect_icon, self._set_icon_color)
        elif self._isExpand:
            painter.setBrush(QColor(self._themes.color["dark_3"]))
            painter.drawRoundedRect(rect_inside, 8, 8)
            painter.setPen(QColor(self._themes.color["text_foreground"]))
            painter.drawText(rect_text, Qt.AlignVCenter, self.text())
            self._iconPaint(painter, self._icon, rect_icon, self._themes.color["context_color"])
        else:
            painter.setBrush(QColor(self._set_bg_color))
            painter.drawRoundedRect(rect_inside, 8, 8)
            painter.setPen(QColor(self._themes.color["text_foreground"]))
            painter.drawText(rect_text, Qt.AlignVCenter, self.text())
            self._iconPaint(painter, self._icon, rect_icon, self._set_icon_color)
        painter.end()

    def enterEvent(self, event):
        self._changeStyle(QEvent.Enter)
        if self.width() == 50 and self._tooltipText:
            self._moveTooltip()
            self.tooltip.show()

    def leaveEvent(self, event):
        self._changeStyle(QEvent.Leave)
        self.tooltip.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._changeStyle(QEvent.MouseButtonPress)
            self.tooltip.hide()
            return self.clicked.emit(self)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._changeStyle(QEvent.MouseButtonRelease)
            return self.released.emit(self)

    # 私有方法
    # ///////////////////////////////////////////////////////////////
    def _setIconActive(self, qp: QPainter, icon, width):
        icon = QPixmap(icon)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._themes.color["bg_1"])
        qp.drawPixmap(width - 5, 0, icon)
        painter.end()

    def _iconPaint(self, qp: QPainter, icon, rect: QRect, color):
        icon = QPixmap(icon)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap((rect.width() - icon.width()) / 2, (rect.height() - icon.height()) / 2, icon)
        painter.end()

    def _moveTooltip(self):
        gp = self.mapToGlobal(QPoint(0, 0))
        pos = self._container.mapFromGlobal(gp)
        pos_x = pos.x() + self.width() + 5
        pos_y = pos.y() + (self.width() - self.tooltip.height()) // 2
        self.tooltip.move(pos_x, pos_y)
