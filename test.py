from typing import Optional
from ui.pages.tempview import Ui_TempviewPage
from core.sys.file import File, SysPath, DataType
from ui.dialog import Notice
from PySide6.QtCore import QObject, Signal, QThread, QFile, QByteArray, QIODevice


class Func_TempviewPage(QObject):
    ui: Ui_TempviewPage

    currentFilePath: str = None

    def __init__(self, ui) -> None:
        self.ui = ui
        self.fileReadThread = QThread()
        self._btnConnect()

    def _btnConnect(self) -> None:
        self.ui.indexPage_ui.btn_read.clicked.connect(self.solt_read)

    def solt_read(self) -> None:
        self.newtask = FileReadTask()
        self.newtask.setPath(self.currentFilePath)
        self.newtask.moveToThread(self.fileReadThread)
        self.newtask.sig_read_compleat.connect(self.solt_append_file_text)
        self.fileReadThread.started.connect(self.newtask.readfile)
        self.fileReadThread.start()

    def solt_append_file_text(self, text) -> None:
        pass


class FileReadTask(QObject):
    # sig_read_start = Signal()
    sig_read_compleat = Signal(str)

    path = None

    def __init__(self) -> None:
        super().__init__()

    def readfile(self) -> str:
        # self.sig_read_start.emit()
        file = QFile(self.path)
        file.open(QIODevice.OpenModeFlag.ReadOnly)
        self.sig_read_compleat.emit(file.readAll().toStdString())

    def setPath(self, path) -> None:
        self.path = path
