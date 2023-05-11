from .Ui_TempviewPage import Ui_TempviewPage
from core.sys.file import File, SysPath, DataType


class Func_TempviewPage:
    ui: Ui_TempviewPage

    INDEX_TO_FILE_DIR_PATH = {0: "requestout", 1: "parseout"}
    INDEX_TO_DAT_FILE_NAME = {0: "temp_request.dat", 1: "temp_parse.dat"}
    INDEX_TO_TABLE_HEADDER = {0: ["文件名", "请求域名", "请求方式", "时间", "状态码", "编码", "文件大小"], 1: ["文件名", "数据类型", "时间", "数据来源", "是否输出", "输出文件", "文件大小"]}
    INDEX_TO_FILE_SIZE_COL = {0: 6, 1: 6}

    def __init__(self, ui) -> None:
        self.ui = ui
        self._btnConnect()
        self._signalConnect()

    def _btnConnect(self) -> None:
        self.ui.indexPage_ui.btn_read.clicked.connect(self.solt_read)
        self.ui.indexPage_ui.btn_export.clicked.connect(self.solt_export)
        self.ui.indexPage_ui.btn_delete.clicked.connect(self.solt_delete)
        self.ui.indexPage_ui.btn_flush.clicked.connect(self.solt_flush)
        self.ui.indexPage_ui.btn_clearSelect.clicked.connect(self.ui.indexPage_ui.ledit_select.clear)

    def _signalConnect(self) -> None:
        self.ui.indexPage_ui.combo_chooseView.currentIndexChanged.connect(self.solt_change_datasource)
        self.ui.indexPage_ui.ledit_select.textChanged.connect(self.solt_select)

    # 方法
    # ///////////////////////////////////////////////////////////////

    # 按钮动作定义
    # ///////////////////////////////////////////////////////////////
    def solt_read(self) -> None:
        pass

    def solt_export(self) -> None:
        pass

    def solt_delete(self) -> None:
        pass

    def solt_flush(self) -> None:
        self.solt_change_datasource(self.ui.indexPage_ui.combo_chooseView.currentIndex())

    # 信号动作定义
    # ///////////////////////////////////////////////////////////////
    def solt_change_datasource(self, index) -> None:
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
