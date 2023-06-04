from .Ui_TempviewPage import Ui_TempviewPage
from core.sys.file import File, SysPath, DataType
from ui.dialog import Notice, Question
from PySide6.QtCore import QObject, Signal, QThread, QFile, QIODevice
from PySide6.QtWidgets import QFileDialog
from core.static.define import Define
from shutil import copyfile


class Func_TempviewPage(QObject):
    ui: Ui_TempviewPage

    INDEX_TO_FILE_DIR_PATH = {0: "requestout", 1: "parseout"}
    INDEX_TO_DAT_FILE_NAME = {0: "temp_request.dat", 1: "temp_parse.dat"}
    INDEX_TO_TABLE_HEADDER = {0: ["文件名", "请求域名", "请求方式", "时间", "状态码", "编码", "文件大小"], 1: ["文件名", "数据类型", "时间", "数据来源", "是否输出", "输出文件", "文件大小"]}
    INDEX_TO_FILE_SIZE_COL = {0: 6, 1: 6}

    currentComboIndex: int = 0
    currentTableRow: list = []
    currentFilePath: str = None
    fileReadThread: QThread = None
    flag_threadRunning: bool = False

    def __init__(self, ui) -> None:
        self.ui = ui
        self.fileReadThread = QThread()
        self._btnConnect()
        self._signalConnect()

    def _btnConnect(self) -> None:
        self.ui.indexPage_ui.btn_read.clicked.connect(self.solt_read)
        self.ui.indexPage_ui.btn_export.clicked.connect(self.solt_export)
        self.ui.indexPage_ui.btn_delete.clicked.connect(self.solt_delete)
        self.ui.indexPage_ui.btn_flush.clicked.connect(self.solt_flush)
        self.ui.indexPage_ui.btn_clearSelect.clicked.connect(self.ui.indexPage_ui.ledit_select.clear)

        self.ui.readPage_ui.btn_back.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.indexPage))

    def _signalConnect(self) -> None:
        self.ui.indexPage_ui.combo_chooseView.currentIndexChanged.connect(self.solt_change_datasource)
        self.ui.indexPage_ui.ledit_select.textChanged.connect(self.solt_select)
        self.ui.indexPage_ui.table_overview.itemSelectionChanged.connect(self.solt_update_current_data)

    # 方法
    # ///////////////////////////////////////////////////////////////

    # 按钮动作定义
    # ///////////////////////////////////////////////////////////////
    def solt_read(self) -> None:
        if self.flag_threadRunning:
            notice = Notice()
            notice.exec("提示", "请等待上一进程结束后重试")
        else:
            if self.currentTableRow:
                self.newtask = FileReadTask()
                self.newtask.setPath(self.currentFilePath)
                self.newtask.moveToThread(self.fileReadThread)
                self.newtask.sig_read_line.connect(self.ui.readPage_ui.tedit_view.c_insertWithColor)
                self.newtask.sig_read_compleat.connect(self.solt_delete_task)
                self.fileReadThread.started.connect(self.newtask.readfile)
                self.solt_readpage_setmsg()
                self.fileReadThread.start()
                self.flag_threadRunning = True
            else:
                notice = Notice()
                notice.exec("提示", "未选择任何文件")

    def solt_export(self) -> None:
        # TODO: 临时数据文件导出功能
        if self.currentFilePath is not None:
            filter: str = ""
            if self.currentComboIndex == 0:
                filter = "文本文件(*.txt);;网页文件(*.html)"
            elif self.currentComboIndex == 1:
                filter = "文本文件(*.txt);;Excel文件(*.xlsx)"
            path, _ = QFileDialog.getSaveFileName(None, "选择保存路径", filter=filter)
            ftype = path.rsplit(".", 1)[-1].lower()
            if ftype in ["txt", "html"]:
                copyfile(self.currentFilePath, path)
            else:
                File.createExcelFile(path, {"data": eval(File.read(self.currentFilePath))})
        else:
            Notice().exec("提示", "未选择任何临时数据")

    def solt_delete(self) -> None:
        if self.currentTableRow:
            dQuestion = Question()
            if dQuestion.exec("请确认", "是否删除选中项", titleType="warn"):
                path = File.path(SysPath.CACHE, self.INDEX_TO_DAT_FILE_NAME[self.currentComboIndex])
                lst = File.read_opt(path, DataType.LIST, comment_mark="#")
                for rowIndex in self.currentTableRow:
                    fpath = File.path(SysPath.TEMP, self.INDEX_TO_FILE_DIR_PATH[self.currentComboIndex], self.ui.indexPage_ui.table_overview.item(rowIndex, 0).text())
                    File.delete(fpath)
                    lst.pop(rowIndex)
                File.writeWithComment(path, "\n".join([str(item) for item in lst]), top_comment=Define.FILE_DAT_TOP_COMMENT[self.INDEX_TO_DAT_FILE_NAME[self.currentComboIndex]])
                self.solt_flush()
        else:
            dNotice = Notice()
            dNotice.exec("提示", "未选择任何文件")

    def solt_flush(self) -> None:
        self.solt_change_datasource(self.ui.indexPage_ui.combo_chooseView.currentIndex())

    def solt_readpage_setmsg(self) -> None:
        data = self.ui.indexPage_ui.table_overview.c_getData(onlySelectedRows=True)[0]
        textedit = self.ui.readPage_ui.tedit_view
        textedit.clear()
        textedit.c_appendWithColor("存档信息:", after="\n")
        for i in range(self.INDEX_TO_TABLE_HEADDER[self.currentComboIndex].__len__()):
            textedit.c_insertWithColor(self.INDEX_TO_TABLE_HEADDER[self.currentComboIndex][i])
            textedit.c_appendWithColor(data[i], ctype="info", pre=": ")
        textedit.c_appendWithColor("--------------------以下是文件内容--------------------", pre="\n", after="\n")
        self.ui.pages.setCurrentWidget(self.ui.readPage)

    # 信号动作定义
    # ///////////////////////////////////////////////////////////////
    def solt_change_datasource(self, index) -> None:
        self.currentComboIndex = index
        table = self.ui.indexPage_ui.table_overview
        data = File.read_opt(File.path(SysPath.CACHE, self.INDEX_TO_DAT_FILE_NAME[index]), DataType.LIST, comment_mark="#")

        table.clear()
        table.c_setHeader(self.INDEX_TO_TABLE_HEADDER[index])

        dataappend = []
        filecount = 0
        bytecount = 0
        for row in data:
            lst = eval(row)
            filecount += 1
            nbyte = int(lst[self.INDEX_TO_FILE_SIZE_COL[index]])
            bytecount += nbyte
            lst[self.INDEX_TO_FILE_SIZE_COL[index]] = File.fileSizeConversion(nbyte)
            dataappend.append(lst)

        table.c_addRows(dataappend)
        self.ui.indexPage_ui.ledit_fileCount.setText(str(filecount))
        self.ui.indexPage_ui.ledit_sizeCount.setText(File.fileSizeConversion(bytecount))

    def solt_select(self, text) -> None:
        if text == "":
            self.ui.indexPage_ui.table_overview.c_setAllHidden(False)
        else:
            self.ui.indexPage_ui.table_overview.c_search(text)

    def solt_delete_task(self) -> None:
        self.newtask.deleteLater()
        self.fileReadThread.quit()
        self.flag_threadRunning = False

    def solt_update_current_data(self) -> None:
        self.currentTableRow = []
        self.currentFilePath = None
        current = self.ui.indexPage_ui.table_overview.selectedItems()
        if current:
            for item in current:
                if item.row() not in self.currentTableRow: self.currentTableRow.append(item.row())
            self.currentFilePath = File.path(SysPath.TEMP, self.INDEX_TO_FILE_DIR_PATH[self.currentComboIndex], current[0].text())
        self.currentTableRow.sort(reverse=True)


class FileReadTask(QObject):
    sig_read_compleat = Signal()
    sig_read_line = Signal(object)

    path = None

    def __init__(self) -> None:
        super().__init__()

    def readfile(self) -> str:
        file = QFile(self.path)
        file.open(QIODevice.OpenModeFlag.ReadOnly)
        text = file.readAll().toStdString()
        self.sig_read_line.emit(text)
        file.close()
        self.sig_read_compleat.emit()

    def setPath(self, path) -> None:
        self.path = path
