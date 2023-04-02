import random
from time import sleep

from requests import Response

from core.data import Parse, Request
from core.sys import Configuration, DataType, File, Settings, SysPath
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
        self.btn_connect()
        self.signal_connect()

    def btn_connect(self) -> None:
        # 按钮界面
        self.ui.page_btn_ui.btn_run.clicked.connect(self.btn_to_run_page)

        # 运行界面
        self.ui.page_run_ui.btn_back.clicked.connect(self.btn_back)
        self.ui.page_run_ui.btn_run.clicked.connect(self.btn_run)

    def signal_connect(self) -> None:
        self.ui.page_run_ui.combo_config_select.sig_current_text_changed.connect(self.current_config_name_changed)
        self.runner.sig_msg_append.connect(self.ui.page_run_ui.tedit_msg_out.append_with_color)
        self.runner.sig_msg_insert.connect(self.ui.page_run_ui.tedit_msg_out.insert_with_color)
        self.sig_run.connect(self.runner.run)
        self.runner.sig_sleep.connect(self.thread_sleep)
        self.runner.sig_stop.connect(self.thread_stop)

    # 按钮事件定义
    # ///////////////////////////////////////////////////////////////
    # 按钮界面
    def btn_to_run_page(self) -> None:
        datas = File.read_opt(File.path(SysPath.CACHE, "local_configuration.dat"), DataType.LIST, "#")
        for item in datas:
            data = eval(item)
            self.runner.config_file_paths[data[0]] = data[1]
        self.ui.page_run_ui.combo_config_select.clear()
        self.ui.page_run_ui.combo_config_select.addItems([eval(data)[0] for data in datas])
        self.ui.page_run_ui.tedit_msg_out.clear()
        self.ui.page_run_ui.tedit_msg_out.append_with_color("提示", "info", "[", "]: 选择配置文件以启动运行")
        self.ui.pages.setCurrentWidget(self.ui.page_run)

    # 运行界面
    def btn_back(self) -> None:
        self.thread_stop()
        self.ui.pages.setCurrentWidget(self.ui.page_btn)

    def btn_run(self) -> None:
        self.thread_run()
        self.sig_run.emit()

    # 信号事件定义
    # ///////////////////////////////////////////////////////////////
    def current_config_name_changed(self, current_name) -> None:
        self.runner.current_config_name = current_name

    def thread_sleep(self, time) -> None:
        self._thread.sleep(time)

    # 中间方法
    # ///////////////////////////////////////////////////////////////
    def thread_run(self) -> None:
        if self._thread.isRunning():
            return
        self._thread.start()

    def thread_stop(self) -> None:
        if not self._thread.isRunning():
            return
        self._thread.quit()
        self._thread.wait()


class Runner(QObject):
    sig_msg_insert = Signal(object, object, object, object)
    sig_msg_append = Signal(object, object, object, object)
    sig_sleep = Signal(object)
    sig_stop = Signal()

    config_file_paths: dict = {}
    current_config_name: str = ""

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        config = Configuration(self.config_file_paths[self.current_config_name])
        settings = Settings()
        data: list = self.do_request(config, settings)
        data = self.do_parse(data, config)
        self.do_data_save(data, config)
        self.sig_stop.emit()

    def do_request(self, config: Configuration, settings: Settings) -> list:
        sleep_set = settings.sleep
        responses: list = []
        self.sig_msg_append.emit("Reading Start\n", "info", None, None)
        count = config.urls.__len__()
        num = 1
        for url in config.urls:
            schedule = F"{num}/{count}".center(13, " ")
            num += 1
            self.sig_msg_insert.emit(F"Reading page NO. = {schedule} ", None, None, None)
            try:
                response = Request.run(config.request_method, url, config.headers, config.data_form, config.cookies, config.verify, config.timeout)
                responses.append(response)
                self.sig_msg_insert.emit("successfully", "success", None, "  ")
                self.sig_msg_insert.emit(F"{response.status_code}", "info", "Status: ", "  ")
                self.sig_msg_append.emit(F"{response.url}", "info", "url = ", None)
            except Exception as e:
                self.sig_msg_insert.emit("error", "error", None, "  ")
                self.sig_msg_insert.emit(F"{response.status_code}", "info", "Status: ", "  ")
                self.sig_msg_append.emit(F"{e}", "info", "msg = ", None)
            if sleep_set["enable"]: sleep(self.randomSleepTime(sleep_set["time"]))
        self.sig_msg_append.emit("\nReading Complete\n", "info", None, None)
        return responses

    def do_parse(self, responses: list, config: Configuration) -> list:
        return_list: list = []
        func: dict = {"bs4": Parse.bs4_select, "re": Parse.re_findall, "xpath": Parse.lxml_xpath}
        self.sig_msg_append.emit("Data Parsing Start\n", "info", None, None)
        if config.data_type == "text":
            data: list = []
            cols: list = []
            response: Response
            self.sig_msg_insert.emit("info", "info", "[", "] analytic response list...  ")
            for response in responses:
                response.encoding = config.encoding
                data.append(response.text)
                response.close()
            self.sig_msg_append.emit("complete", "success", None, None)
            if config.pretreatment_enable and config.pretreatment_setting:
                self.sig_msg_insert.emit("info", "info", "[", "] data pretreatment...  ")
                data = Parse.pretreatment(data, config.pretreatment_setting["tag_name"], config.pretreatment_setting["attrs"])
                self.sig_msg_append.emit("complete\n", "success", None, None)
            if config.parser_enable and config.parser_text_setting:
                count = config.parser_text_setting.keys().__len__()
                num = 1
                for key, value in config.parser_text_setting.items():
                    schedule = F"{num}/{count}".center(13, " ")
                    num += 1
                    self.sig_msg_insert.emit(F"Parsing col NO. = {schedule} ", None, None, None)
                    col = func[key.split("@")[1]](data, value["selector"], value["index"], value["sep"])
                    cols.append(col)
                    self.sig_msg_append.emit("complete", "success", None, None)
            self.sig_msg_insert.emit("info", "info", "\n[", "] merge columns...  ")
            if cols:
                return_list = [[item] for item in cols[0]]
                for i in range(1, cols.__len__()):
                    k = 0
                    for item in return_list:
                        item.append(cols[i][k])
                        k += 1
            elif data:
                return_list = [[item] for item in data]
            self.sig_msg_append.emit("complete", "success", None, None)
            return return_list
        elif config.data_type == "bin":
            # TODO: 二进制数据解析
            pass
        self.sig_msg_append.emit("\nData Parseing Complete\n", "info", None, None)

    def do_data_save(self, data: list, config: Configuration):
        if config.file_save_enable:
            self.sig_msg_append.emit("\nStart File Output\n", "info", None, None)
            if config.data_type == "text":
                # TODO: 不同文件格式的保存
                file_name = config.file_save_setting["text"]["file_name"]
                path = File.path(SysPath.OUTPUT, file_name)
                with open(path, "w", encoding="UTF-8") as file:
                    lines = ["::".join(item) + "\n" for item in data]
                    file.writelines(lines)
                self.sig_msg_append.emit(F"file successfully saved at {path}", "success", None, None)

    def randomSleepTime(self, timeset: float) -> float:
        """随机间隔时间生成器

        Returns:
            float: 返回随机时间
        """
        if random.randint(0, 1) == 0:
            t = timeset + (float(random.randint(0, 50)) / 100)
        else:
            t = timeset - (float(random.randint(0, 50)) / 100)
        return t
