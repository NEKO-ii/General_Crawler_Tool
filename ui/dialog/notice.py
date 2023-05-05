from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)
from ui.widgets import PushButton
from core.static import Define


class Notice(QDialog):
    color: dict
    ticon: dict

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.color = Define.TYPE_COLOR
        self.ticon = Define.TYPE_ICON
        self.setWindowTitle("提示窗口")
        self.setStyleSheet("background-color: #2c313c;")
        self.setFixedSize(300, 120)
        self.setupUi()
        self.btn_accept.clicked.connect(self.btn_accept_clicked)

    def exec(self, title="标题", msg="信息", titleType="info", msgType="default", btnAcceptText="确认") -> bool:
        self.label_title.setText(F"{self.ticon[titleType]} {title}")
        self.label_text.setText(msg)
        self.btn_accept.setText(btnAcceptText)
        self.label_title.setStyleSheet(F"color: {self.color[titleType]};")
        self.label_text.setStyleSheet(F"color: {self.color[msgType]};")
        super().exec()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Notice")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(self)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(11)
        self.label_title.setFont(font)
        self.label_title.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_title)

        self.label_text = QLabel(self)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_text)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_accept = PushButton(self, type="success")
        self.btn_accept.setObjectName(u"btn_accept")

        self.horizontalLayout.addWidget(self.btn_accept)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.label_title.setText(QCoreApplication.translate("Question", u"\u6807\u9898", None))
        self.label_text.setText(QCoreApplication.translate("Question", u"\u5185\u5bb9", None))
        self.btn_accept.setText(QCoreApplication.translate("Question", u"\u786e\u8ba4", None))

    def btn_accept_clicked(self) -> None:
        self.accept()
