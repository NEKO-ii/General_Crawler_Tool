# 底部信息栏
# ///////////////////////////////////////////////////////////////
from core.sys import Themes
from ui.preload.imp_qt import QWidget, QHBoxLayout, QFrame, Qt, QSizePolicy, QSpacerItem, QLabel


class Credits(QWidget):

    def __init__(self, copyright: str, version: str, themes: Themes, font: dict):
        super().__init__()

        self._copyright = copyright
        self._version = version
        self._themes = themes
        self._font = font
        self._radius = 8
        self._padding = 10

        self.setup()

    def setup(self):
        self.widget_layout = QHBoxLayout(self)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)

        style = F"""
        #bg_frame {{
            border-radius: {self._radius}px;
            background-color: {self._themes.color["bg_2"]};
        }}
        .QLabel {{
            font: {self._font["text_size"]}pt "{self._font["family"]}";
            color: {self._themes.color["text_description"]};
            padding-left: {self._padding}px;
            padding-right: {self._padding}px;
        }}
        """

        self.bg_frame = QFrame()
        self.bg_frame.setObjectName("bg_frame")
        self.bg_frame.setStyleSheet(style)

        self.widget_layout.addWidget(self.bg_frame)

        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setContentsMargins(0, 0, 0, 0)

        self.copyright_label = QLabel(self._copyright)
        self.copyright_label.setAlignment(Qt.AlignVCenter)

        self.version_label = QLabel(self._version)
        self.version_label.setAlignment(Qt.AlignVCenter)

        self.separator = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bg_layout.addWidget(self.copyright_label)
        self.bg_layout.addSpacerItem(self.separator)
        self.bg_layout.addWidget(self.version_label)
