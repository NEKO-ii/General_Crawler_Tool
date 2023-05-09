import random
from time import sleep

from requests import Response

from core.data.request import Request
from core.data.parse import Parse
from core.sys.configuration import Configuration
from core.sys.settings import Settings
from core.sys.file import DataType, File, SysPath
from core.support.tools import Tools
from core.static.define import Define
from ui.preload.imp_qt import QObject, QThread, Signal

from .Ui_StartPage import Ui_StartPage


class Func_StartPage(QObject):
    ui: Ui_StartPage
    sig_run = Signal()

    def __init__(self, ui: Ui_StartPage) -> None:
        super().__init__()
        self.ui = ui
        self._thread = QThread()
        self.runner = Runner()
        self.runner.moveToThread(self._thread)
        self._btnConnect()
        self._signalConnect()

    def _btnConnect(self) -> None:
        # 按钮界面
        self.ui.btnPage_ui.btn_run.clicked.connect(self.btn_to_run_page)

        # 运行界面
        self.ui.runPage_ui.btn_back.clicked.connect(self.btn_back)
        self.ui.runPage_ui.btn_run.clicked.connect(self.btn_run)

    def _signalConnect(self) -> None:
        self.ui.runPage_ui.combo_configSelector.sig_currentTextChanged.connect(self.current_config_name_changed)
        self.runner.sig_msgAppend.connect(self.ui.runPage_ui.tedit_msgOutput.c_appendWithColor)
        self.runner.sig_msgInsert.connect(self.ui.runPage_ui.tedit_msgOutput.c_insertWithColor)
        self.sig_run.connect(self.runner.run)
        self.runner.sig_sleep.connect(self.thread_sleep)
        self.runner.sig_stop.connect(self._threadStop)
        self._thread.finished.connect(self._thread.wait)

    # 按钮事件定义
    # ///////////////////////////////////////////////////////////////
    # 按钮界面
    def btn_to_run_page(self) -> None:
        datas = File.read_opt(File.path(SysPath.CACHE, "local_configuration.dat"), DataType.LIST, "#")
        for item in datas:
            data = eval(item)
            self.runner.configFilePaths[data[0]] = data[1]
        self.ui.runPage_ui.combo_configSelector.clear()
        self.ui.runPage_ui.combo_configSelector.addItems([eval(data)[0] for data in datas])
        self.ui.runPage_ui.tedit_msgOutput.clear()
        self.ui.runPage_ui.tedit_msgOutput.c_appendWithColor("提示", "info", "[", "]: 选择配置文件以启动运行")
        self.ui.pages.setCurrentWidget(self.ui.runPage)

    # 运行界面
    def btn_back(self) -> None:
        self._threadStop()
        self.ui.pages.setCurrentWidget(self.ui.btnPage)

    def btn_run(self) -> None:
        self.ui.runPage_ui.tedit_msgOutput.clear()
        self._threadRun()
        self.sig_run.emit()

    # 信号事件定义
    # ///////////////////////////////////////////////////////////////
    def current_config_name_changed(self, current_name) -> None:
        self.runner.currentConfigName = current_name

    def thread_sleep(self, time) -> None:
        self._thread.sleep(time)

    # 中间方法
    # ///////////////////////////////////////////////////////////////
    def _threadRun(self) -> None:
        if self._thread.isRunning():
            return
        self._thread.start()

    def _threadStop(self) -> None:
        if not self._thread.isRunning():
            return
        self._thread.quit()
        self._thread.wait()


class Runner(QObject):
    sig_msgInsert = Signal(object, object, object, object)
    sig_msgAppend = Signal(object, object, object, object)
    sig_sleep = Signal(object)
    sig_stop = Signal()

    configFilePaths: dict = {}
    currentConfigName: str = ""

    f_continue: bool

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        self.f_continue = True
        config = Configuration(self.configFilePaths[self.currentConfigName])
        settings = Settings()
        data: list = self._doRequest(config, settings)
        if self.f_continue: data = self._doParse(data, config)
        if self.f_continue: self._doDataSave(data, config)
        self.sig_stop.emit()

    def _doRequest(self, config: Configuration, settings: Settings) -> list:
        sleep_set = settings.sleep
        responses: list = []
        self.sig_msgAppend.emit("Start Reading\n", "info", None, None)
        count = config.urls.__len__()
        if count == 0:
            self.sig_msgAppend.emit("[stop] empty request url list, stop running.\n", "warn", None, None)
            self.f_continue = False
            return responses
        num = 1
        for url in config.urls:
            if url in Define.TYPE_ICON_LIST: continue
            schedule = F"{num}/{count}".center(13, " ")
            num += 1
            self.sig_msgInsert.emit(F"Reading page NO. = {schedule} ", None, None, None)
            try:
                response = None
                response = Request.run(config.request_method, url, config.headers, config.data_form, config.cookies, config.verify, config.timeout)
                responses.append(response)
                self.sig_msgInsert.emit("successfully", "success", None, "  ")
                self.sig_msgInsert.emit(F"{response.status_code}", "info", "Status: ", "  ")
                self.sig_msgAppend.emit(F"{response.url}", "info", "url = ", None)
            except Exception as e:
                self.sig_msgInsert.emit("error", "error", None, "  ")
                self.sig_msgInsert.emit(F"{response.status_code if response else 'none'}", "info", "Status: ", "  ")
                self.sig_msgAppend.emit(F"{e}", "info", "msg = ", None)
            if sleep_set["enable"]: sleep(self._randomSleepTime(sleep_set["time"]))
        self.sig_msgAppend.emit("\nReading Complete\n", "info", None, None)
        return responses

    def _doParse(self, responses: list, config: Configuration) -> list:
        returnList: list = []
        func: dict = {"bs4": Parse.bs4_select, "re": Parse.re_findall, "xpath": Parse.lxml_xpath}
        self.sig_msgAppend.emit("Start Data Parsing\n", "info", None, None)
        if not responses:
            self.f_continue = False
            self.sig_msgAppend.emit("[stop] empty response data, stop running.\n", "warn", None, None)
            return returnList
        if config.data_type == "text":
            data: list = []
            cols: list = []
            response: Response
            self.sig_msgInsert.emit("info", "info", "[", "] analytic response list...  ")
            for response in responses:
                response.encoding = config.encoding
                data.append(response.text)
                response.close()
            self.sig_msgAppend.emit("complete", "success", None, None)
            if config.pretreatment_enable and config.pretreatment_setting["tag_name"]:
                self.sig_msgInsert.emit("info", "info", "[", "] data pretreatment...  ")
                data = Parse.pretreatment(data, config.pretreatment_setting["tag_name"], config.pretreatment_setting["attrs"])
                self.sig_msgAppend.emit("complete\n", "success", None, None)
            if config.parser_enable and config.parser_text_setting:
                count = config.parser_text_setting.keys().__len__()
                num = 1
                for key, value in config.parser_text_setting.items():
                    schedule = F"{num}/{count}".center(13, " ")
                    num += 1
                    self.sig_msgInsert.emit(F"Parsing col NO. = {schedule} ", None, None, None)
                    col = func[key.split("@")[1]](data, value["selector"], value["index"], value["sep"])
                    cols.append(col)
                    self.sig_msgAppend.emit("complete", "success", None, None)
            self.sig_msgInsert.emit("info", "info", "\n[", "] merge columns...  ")
            if cols:
                returnList = [[item] for item in cols[0]]
                for i in range(1, cols.__len__()):
                    k = 0
                    for item in returnList:
                        item.append(cols[i][k])
                        k += 1
            elif data:
                returnList = [[item] for item in data]
            self.sig_msgAppend.emit("complete", "success", None, None)
            return returnList
        elif config.data_type == "bin":
            # TODO: 二进制数据解析
            pass
        self.sig_msgAppend.emit("\nData Parseing Complete\n", "info", None, None)

    def _doDataSave(self, data: list, config: Configuration):
        if config.file_save_enable:
            self.sig_msgAppend.emit("\nStart File Output\n", "info", None, None)
            savePath = File.path(SysPath.OUTPUT) if config.file_save_setting["save_path"] == "default" else config.file_save_setting["save_path"]
            if config.data_type == "text":
                FILE_EXTEND_NAME: dict = {"txt": ["txt"], "excel": ["xlsx", "xls"], "sql": ["sql"]}
                # TODO: SQL文件格式的保存
                if config.file_save_setting["text"]["page_cut_enable"]:
                    limit = config.file_save_setting["text"]["limit_per_page"]
                    datadict = Tools.toPagingDict(data, limit)
                else:
                    datadict = {"": data}
                fileName: str = config.file_save_setting["text"]["file_name"]
                fileType = config.file_save_setting["text"]["file_type"]
                if fileName.find(".") == -1 or fileName.split(".", 1)[-1] not in FILE_EXTEND_NAME[fileType]:
                    fileName = F"{fileName}.{FILE_EXTEND_NAME[fileType][0]}"
                if fileType == "txt":
                    for page in datadict:
                        path = File.pathJoin(savePath, File.insertFileName(fileName, -1, F" ({page})") if page else fileName)
                        with open(path, "w", encoding="UTF-8") as file:
                            lines = ["::".join(item) + "\n" for item in datadict[page]]
                            file.writelines(lines)
                        self.sig_msgAppend.emit(F"file successfully saved at {path}", "success", None, None)
                elif fileType == "excel":
                    if not config.file_save_setting["text"]["page_cut_enable"]: datadict["data"] = datadict.pop("")
                    path = File.pathJoin(savePath, fileName)
                    File.createExcelFile(path, datadict)
                    self.sig_msgAppend.emit(F"file successfully saved at {path}", "success", None, None)
                elif fileType == "sql":
                    pass

    def _randomSleepTime(self, timeset: float) -> float:
        """随机间隔时间生成器

        Returns:
            float: 返回随机时间
        """
        if random.randint(0, 1) == 0:
            t = timeset + (float(random.randint(0, 50)) / 100)
        else:
            t = timeset - (float(random.randint(0, 50)) / 100)
        return t
