from .Ui_CloudPage import Ui_CloudPage
from core.sys.cloud import getConfigList, getConfig, updateShareState, deleteConfig, updateLocalAccountState
from core.sys.globalv import Globalv, GlvKey
from core.sys.accountstate import AccountState
from ui.dialog import Notice, ConfigShareMsgInput, Question
from ui.widgets import PushButton


class Func_CloudPage:
    ui: Ui_CloudPage

    accountState: AccountState
    editPageMode: str = ""

    def __init__(self, ui: Ui_CloudPage) -> None:
        self.ui = ui
        self.accountState = Globalv.get(GlvKey.ACCOUNT_STATE)
        self._btnConnect()
        self._sigConnect()

    def _btnConnect(self) -> None:
        self.ui.overviewPage_ui.btn_read.clicked.connect(lambda: self.ui.pages.setCurrentIndex(1))
        self.ui.readPage_ui.btn_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(0))
        self.ui.overviewPage_ui.btn_clear.clicked.connect(self.ui.overviewPage_ui.ledit_fillter.clear)
        self.ui.overviewPage_ui.btn_delete.clicked.connect(self.solt_delete_config)

    def _sigConnect(self) -> None:
        self.ui.overviewPage_ui.combo_select.currentIndexChanged.connect(self.flushOverviewPage)
        self.ui.overviewPage_ui.ledit_fillter.textChanged.connect(self.solt_search)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def flushOverviewPage(self) -> None:
        self.ui.overviewPage_ui.table_overview.clear()
        if self.accountState._isLoginSucceed:
            dic = {0: -1, 1: 0, 2: 1}
            resp = getConfigList(self.accountState._userId, dic[self.ui.overviewPage_ui.combo_select.currentIndex()])
            if resp["flag"]:
                datas = resp["data"]
                self.ui.overviewPage_ui.ledit_count.setText(F"{self.accountState._configSaveCount} / 80")
                rowIndex = 0
                for data in datas:
                    btnText = "共享该配置" if data["isShared"] == 0 else "取消共享"
                    btnType = "success" if data["isShared"] == 0 else "error"
                    btn = PushButton(None, btnText, type=btnType)
                    btn.setObjectName(F"{data['configId']}@{1 if data['isShared']==0 else 0}")
                    btn.clicked.connect(self.solt_table_btns_operation)
                    self.ui.overviewPage_ui.table_overview.c_addRow(
                        [data["configName"], data["fileName"], "云端", data["uploadTime"], data["updateTime"], "私人" if data["isShared"] == 0 else "共享", data["host"], data["comment"], btn,
                         str(data["configId"])])
                    self.ui.overviewPage_ui.table_overview.c_setCellColor(rowIndex, 5, "info" if data["isShared"] == 0 else "success")
                    rowIndex += 1
            else:
                notice = Notice()
                notice.exec("错误", F"获取云端数据失败\n{resp['msg']}", "error")

    # 按钮响应槽
    # ///////////////////////////////////////////////////////////////
    def solt_table_btns_operation(self, objname: str) -> None:
        configId = int(objname.split("@")[0])
        setShare = int(objname.split("@")[1])
        form: dict = {"configId": configId, "setShared": setShare, "isFirstShare": True, "host": "", "doc": ""}

        flag_continue: bool = True
        question: Question = Question()
        rowIndex = self.ui.overviewPage_ui.table_overview.currentRow()

        if setShare == 1:
            data = getConfig(configId)["data"]
            if data["host"]:
                # 非初次共享,直接设置共享
                form["isFirstShare"] = False
                flag_continue = question.exec("请确认", "是否确定共享此配置\n将使用旧的域名以及说明文档\n可查看后进行修改")
            else:
                # 初次共享,弹窗提示设置host和说明文档
                smi = ConfigShareMsgInput()
                flag, host, doc = smi.exec()
                flag_continue = flag
                if flag:
                    form["host"] = host
                    form["doc"] = doc
                    self.ui.overviewPage_ui.table_overview.item(rowIndex, 6).setText(host)
        else:
            flag_continue = question.exec("请确认", "是否确定将此配置取消共享\n已保存的域名以及说明文档将被保留")

        if flag_continue:
            resp = updateShareState(form)
            if resp["flag"]:
                self.ui.overviewPage_ui.table_overview.c_setCellColor(rowIndex, 5, "success" if setShare else "info")
                self.ui.overviewPage_ui.table_overview.item(rowIndex, 5).setText("共享" if setShare else "私人")
                btn: PushButton = self.ui.overviewPage_ui.table_overview.cellWidget(rowIndex, 8)
                btn.setType("error" if setShare else "success")
                btn.setText("取消共享" if setShare else "共享该配置")
                btn.setObjectName(F"{configId}@0" if setShare else F"{configId}@1")
            else:
                notice = Notice()
                notice.exec("错误", F"更新分享状态出错\n{resp['msg']}")

    def solt_delete_config(self)->None:
        datas = self.ui.overviewPage_ui.table_overview.c_getData(onlyCol=[9], onlySelectedRows=True)
        if datas:
            if Question().exec("请确认", "是否确定删除选中的云端配置", "warn"):
                ids = " ".join([data[0] for data in datas])
                resp = deleteConfig({"configIds": ids, "userId": self.accountState._userId})
                if resp["flag"]:
                    self.ui.overviewPage_ui.table_overview.c_deleteSelectdRows()
                    self.ui.overviewPage_ui.ledit_count.setText(str(self.ui.overviewPage_ui.table_overview.rowCount()))
                    updateLocalAccountState()
                else:
                    Notice.exec("错误", F"配置删除失败\n{resp['msg']}")
        else:
            Notice().exec("提示", "未选择任何配置")

    # 信号响应槽
    # ///////////////////////////////////////////////////////////////
    def solt_search(self, text) -> None:
        if text == "":
            self.ui.overviewPage_ui.table_overview.c_setAllHidden(False)
        else:
            self.ui.overviewPage_ui.table_overview.c_search(text)
