from PySide6.QtCore import Qt

from core.support.tools import Tools
from core.sys.accountstate import AccountState
from core.sys.cloud import (deleteConfig, getConfigContent, getConfigDoc, getConfigInfo, getConfigList, updateConfig, updateLocalAccountState, updateShareState, getConfigFileList, downloadConfig)
from core.sys.globalv import Globalv, GlvKey
from core.sys.file import File, SysPath
from ui.dialog import ConfigShareMsgInput, Message, Notice, Question
from ui.widgets import PushButton

from .Ui_CloudPage import Ui_CloudPage


class Func_CloudPage:
    ui: Ui_CloudPage

    accountState: AccountState
    editingRowIndex: int = None
    oldData: dict = None
    flag_inReadPage: bool = False
    flag_currentChanged: bool = False
    flag_jsonChanged: bool = False
    flag_docChanged: bool = False
    flag_infoChanged: bool = False

    def __init__(self, ui: Ui_CloudPage) -> None:
        self.ui = ui
        self.accountState = Globalv.get(GlvKey.ACCOUNT_STATE)
        self._btnConnect()
        self._sigConnect()
        self.message = Message()

    def _btnConnect(self) -> None:
        self.ui.overviewPage_ui.btn_read.clicked.connect(self.solt_read)
        self.ui.readPage_ui.btn_edit.clicked.connect(self.solt_edit)
        self.ui.readPage_ui.btn_reject.clicked.connect(self.solt_reject)
        self.ui.readPage_ui.btn_check.clicked.connect(self.readPageDataCheck)
        self.ui.readPage_ui.btn_back.clicked.connect(self.solt_back)
        self.ui.readPage_ui.btn_save.clicked.connect(self.solt_save)
        self.ui.readPage_ui.btn_stateChange.clicked.connect(self.solt_table_btns_operation)
        self.ui.overviewPage_ui.btn_download.clicked.connect(self.solt_download)
        self.ui.overviewPage_ui.btn_clear.clicked.connect(self.ui.overviewPage_ui.ledit_fillter.clear)
        self.ui.overviewPage_ui.btn_delete.clicked.connect(self.solt_delete_config)

    def _sigConnect(self) -> None:
        self.ui.overviewPage_ui.combo_select.currentIndexChanged.connect(self.flushOverviewPage)
        self.ui.overviewPage_ui.ledit_fillter.textChanged.connect(self.solt_search)
        self.ui.readPage_ui.combo_selectView.currentIndexChanged.connect(self.ui.readPage_ui.view.setCurrentIndex)
        self.ui.readPage_ui.tedit_doc.textChanged.connect(self.solt_doc_changed)
        self.ui.readPage_ui.tedit_json.textChanged.connect(self.solt_json_changed)
        self.ui.readPage_ui.ledit_configName.textChanged.connect(self.solt_info_changed)
        self.ui.readPage_ui.ledit_comment.textChanged.connect(self.solt_info_changed)
        self.ui.readPage_ui.ledit_fileName.textChanged.connect(self.solt_info_changed)
        self.ui.readPage_ui.ledit_host.textChanged.connect(self.solt_info_changed)

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

    def setReadOnly(self, flag: bool) -> None:
        page = self.ui.readPage_ui
        page.tedit_doc.setReadOnly(flag)
        page.tedit_json.setReadOnly(flag)
        page.ledit_configName.setReadOnly(flag)
        page.ledit_fileName.setReadOnly(flag)
        page.ledit_host.setReadOnly(flag)
        page.ledit_comment.setReadOnly(flag)
        page.btn_stateChange.setEnabled(not flag)
        fp: Qt.FocusPolicy
        ss: str
        if flag:
            fp = Qt.FocusPolicy.NoFocus
            ss = "color: #aaaabb;"
            page.btn_reject.hide()
            page.btn_check.hide()
            page.btn_save.hide()
            page.btn_edit.show()
        else:
            fp = Qt.FocusPolicy.ClickFocus
            ss = "color: #568af2;"
            page.btn_reject.show()
            page.btn_check.show()
            page.btn_save.show()
            page.btn_edit.hide()
        page.ledit_configName.setFocusPolicy(fp)
        page.ledit_fileName.setFocusPolicy(fp)
        page.ledit_host.setFocusPolicy(fp)
        page.ledit_comment.setFocusPolicy(fp)
        page.lb_configName.setStyleSheet(ss)
        page.lb_fileName.setStyleSheet(ss)
        page.lb_host.setStyleSheet(ss)
        page.lb_comment.setStyleSheet(ss)

    def getCurrentRowIndex(self, mode: str = "first") -> int | list[int]:
        """获取表格控件当前选中行

        Args:
            mode (str, optional): 模式[first:只返回选中的第一行的索引, all:返回索引列表]

        Returns:
            int | list[int]: 未选中任何内容时返回-1
        """
        indexes = self.ui.overviewPage_ui.table_overview.selectedIndexes()
        if indexes:
            if mode == "first":
                return indexes[0].row()
            elif mode == "all":
                selectedRowIndexes: list = []
                for index in indexes:
                    row = index.row()
                    if row not in selectedRowIndexes:
                        selectedRowIndexes.append(row)
                return selectedRowIndexes
        else:
            return -1

    def readPageDataSet(self, data: dict) -> None:
        self.oldData = data
        page = self.ui.readPage_ui
        configId = str(data["configId"])
        isShared = data["isShared"]
        page.ledit_configId.setText(configId)
        page.ledit_configName.setText(data["configName"])
        page.ledit_fileName.setText(data["fileName"])
        page.ledit_comment.setText(data["comment"])
        page.ledit_host.setText(data["host"])
        page.ledit_uploadTime.setText(data["uploadTime"])
        page.ledit_updateTime.setText(data["updateTime"])
        page.ledit_state.setText("共享" if isShared == 1 else "私人")
        page.ledit_state.setColor("success" if isShared == 1 else "info")
        page.btn_stateChange.setText("取消共享" if isShared == 1 else "共享此配置")
        page.btn_stateChange.setType("error" if isShared == 1 else "success")
        page.btn_stateChange.setObjectName(F"{configId}@0" if isShared == 1 else F"{configId}@1")
        docfname = data["docFileName"]
        if docfname is not None and docfname != "":
            resp = getConfigDoc(docfname)
            self.ui.readPage_ui.tedit_doc.setText(resp["data"])
        conffname = data["fileName"]
        resp = getConfigContent(self.accountState._userId, conffname)
        self.ui.readPage_ui.tedit_json.setText(resp["data"])

    def readPageDataGet(self) -> tuple[dict, str, str]:
        """获取阅读界面数据

        Returns:
            tuple[dict, str, str]: 返回元组(info, content, doc)
        """
        page = self.ui.readPage_ui
        info: dict = {
            "userId": self.oldData["userId"],
            "configId": int(page.ledit_configId.text()),
            "configName": page.ledit_configName.text().strip(),
            "fileName": page.ledit_fileName.text().strip(),
            "host": page.ledit_host.text().strip(),
            "comment": page.ledit_comment.text().strip(),
            "isShared": self.oldData["isShared"],
            "uploadTime": self.oldData["uploadTime"],
            "updateTime": Tools.datetime("%Y-%m-%d %H:%M:%S")
        }
        if self.oldData["docFileName"] is not None:
            info["docFileName"] = self.oldData["docFileName"]
        doc: str = page.tedit_doc.toPlainText().strip()
        content: str = page.tedit_json.toPlainText().strip()
        return (info, content, doc)

    def reSetChangeFlag(self) -> None:
        self.flag_currentChanged = False
        self.flag_jsonChanged = False
        self.flag_docChanged = False
        self.flag_infoChanged = False

    def readPageDataCheck(self) -> bool:
        page = self.ui.readPage_ui
        if page.ledit_configName.text().strip() == "":
            self.message.appendMsg("配置名不能为空", "error")
        filename = page.ledit_fileName.text().strip()
        if filename == "":
            self.message.appendMsg("文件名不能为空", "error")
        elif File.checkFileName(filename) is False:
            self.message.appendMsg("非法文件名", "error")
        elif filename.endswith(".json") is False:
            self.message.appendMsg("文件后缀名须使用json,已修改", "warn")
            page.ledit_fileName.setText(filename + ".json")
        else:
            files = getConfigFileList(self.accountState._userId)["data"]
            if filename != self.oldData["fileName"] and filename in files:
                self.message.appendMsg("云端已存在同名文件", "error")
        host = page.ledit_host.text().strip()
        if host.find("/") != -1:
            self.message.appendMsg("请使用根域名", "error")
        if self.oldData["isShared"]:
            if host == "":
                self.message.appendMsg("已分享配置的域名不能为空", "error")

        flag_show = False
        flag_pass = True
        if self.message.getMsgCount("error"):
            flag_show = True
            flag_pass = False
            page.lb_check.setText("数据错误")
            page.lb_check.setStyleSheet("color: red;")
        elif self.message.getMsgCount("warn"):
            flag_show = True
            page.lb_check.setText("数据可用")
            page.lb_check.setStyleSheet("color: orange;")
        else:
            page.lb_check.setText("数据可用")
            page.lb_check.setStyleSheet("color: green;")

        if flag_show:
            self.message.exec()

        return flag_pass

    # 按钮响应槽
    # ///////////////////////////////////////////////////////////////
    def solt_read(self) -> None:
        rowIndex = self.getCurrentRowIndex()
        if rowIndex == -1:
            Notice().exec("提示", "未选择任何配置")
        else:
            self.flag_inReadPage = True
            self.editingRowIndex = rowIndex
            self.setReadOnly(True)
            self.ui.readPage_ui.combo_selectView.setCurrentIndex(0)
            self.ui.pages.setCurrentIndex(1)

            configId = int(self.ui.overviewPage_ui.table_overview.item(rowIndex, 9).text())
            resp = getConfigInfo(configId)
            if resp["flag"]:
                self.readPageDataSet(resp["data"])
                self.reSetChangeFlag()
            else:
                Notice().exec("错误", F"获取配置信息失败\n{resp['msg']}", "error")

    def solt_edit(self) -> None:
        self.setReadOnly(False)

    def solt_reject(self) -> None:
        if self.flag_currentChanged:
            if Question().exec("警告", "是否放弃所有修改内容", "warn"):
                self.setReadOnly(True)
                self.readPageDataSet(self.oldData)
                self.reSetChangeFlag()
        else:
            self.setReadOnly(True)

    def solt_back(self) -> None:
        if self.flag_currentChanged:
            if Question().exec("警告", "修改内容未保存,返回总览界面将放弃所有修改\n是否继续?", "warn"):
                self.flag_inReadPage = False
                self.reSetChangeFlag()
                self.ui.pages.setCurrentIndex(0)
        else:
            self.flag_inReadPage = False
            self.ui.pages.setCurrentIndex(0)

    def solt_save(self) -> None:
        # 检查
        # 修改的文件名重名问题
        if self.flag_currentChanged:
            if self.readPageDataCheck():
                requ: dict = {}
                keys: list = []
                info, content, doc = self.readPageDataGet()
                requ["fileNameChanged"] = False if info["fileName"] == self.oldData["fileName"] else True
                requ["oldFileName"] = self.oldData["fileName"]
                requ["configId"] = info["configId"]
                requ["userId"] = info["userId"]
                if self.flag_infoChanged:
                    keys.append("info")
                    requ["info"] = str(info)
                if self.flag_jsonChanged:
                    keys.append("content")
                    requ["content"] = content
                if self.flag_docChanged:
                    keys.append("doc")
                    requ["doc"] = doc
                requ["keys"] = " ".join(keys)
                resp = updateConfig(requ)
                if resp["flag"]:
                    self.flushOverviewPage()
                    self.ui.pages.setCurrentIndex(0)
                else:
                    Notice().exec("错误", F"保存失败\n{resp['msg']}", "error")
        else:
            Notice().exec("提示", "未修改任何数据,无需保存")

    def solt_table_btns_operation(self, objname: str) -> None:
        configId = int(objname.split("@")[0])
        setShare = int(objname.split("@")[1])
        form: dict = {"configId": configId, "setShared": setShare, "host": "", "doc": ""}

        flag_continue: bool = True
        question: Question = Question()
        rowIndex = self.ui.overviewPage_ui.table_overview.currentRow()

        if setShare == 1:
            data = getConfigInfo(configId)["data"]
            smi = ConfigShareMsgInput()
            docfname = data["docFileName"]
            smi.ledit_host.setText(data["host"])
            if docfname is not None and docfname != "":
                doc = getConfigDoc(docfname)["data"]
                smi.tedit_doc.setText(doc)
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
                if self.flag_inReadPage:
                    self.oldData["isShared"] = setShare
                    self.ui.readPage_ui.ledit_host.setText(host)
                    self.ui.readPage_ui.ledit_state.setText("共享" if setShare else "私人")
                    self.ui.readPage_ui.ledit_state.setColor("success" if setShare else "info")
                    self.ui.readPage_ui.btn_stateChange.setType("error" if setShare else "success")
                    self.ui.readPage_ui.btn_stateChange.setText("取消共享" if setShare else "共享该配置")
                    self.ui.readPage_ui.btn_stateChange.setObjectName(F"{configId}@0" if setShare else F"{configId}@1")
            else:
                notice = Notice()
                notice.exec("错误", F"更新分享状态出错\n{resp['msg']}")

    def solt_delete_config(self) -> None:
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

    def solt_download(self) -> None:
        inds = self.getCurrentRowIndex("all")
        if inds != -1:
            if Question().exec("请确认", F"是否下载选中的配置(共{len(inds)}项)") is False: return
            configIds: str = " ".join([self.ui.overviewPage_ui.table_overview.item(rid, 9).text() for rid in inds])
            form = {"configIds": configIds}
            resp = downloadConfig(form)
            if resp["flag"]:
                fileNames = resp["data"]["fileNames"]
                fileInfos = resp["data"]["fileInfos"]
                fileContents = resp["data"]["fileContents"]
                cacheAppend = []

                for filename in fileNames:
                    info = fileInfos[filename]
                    content = fileContents[filename]

                    path = File.path(SysPath.CONFIGURATION, filename)
                    if File.isFileExists(path):
                        self.message.appendMsg(F"本地配置文件已存在: {path}", "error")
                        continue
                    File.write(path, content)

                    cache = []
                    cache.append(info["configName"])
                    cache.append(path)
                    cache.append(info["updateTime"])
                    cache.append("U")
                    cache.append(info["comment"])
                    cacheAppend.append(str(cache))

                    self.message.appendMsg(F"下载成功: {info['configName']}", "success")

                File.write(File.path(SysPath.CACHE, "local_configuration.dat"), "\n".join(cacheAppend), "a")
                if self.message.isEmptyMsg() is False:
                    self.message.exec()
            else:
                Notice().exec("错误", F"配置下载失败\n{resp['msg']}", "error")
        else:
            Notice().exec("提示", "未选择任何配置")

    # 信号响应槽
    # ///////////////////////////////////////////////////////////////
    def solt_search(self, text) -> None:
        if text == "":
            self.ui.overviewPage_ui.table_overview.c_setAllHidden(False)
        else:
            self.ui.overviewPage_ui.table_overview.c_search(text)

    def solt_json_changed(self) -> None:
        self.flag_currentChanged = True
        self.flag_jsonChanged = True

    def solt_doc_changed(self) -> None:
        self.flag_currentChanged = True
        self.flag_docChanged = True

    def solt_info_changed(self) -> None:
        self.flag_currentChanged = True
        self.flag_infoChanged = True
