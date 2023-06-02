# 复制并修改自Dialog_ConfigMessageInput.py
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QDialog, QWidget, QFormLayout, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)
from core.sys.file import File, SysPath, DataType
from core.static.define import Define
from ui.widgets import PushButton, LineEdit, TextEdit


class ScriptMessageInput(QDialog):

    fileType: str
    color: dict

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.color = Define.TYPE_COLOR
        self.setWindowTitle("脚本保存")
        self.setStyleSheet("background-color: #2c313c; color: #aaaabb;")
        self.setFixedSize(400, 220)
        self.setupUi()
        self._btnConnect()

    def _btnConnect(self) -> None:
        """按钮点击事件链接"""
        self.btn_reject.clicked.connect(self.reject)
        self.btn_check.clicked.connect(self.checkData)
        self.btn_save.clicked.connect(self.btn_save_clicked)

    def _initData(self) -> None:
        """初始化控件内容数据"""
        self.ledit_scriptName.setText("新建脚本")
        self.ledit_fileBaseName.setText("new_script")
        if self.fileType:
            self.ledit_fileExtendName.setText(F".{self.fileType}")
            self.ledit_fileExtendName.setEnabled(False)
        else:
            self.ledit_fileExtendName.clear()
            self.ledit_fileExtendName.setEnabled(True)
        self.tedit_comment.clear()
        self._setCheckState()

    def _setCheckState(self, state: str = "default", msg: str = "") -> None:
        """更新检查结果显示标签"""
        if state == "default":
            self.label_checkMsg.setText("未检查")
            self.label_checkMsg.setStyleSheet(F"color: {self.color['default']};")
        elif state == "pass":
            self.label_checkMsg.setText("数据可用")
            self.label_checkMsg.setStyleSheet(F"color: {self.color['success']};")
        elif state == "warn":
            self.label_checkMsg.setText(msg)
            self.label_checkMsg.setStyleSheet(F"color: {self.color['warn']};")
        elif state == "error":
            self.label_checkMsg.setText(msg)
            self.label_checkMsg.setStyleSheet(F"color: {self.color['error']};")

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"self")
        self.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self)
        self.formLayout = QFormLayout()

        self.label = QLabel(self)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ledit_scriptName = LineEdit(self)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ledit_scriptName)

        self.label_2 = QLabel(self)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.ledit_fileBaseName = LineEdit(self, placeHolderText="文件名")
        self.horizontalLayout_3.addWidget(self.ledit_fileBaseName)

        self.ledit_fileExtendName = LineEdit(self, placeHolderText="扩展名")
        self.ledit_fileExtendName.setEnabled(False)
        self.ledit_fileExtendName.setMaximumWidth(100)
        self.horizontalLayout_3.addWidget(self.ledit_fileExtendName)

        self.fileNameWidget = QWidget(self)
        self.fileNameWidget.setLayout(self.horizontalLayout_3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.fileNameWidget)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.label_3 = QLabel(self)
        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_checkMsg = QLabel(self)
        self.horizontalLayout_2.addWidget(self.label_checkMsg)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tedit_comment = TextEdit(self)
        self.verticalLayout.addWidget(self.tedit_comment)

        self.horizontalLayout = QHBoxLayout()
        self.btn_reject = PushButton(self, type="error")
        self.horizontalLayout.addWidget(self.btn_reject)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_check = PushButton(self, type="primary")
        self.horizontalLayout.addWidget(self.btn_check)

        self.btn_save = PushButton(self, type="success")
        self.horizontalLayout.addWidget(self.btn_save)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.label.setText(QCoreApplication.translate("self", u"\u914d\u7f6e\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("self", u"\u6587\u4ef6\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("self", u"\u8bf4\u660e\u003a", None))
        self.label_checkMsg.setText(QCoreApplication.translate("self", u"\u4fe1\u606f\u53ef\u7528", None))
        self.btn_reject.setText(QCoreApplication.translate("self", u"\u53d6\u6d88", None))
        self.btn_check.setText(QCoreApplication.translate("self", u"\u68c0\u67e5", None))
        self.btn_save.setText(QCoreApplication.translate("self", u"\u4fdd\u5b58", None))

    # 每次打开时初始化数据并在控件中显示
    def showEvent(self, event) -> None:
        self._initData()
        return super().showEvent(event)

    def checkData(self) -> bool:
        passf = True
        if self.ledit_fileBaseName.text() == "":
            passf = False
            self._setCheckState("error", "文件名不能为空")
        elif self.ledit_fileExtendName.text() == "":
            passf = False
            self._setCheckState("error", "扩展名不能为空")
        elif self.ledit_fileExtendName.text() not in [".py",".js"]:
            passf = False
            self._setCheckState("error", "只支持Python和JS脚本")
        elif self.ledit_scriptName.text() == "":
            passf = False
            self._setCheckState("error", "脚本名称不能为空")
        if passf:
            fileName = F"{self.ledit_fileBaseName.text()}{self.ledit_fileExtendName.text()}"
            path = File.path(SysPath.SCRIPT, fileName)
            if File.checkFileName(fileName) is False:
                passf = False
                self._setCheckState("error", "文件名无效(包含非法字符)")
            elif File.isFileExists(path):
                passf = False
                self._setCheckState("error", "文件已存在")
            else:
                for item in File.read_opt(File.path(SysPath.CACHE, "custom_script.dat"), DataType.LIST, "#"):
                    if self.ledit_scriptName.text() == eval(item)[0]:
                        self._setCheckState("error", "存在同名配置")
                        passf = False
                        break
        if passf: self._setCheckState("pass")
        return passf

    def btn_save_clicked(self) -> None:
        if self.checkData():
            self.accept()

    def exec(self, fileType: str) -> tuple[int, dict]:
        self.fileType = fileType
        code = super().exec()
        data = {"script_name": self.ledit_scriptName.text(), "file_name": F"{self.ledit_fileBaseName.text()}{self.ledit_fileExtendName.text()}", "comment": self.tedit_comment.toPlainText()}
        return (code, data)
