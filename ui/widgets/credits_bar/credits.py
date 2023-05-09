# 底部信息栏
# ///////////////////////////////////////////////////////////////
from core.sys.themes import Themes
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
        self.widgetLayout = QHBoxLayout(self)
        self.widgetLayout.setContentsMargins(0, 0, 0, 0)

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

        self.widgetLayout.addWidget(self.bg_frame)

        self.bgLayout = QHBoxLayout(self.bg_frame)
        self.bgLayout.setContentsMargins(0, 0, 0, 0)

        self.copyrightLabel = QLabel(self._copyright)
        self.copyrightLabel.setAlignment(Qt.AlignVCenter)

        self.versionLabel = QLabel(self._version)
        self.versionLabel.setAlignment(Qt.AlignVCenter)

        self.separator = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bgLayout.addWidget(self.copyrightLabel)
        self.bgLayout.addSpacerItem(self.separator)
        self.bgLayout.addWidget(self.versionLabel)
