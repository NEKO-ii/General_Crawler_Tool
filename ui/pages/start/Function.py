import random
from time import sleep

from requests import Response

from core.data.request import Request
from core.data.parse import Parse
from core.sys.configuration import Configuration
from core.sys.settings import Settings
from core.sys.file import DataType, File, SysPath
from core.support.tools import Tools
from core.support.coderunner import runjs, runpy
from core.static.define import Define
from ui.preload.imp_qt import QObject, QThread, Signal
from ui.dialog.Dialog_Select import Select
from ui.dialog.Notice import Notice
from .Ui_StartPage import Ui_StartPage


class Func_StartPage(QObject):
    ui: Ui_StartPage
    sig_run = Signal()

    flag_configLoad: bool = False

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
        self.ui.runPage_ui.btn_configSelector.clicked.connect(self.btn_config_select)

    def _signalConnect(self) -> None:
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
        self.flag_configLoad = False
        self.ui.runPage_ui.ledit_configShow.clear()
        self.ui.runPage_ui.tedit_msgOutput.clear()
        self.ui.runPage_ui.tedit_msgOutput.c_appendWithColor("提示", "info", "[", "]: 选择配置文件以启动运行")
        self.ui.pages.setCurrentWidget(self.ui.runPage)

    # 运行界面
    def btn_back(self) -> None:
        self._threadStop()
        self.ui.pages.setCurrentWidget(self.ui.btnPage)

    def btn_run(self) -> None:
        if self.flag_configLoad:
            self.ui.runPage_ui.tedit_msgOutput.clear()
            self._threadRun()
            self.sig_run.emit()
        else:
            notice = Notice()
            notice.exec("提示", "未选择任何配置,无法启动")

    def btn_config_select(self) -> None:
        datas = File.read_opt(File.path(SysPath.CACHE, "local_configuration.dat"), DataType.LIST, "#")
        datas = [eval(item) for item in datas]
        data = []
        for row in datas:
            if row[3] not in Define.LOCAL_CONF_STATE_TYPE["error"]:
                data.append(row)
        header = ["配置名", "文件路径", "更新时间", "标记", "备注"]
        select = Select()
        code, ret = select.exec(header, data)
        if code and ret:
            self.flag_configLoad = True
            self.runner.currentConfigPath = ret[0][1]
            self.ui.runPage_ui.ledit_configShow.setText(ret[0][0])
        else:
            self.flag_configLoad = False
            self.ui.runPage_ui.ledit_configShow.clear()

    # 信号事件定义
    # ///////////////////////////////////////////////////////////////

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

    currentConfigPath: str = ""
    currentRequTempFile: str = ""

    f_continue: bool

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        self.f_continue = True
        config = Configuration(self.currentConfigPath)
        settings = Settings()
        data: list = self._doRequest(config, settings)
        if self.f_continue: data = self._doParse(data, config)
        if self.f_continue: self._doDataSave(data, config)
        self.sig_stop.emit()

    def _doRequest(self, config: Configuration, settings: Settings) -> list:
        sleep_set = settings.sleep
        host = ""
        texts: list = []
        responses: list = []
        self.sig_msgAppend.emit("Start Reading\n", "info", None, None)
        count = config.urls.__len__()
        if count == 0:
            self.sig_msgAppend.emit("[stop] empty request url list, stop running.\n", "warn", None, None)
            self.f_continue = False
            return responses
        # 数据表单构建
        func = {"py": runpy, "js": runjs}
        dataform: dict = config.data_form
        for key in config.data_form_script:
            stype = key.split("@")[0]
            path = config.data_form_script[key]["path"]
            args = config.data_form_script[key]["args"]
            flag, data, msg = func[stype](path, args)
            if flag: dataform.update(data)
        num = 1
        for url in config.urls:
            if url in Define.TYPE_ICON_LIST: continue
            schedule = F"{num}/{count}".center(13, " ")
            num += 1
            self.sig_msgInsert.emit(F"Reading page NO. = {schedule} ", None, None, None)
            try:
                # print(json.dumps(dataform, indent=2))
                response = None
                response = Request.run(config.request_method, url, config.headers, dataform, config.cookies, config.verify, config.timeout)
                response.encoding = config.encoding
                host = response.request.headers["host"]
                texts.append(response.text)
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
        fname = F"request_{Tools.timestamp()}.txt"
        self.currentRequTempFile = fname
        path = File.path(SysPath.TEMP, "requestout", fname)
        File.write(path, "\n".join(texts))
        File.write(File.path(SysPath.CACHE, "temp_request.dat"), str([fname, host, config.request_method, Tools.datetime(), str(response.status_code), config.encoding, str(File.getSize(path))]) + "\n", mode="a")
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
            fname = F"parse_{Tools.timestamp()}.txt"
            path = File.path(SysPath.TEMP, "parseout", fname)
            data = "[\n"
            index = -1
            length = len(returnList)
            for row in returnList:
                index += 1
                data = data + F"{str(row)},\n" if index < length else data + F"{str(row)}\n"
            data = data + "]"
            File.write(path, data)
            File.write(
                File.path(SysPath.CACHE, "temp_parse.dat"),
                str([fname, config.data_type, Tools.datetime(), self.currentRequTempFile, "true" if config.file_save_enable else "false", config.file_save_setting["text"]["file_name"],
                     str(File.getSize(path))]) + "\n",
                mode="a")
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
