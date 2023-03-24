# 窗口边框
# ///////////////////////////////////////////////////////////////
from typing import Any
from ui.preload.imp_qt import QWidget, QSizeGrip, QMainWindow
from .widgets import Widgets


class Grips(QWidget):
    """窗口边框类
    """

    # 属性
    # ///////////////////////////////////////////////////////////////
    _container: Any
    wi: Widgets

    # ///////////////////////////////////////////////////////////////

    def __init__(self, parent, position, hide_grips=False):
        super().__init__()
        self._container = parent
        self.setParent(parent)
        self.wi = Widgets()

        if position == "top_left":
            self.wi.top_left(self)
            grip = QSizeGrip(self.wi.top_left_grip)
            grip.setFixedSize(self.wi.top_left_grip.size())
            self.setGeometry(5, 5, 15, 15)
            if hide_grips: self.wi.top_left_grip.setStyleSheet("background: transparent")

        if position == "top_right":
            self.wi.top_right(self)
            grip = QSizeGrip(self.wi.top_right_grip)
            grip.setFixedSize(self.wi.top_right_grip.size())
            self.setGeometry(self._container.width() - 20, 5, 15, 15)
            if hide_grips: self.wi.top_right_grip.setStyleSheet("background: transparent")

        if position == "bottom_left":
            self.wi.bottom_left(self)
            grip = QSizeGrip(self.wi.bottom_left_grip)
            grip.setFixedSize(self.wi.bottom_left_grip.size())
            self.setGeometry(5, self._container.height() - 20, 15, 15)
            if hide_grips: self.wi.bottom_left_grip.setStyleSheet("background: transparent")

        if position == "bottom_right":
            self.wi.bottom_right(self)
            grip = QSizeGrip(self.wi.bottom_right_grip)
            grip.setFixedSize(self.wi.bottom_right_grip.size())
            self.setGeometry(self._container.width() - 20, self._container.height() - 20, 15, 15)
            if hide_grips: self.wi.bottom_right_grip.setStyleSheet("background: transparent")

        if position == "top":
            self.wi.top(self)
            self.setGeometry(0, 5, self._container.width(), 10)
            self.setMaximumHeight(10)

            def resize_top(event):
                delta = event.pos()
                height = max(self._container.minimumHeight(), self._container.height() - delta.y())
                geo = self._container.geometry()
                geo.setTop(geo.bottom() - height)
                self._container.setGeometry(geo)
                event.accept()

            self.wi.top_grip.mouseMoveEvent = resize_top
            if hide_grips: self.wi.top_grip.setStyleSheet("background: transparent")

        elif position == "bottom":
            self.wi.bottom(self)
            self.setGeometry(0, self._container.height() - 10, self._container.width(), 10)
            self.setMaximumHeight(10)

            def resize_bottom(event):
                delta = event.pos()
                height = max(self._container.minimumHeight(), self._container.height() + delta.y())
                self._container.resize(self._container.width(), height)
                event.accept()

            self.wi.bottom_grip.mouseMoveEvent = resize_bottom
            if hide_grips: self.wi.bottom_grip.setStyleSheet("background: transparent")

        elif position == "left":
            self.wi.left(self)
            self.setGeometry(0, 10, 10, self._container.height())
            self.setMaximumWidth(10)

            def resize_left(event):
                delta = event.pos()
                width = max(self._container.minimumWidth(), self._container.width() - delta.x())
                geo = self._container.geometry()
                geo.setLeft(geo.right() - width)
                self._container.setGeometry(geo)
                event.accept()

            self.wi.left_grip.mouseMoveEvent = resize_left
            if hide_grips: self.wi.left_grip.setStyleSheet("background: transparent")

        elif position == "right":
            self.wi.right(self)
            self.setGeometry(self._container.width() - 10, 10, 10, self._container.height())
            self.setMaximumWidth(10)

            def resize_right(event):
                delta = event.pos()
                width = max(self._container.minimumWidth(), self._container.width() + delta.x())
                self._container.resize(width, self._container.height())
                event.accept()

            self.wi.right_grip.mouseMoveEvent = resize_right

            if hide_grips: self.wi.right_grip.setStyleSheet("background: transparent")

    # 重写方法
    # ///////////////////////////////////////////////////////////////

    def mouseReleaseEvent(self, event):
        self.mousePos = None

    def resizeEvent(self, event):
        if hasattr(self.wi, "top_grip"):
            self.wi.top_grip.setGeometry(0, 0, self.width(), 10)
        elif hasattr(self.wi, "bottom_grip"):
            self.wi.bottom_grip.setGeometry(0, 0, self.width(), 10)
        elif hasattr(self.wi, "left_grip"):
            self.wi.left_grip.setGeometry(0, 0, 10, self.height() - 20)
        elif hasattr(self.wi, "right_grip"):
            self.wi.right_grip.setGeometry(0, 0, 10, self.height() - 20)
        elif hasattr(self.wi, "top_right_grip"):
            self.wi.top_right_grip.setGeometry(self.width() - 15, 0, 15, 15)
        elif hasattr(self.wi, "bottom_left_grip"):
            self.wi.bottom_left_grip.setGeometry(0, self.height() - 15, 15, 15)
        elif hasattr(self.wi, "bottom_right_grip"):
            self.wi.bottom_right_grip.setGeometry(self.width() - 15, self.height() - 15, 15, 15)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
