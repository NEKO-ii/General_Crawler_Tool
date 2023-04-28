from copy import deepcopy
from json import loads, dumps

from core.static import Define
from core.support import MsgType, Tools, console_printer
from core.sys import DataType, File, SysPath, Globalv, GlvKey, Themes
from ui.preload.imp_qt import QFileDialog, QUrl
from ui.dialog import Dialog_ConfigMessageInput, Question, Notice, Inputer
from ui.widgets import ComboBox

from .Ui_ConfigurationPage import Ui_ConfigurationPage


class Func_ConfigPage:
    ui: Ui_ConfigurationPage

    editPageMode: str = None  # 当前配置编辑页面所处的功能模式,新建配置时为:new,编辑配置时为:edit
    editData: dict = None
    editFilePath: str = None
    overviewTableEditRowIndex: int = None

    def __init__(self, ui: Ui_ConfigurationPage) -> None:
        self.themes: Themes = Globalv.get(GlvKey.THEMES)
        self.ui = ui
        self._btnConnect()
        self._signalConnect()
        self._createDialog()

    # 按钮事件链接
    # ///////////////////////////////////////////////////////////////
    def _btnConnect(self) -> None:
        """按钮事件链接"""
        # 配置总览页面
        self.ui.overviewPage_ui.btn_newConfig.clicked.connect(self.btn_new_config)
        self.ui.overviewPage_ui.btn_import.clicked.connect(self.btn_import_config)
        self.ui.overviewPage_ui.btn_edit.clicked.connect(self.btn_edit_config)
        self.ui.overviewPage_ui.btn_flush.clicked.connect(self.ov_table_overview_flush)
        self.ui.overviewPage_ui.btn_delete.clicked.connect(self.btn_delete_config)

        # 配置编辑页面
        self.ui.editorPage_ui.btn_back.clicked.connect(self.btn_edit_back)
        self.ui.editorPage_ui.btn_default.clicked.connect(self.btn_edit_default)
        self.ui.editorPage_ui.btn_editInJson.clicked.connect(self.btn_edit_in_json)
        self.ui.editorPage_ui.btn_check.clicked.connect(self.btn_edit_check)
        self.ui.editorPage_ui.btn_save.clicked.connect(self.btn_edit_config_save)
        self.ui.editorPage_ui.btn_chooseFile.clicked.connect(self.btn_edit_choose_file)
        self.ui.editorPage_ui.btn_urlSetConfirm.clicked.connect(self.btn_edit_url_set_confirm)
        self.ui.editorPage_ui.btn_dataSavePath.clicked.connect(self.btn_edit_choose_save_path)

        self.ui.editorPage_ui.btn_parameterAdd.clicked.connect(self.btns_add_items)
        self.ui.editorPage_ui.btn_urlView_add.clicked.connect(self.btns_add_items)
        self.ui.editorPage_ui.btn_headersParse.clicked.connect(self.btn_parse_headers)
        self.ui.editorPage_ui.btn_headersAdd.clicked.connect(self.btns_add_items)
        self.ui.editorPage_ui.btn_dataForm_add.clicked.connect(self.btns_add_items)
        self.ui.editorPage_ui.btn_dataForm_script_add.clicked.connect(self.btns_add_items)
        self.ui.editorPage_ui.btn_cookiesParse.clicked.connect(self.btn_parse_cookies)
        self.ui.editorPage_ui.btn_cookiesAdd.clicked.connect(self.btns_add_items)
        self.ui.editorPage_ui.btn_psetTextAdd.clicked.connect(self.btns_add_items)

        self.ui.editorPage_ui.btn_parameterDelete.clicked.connect(self.btns_delete_items)
        self.ui.editorPage_ui.btn_urlView_delete.clicked.connect(self.btns_delete_items)
        self.ui.editorPage_ui.btn_headersDelete.clicked.connect(self.btns_delete_items)
        self.ui.editorPage_ui.btn_dataForm_delete.clicked.connect(self.btns_delete_items)
        self.ui.editorPage_ui.btn_dataForm_script_delete.clicked.connect(self.btns_delete_items)
        self.ui.editorPage_ui.btn_cookiesDelete.clicked.connect(self.btns_delete_items)
        self.ui.editorPage_ui.btn_psetTextDelete.clicked.connect(self.btns_delete_items)

        # 配置编辑页面:JSON
        self.ui.jsonEditPage_ui.btn_back.clicked.connect(self.btn_json_back)
        self.ui.jsonEditPage_ui.btn_default.clicked.connect(self.btn_json_default)
        self.ui.jsonEditPage_ui.btn_confirm.clicked.connect(self.btn_json_confirm)

    def _signalConnect(self) -> None:
        """自定义信号槽链接"""
        # 配置总览页面
        self.ui.overviewPage_ui.table_overview.sig_open.connect(self.ov_table_overview_init_data)
        self.ui.overviewPage_ui.table_overview.sig_dataChanged.connect(self.ov_table_overview_data_changed)
        self.ui.overviewPage_ui.table_overview.sig_flush.connect(self.ov_table_overview_flush)

        # 配置编辑页面
        self.ui.editorPage_ui.combo_dataType.sig_currentIndexChanged.connect(self.ed_combo_data_type_index_changed)
        self.ui.editorPage_ui.combo_urlSource.sig_currentIndexChanged.connect(self.ed_combo_url_source_index_changed)
        self.ui.editorPage_ui.combo_dataSavePath.sig_currentIndexChanged.connect(self.ed_combo_save_path_index_changed)

        # 配置编辑页面:JSON

    def _createDialog(self) -> None:
        """创建对话框"""
        self.dialog_configSaveMsgInput = Dialog_ConfigMessageInput()
        self.question = Question()
        self.notice = Notice()
        self.inputer = Inputer()

    # 函数定义
    # ///////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////
    def name(self) -> None:
        pass

    def btns_add_items(self, obj_name: str) -> None:
        """给按钮对应的列表或表格添加一行"""
        if obj_name == "btn_parameter_add": self.ui.editorPage_ui.table_parameter.c_addRow()
        if obj_name == "btn_url_view_add":
            self.ui.editorPage_ui.list_urlView.c_addRows(["new url"])
            self.ui.editorPage_ui.ledit_urlView_count.setText(str(self.ui.editorPage_ui.list_urlView.count()))
        if obj_name == "btn_headers_add": self.ui.editorPage_ui.table_headers.c_addRow()
        if obj_name == "btn_data_form_add": self.ui.editorPage_ui.table_dataForm.c_addRow()
        if obj_name == "btn_data_form_script_add": self.ui.editorPage_ui.table_dataForm_script.c_addRow()
        if obj_name == "btn_cookies_add": self.ui.editorPage_ui.table_cookies.c_addRow()
        cbox = ComboBox(scrollParent=self.ui.editorPage_ui.table_psetText)
        cbox.addItems(["RE", "BS4", "XPATH"])
        cbox.setCurrentText("RE")
        if obj_name == "btn_pset_text_add": self.ui.editorPage_ui.table_psetText.c_addRow([cbox])

    def btns_delete_items(self, obj_name: str) -> None:
        """删除按钮对应的列表或表格的所有选中行"""
        if obj_name == "btn_parameter_delete": self.ui.editorPage_ui.table_parameter.c_deleteSelectdRows()
        if obj_name == "btn_url_view_delete":
            self.ui.editorPage_ui.list_urlView.c_deleteSelectdRows()
            self.ui.editorPage_ui.ledit_urlView_count.setText(str(self.ui.editorPage_ui.list_urlView.count()))
        if obj_name == "btn_headers_delete": self.ui.editorPage_ui.table_headers.c_deleteSelectdRows()
        if obj_name == "btn_data_form_delete": self.ui.editorPage_ui.table_dataForm.c_deleteSelectdRows()
        if obj_name == "btn_data_form_script_delete": self.ui.editorPage_ui.table_dataForm_script.c_deleteSelectdRows()
        if obj_name == "btn_cookies_delete": self.ui.editorPage_ui.table_cookies.c_deleteSelectdRows()
        if obj_name == "btn_pset_text_delete": self.ui.editorPage_ui.table_psetText.c_deleteSelectdRows()

    # 配置总览页面
    # ///////////////////////////////////////////////////////////////
    def ov_table_overview_init_data(self) -> None:
        """初始化配置总览信息"""
        table = self.ui.overviewPage_ui.table_overview
        datas = File.read_opt(File.path(SysPath.CACHE, "local_configuration.dat"), DataType.LIST, "#")
        for data in datas:
            dataList = eval(data)
            table.c_addRow(dataList)
        rindex = 0
        for item in table.c_getData(onlyCol=[3]):
            if item != []:
                if item[0] in Define.LOCAL_CONF_STATE_TYPE["success"]: table.c_setCellColor(rindex, 3, "success")
                elif item[0] in Define.LOCAL_CONF_STATE_TYPE["error"]: table.c_setCellColor(rindex, 3, "error")
                elif item[0] in Define.LOCAL_CONF_STATE_TYPE["warning"]: table.c_setCellColor(rindex, 3, "warning")
            rindex += 1
        table.flag_initComplete = True

    def ov_table_overview_flush(self) -> None:
        """刷新配置总览信息"""
        table = self.ui.overviewPage_ui.table_overview
        table.flag_initComplete = False
        table.clear()
        datas = File.read_opt(File.path(SysPath.CACHE, "local_configuration.dat"), DataType.LIST, "#")
        for data in datas:
            dataList = eval(data)
            table.c_addRow(dataList)
        rindex = 0
        for item in table.c_getData(onlyCol=[3]):
            if item != []:
                if item[0] in Define.LOCAL_CONF_STATE_TYPE["success"]: table.c_setCellColor(rindex, 3, "success")
                elif item[0] in Define.LOCAL_CONF_STATE_TYPE["error"]: table.c_setCellColor(rindex, 3, "error")
                elif item[0] in Define.LOCAL_CONF_STATE_TYPE["warning"]: table.c_setCellColor(rindex, 3, "warning")
            rindex += 1
        table.flag_initComplete = True

    def ov_table_overview_data_changed(self, currentIndex: list) -> None:
        """表格数据变化后更新文件数据"""
        table = self.ui.overviewPage_ui.table_overview
        currentRow = currentIndex[0]
        currentCol = currentIndex[1]
        if currentRow: table.item(currentRow, 2).setText(Tools.datetime())
        data = table.c_getData()
        File.writeWithComment(File.path(SysPath.CACHE, "local_configuration.dat"), data, top_comment=Define.FILE_DAT_TOP_COMMENT["local_configuration"])
        if currentCol and currentCol == 3:
            text = table.item(currentRow, currentCol).text()
            if text in Define.LOCAL_CONF_STATE_TYPE["success"]: table.c_setCellColor(currentRow, currentCol, "success")
            elif text in Define.LOCAL_CONF_STATE_TYPE["error"]: table.c_setCellColor(currentRow, currentCol, "error")
            elif text in Define.LOCAL_CONF_STATE_TYPE["warning"]: table.c_setCellColor(currentRow, currentCol, "warning")
            else:
                table.item(currentRow, currentCol).setText("U")
                table.c_setCellColor(currentRow, currentCol, "warning")
                self.notice.exec("注意", "输入状态标识无效, 请参考提示\n已修改为未知状态:U", titleType="warning", msgType="info")

    def btn_new_config(self) -> None:
        """新建配置"""
        self.editPageMode = "new"
        defaultData: dict = loads(Define.FILE_DEFAULT_CONTENT["configuration"])
        self._editPageFormDataSet(defaultData)
        self.ui.pages.setCurrentWidget(self.ui.editorPage)

    def btn_import_config(self) -> None:
        """导入配置"""
        console_printer(MsgType.INFOMATION, "btn import config clicked")

    def btn_edit_config(self) -> None:
        """编辑配置"""
        self.editPageMode = "edit"
        table = self.ui.overviewPage_ui.table_overview
        selectedItems = table.selectedItems()
        if selectedItems:
            currentRow = selectedItems[0].row()
            self.overviewTableEditRowIndex = currentRow
            path = table.item(currentRow, 1).text()
            # print(path)
            if File.isFileExists(path):
                try:
                    self.editData = File.read_opt(path, DataType.DICTIONARY)
                    self.editFilePath = path
                    self._editPageFormDataSet(self.editData)
                    self.ui.pages.setCurrentWidget(self.ui.editorPage)
                except Exception as e:
                    console_printer(MsgType.ERROR, e)
                    table.item(currentRow, 3).setText(Define.LocalConfigState.N)
                    table.c_setCellColor(currentRow, 3, "error")
                    self.notice.exec("出现错误", "配置文件解析失败,文件内容格式可能出现错误", "error", "info")
            else:
                console_printer(MsgType.ERROR, "该配置JSON文件已被移动")
                table.item(currentRow, 3).setText(Define.LocalConfigState.FL)
                table.c_setCellColor(currentRow, 3, "error")
                self.notice.exec("出现错误", "文件路径不存在,该配置JSON文件可能已被移动或删除", "error", "info")
        else:
            self.notice.exec("注意", "未选择任何配置,请选择后进行编辑\n多选仅编辑第一个选中配置")

    def btn_delete_config(self) -> None:
        """删除配置"""
        table = self.ui.overviewPage_ui.table_overview
        if table.c_getCurrentIndex()[0]:
            if self.question.exec(title="是否确认删除", msg="删除配置会同时删除配置文件,若需保留请提前备份", msgType="warning"):
                for item in table.c_getData(onlyCol=[1], onlySelectedRows=True):
                    # print(item[0])
                    File.delete(item[0])
                table.c_deleteSelectdRows()
        else:
            self.notice.exec("提示", "未选中任何配置文件")

    # 配置编辑页面
    # ///////////////////////////////////////////////////////////////
    def ed_combo_data_type_index_changed(self, index) -> None:
        self.ui.editorPage_ui.psetPages.setCurrentIndex(index)

    def ed_combo_url_source_index_changed(self, index) -> None:
        if index == 0:
            self.ui.editorPage_ui.ledit_urlSource.setPlaceholderText("输入网址基本路径")
            self.ui.editorPage_ui.btn_chooseFile.setEnabled(False)
        elif index == 1:
            self.ui.editorPage_ui.ledit_urlSource.setPlaceholderText("输入或选择网址导入文件路径")
            self.ui.editorPage_ui.btn_chooseFile.setEnabled(True)

    def ed_combo_save_path_index_changed(self, index) -> None:
        if index == 0:
            self.ui.editorPage_ui.ledit_dataSavePath.setText(File.path(SysPath.OUTPUT))
            self.ui.editorPage_ui.ledit_dataSavePath.setEnabled(False)
            self.ui.editorPage_ui.btn_dataSavePath.setEnabled(False)
        if index == 1:
            self.ui.editorPage_ui.ledit_dataSavePath.clear()
            if self.ui.editorPage_ui.group_save.isChecked():
                self.ui.editorPage_ui.ledit_dataSavePath.setEnabled(True)
                self.ui.editorPage_ui.btn_dataSavePath.setEnabled(True)

    def btn_edit_back(self) -> None:
        if self.editPageMode == "new": msg = "是否在未保存的情况下返回总览界面\n将不会创建新配置"
        elif self.editPageMode == "edit": msg = "是否在未保存的情况下返回总览界面\n本次所有修改将被舍弃"
        if self.question.exec(title="请确认", msg=msg, msgType="warning"):
            self.ui.pages.setCurrentWidget(self.ui.overviewPage)

    def btn_edit_in_json(self) -> None:
        """在JSON文件中编辑"""
        self.editData = self._editPageFormDataGet()
        data_str = dumps(self.editData, indent=4)
        self.ui.jsonEditPage_ui.tedit_editor.setText(data_str)
        self.ui.pages.setCurrentWidget(self.ui.jsonEditPage)

    def btn_edit_check(self) -> None:
        self._configCheck_ui()

    def btn_edit_config_save(self) -> None:
        if self.editPageMode == "new":
            if self.dialog_configSaveMsgInput.exec():
                data = self._editPageFormDataGet()
                path = File.path(SysPath.CONFIGURATION, self.dialog_configSaveMsgInput.fileName)
                File.writeWithComment(path, data, bottom_comment=Define.FILE_JSON_BOTTOM_COMMENT["configuration"])
                self.ui.overviewPage_ui.table_overview.c_addRow([self.dialog_configSaveMsgInput.config_name, path, None, Define.LocalConfigState.U, self.dialog_configSaveMsgInput.comment])
                self.notice.exec("提示", "保存成功", msgType="success")
                self.ui.pages.setCurrentWidget(self.ui.overviewPage)
        elif self.editPageMode == "edit":
            data = self._editPageFormDataGet()
            File.writeWithComment(self.editFilePath, data, bottom_comment=Define.FILE_JSON_BOTTOM_COMMENT["configuration"])
            table = self.ui.overviewPage_ui.table_overview
            table.item(self.overviewTableEditRowIndex, 2).setText(Tools.datetime())
            self.notice.exec("提示", "保存成功", msgType="success")
            self.ui.pages.setCurrentWidget(self.ui.overviewPage)

    def btn_edit_default(self) -> None:
        if self.question.exec("注意", "是否确认恢复默认配置?"):
            defaultData: dict = loads(Define.FILE_DEFAULT_CONTENT["configuration"])
            self._editPageFormDataSet(defaultData)

    def btn_edit_url_set_confirm(self) -> None:
        if self.ui.editorPage_ui.combo_urlSource.currentIndex() == 0:
            url = self.ui.editorPage_ui.ledit_urlSource.text()
            urls: list = []
            firstPara = True
            f_continue = True
            if self.ui.editorPage_ui.group_parameter.isEnabled():
                for item in self.ui.editorPage_ui.table_parameter.c_getData():
                    if firstPara:
                        url = F"{url}?{item[0]}={item[1]}"
                        firstPara = False
                    else:
                        url = F"{url}&{item[0]}={item[1]}"
            if self.ui.editorPage_ui.group_iteration.isEnabled():
                i_name = self.ui.editorPage_ui.ledit_iterationName.text()
                i_start = self.ui.editorPage_ui.ledit_iterationStart.text()
                i_stop = self.ui.editorPage_ui.ledit_iterationStop.text()
                i_step = self.ui.editorPage_ui.ledit_iterationStep.text()
                if i_name:
                    try:
                        start = int(i_start)
                        stop = int(i_stop)
                        step = int(i_step)
                        for i in range(start, stop + 1, step):
                            if firstPara:
                                urls.append(F"{url}?{i_name}={i}")
                            else:
                                urls.append(F"{url}&{i_name}={i}")
                    except:
                        self.notice.exec("错误", "输入数据存在错误\n起始值,结束值以及步长只能输入数字", "error", "warning")
                        f_continue = False
            if f_continue:
                if urls:
                    self.ui.editorPage_ui.list_urlView.c_addRows(urls)
                elif url:
                    self.ui.editorPage_ui.list_urlView.c_addRows([url])
                else:
                    self.notice.exec("提示", "未输入任何内容")

        elif self.ui.editorPage_ui.combo_urlSource.currentIndex() == 1:
            self.notice.exec("提示", "该功能暂未实现...")
            # TODO: 实现文件导入功能

        self.ui.editorPage_ui.ledit_urlView_count.setText(str(self.ui.editorPage_ui.list_urlView.count()))

    def btn_edit_choose_file(self) -> None:
        url: QUrl
        url = QFileDialog.getOpenFileUrl(None, "选择文件")
        if url: self.ui.editorPage_ui.ledit_urlSource.setText(url.toLocalFile())

    def btn_edit_choose_save_path(self) -> None:
        url: QUrl
        url = QFileDialog.getExistingDirectoryUrl(None, "选择存储位置")
        if url: self.ui.editorPage_ui.ledit_dataSavePath.setText(url.toLocalFile())

    def btn_parse_headers(self) -> None:
        data = self.inputer.exec()
        self.ui.editorPage_ui.table_headers.c_addRows([item.split(": ") for item in data.splitlines()])

    def btn_parse_cookies(self) -> None:
        data = self.inputer.exec()
        self.ui.editorPage_ui.table_cookies.c_addRows([item.split("=") for item in data.split("; ")])

    # 配置编辑页面:JSON
    # ///////////////////////////////////////////////////////////////
    def btn_json_back(self) -> None:
        if self.question.exec(title="请确认", msg="是否在未保存的情况下返回总览界面\nJSON编辑页面的所有修改将被舍弃", msgType="warning"):
            self.ui.pages.setCurrentWidget(self.ui.editorPage)

    def btn_json_default(self) -> None:
        if self.question.exec("注意", "是否确认恢复默认配置?"):
            self.ui.jsonEditPage_ui.tedit_editor.setText(Define.FILE_DEFAULT_CONTENT["configuration"])

    def btn_json_confirm(self) -> None:
        data = loads(self.ui.jsonEditPage_ui.tedit_editor.toPlainText())
        self._editPageFormDataSet(data)
        self.ui.pages.setCurrentWidget(self.ui.editorPage)
        # TODO: 确认时的JSON格式检查

    # 中间函数
    # ///////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////
    def _editPageFormDataGet(self) -> dict:
        """获取编辑页面的数据打包为字典并返回"""
        data: dict = {}
        data["urls"] = self.ui.editorPage_ui.list_urlView.c_getData()
        data["request_method"] = self.ui.editorPage_ui.combo_requestMethod.currentText().lower()
        data["encoding"] = self.ui.editorPage_ui.combo_responseEncoding.currentText().lower()
        data["timeout"] = self.ui.editorPage_ui.spin_requestTimeout.value()
        data["verify"] = self.ui.editorPage_ui.check_verify.isChecked()
        dic: dict = {}
        for item in self.ui.editorPage_ui.table_headers.c_getData():
            dic[item[0]] = item[1]
        data["headers"] = deepcopy(dic)
        dic.clear()
        if self.ui.editorPage_ui.group_dataForm.isChecked():
            for item in self.ui.editorPage_ui.table_dataForm.c_getData():
                if item[0]: dic[item[0]] = item[1]
            data["data_form"] = deepcopy(dic)
        else:
            data["data_form"] = {}
        dic.clear()
        if self.ui.editorPage_ui.group_dataForm_script.isChecked():
            for item in self.ui.editorPage_ui.table_dataForm_script.c_getData():
                if item[0]: dic[item[0]] = [item[1], item[2], item[3]]
            data["data_form_script"] = deepcopy(dic)
        else:
            data["data_form_script"] = {}
        dic.clear()
        for item in self.ui.editorPage_ui.table_cookies.c_getData():
            if item[0]: dic[item[0]] = item[1]
        data["cookies"] = deepcopy(dic)
        dic.clear()
        lst: list = []
        if self.ui.editorPage_ui.group_userAgentPool.isChecked():
            lst = self.ui.editorPage_ui.tedit_userAgent.c_getLines()
            for item in lst:
                if item in ["", " "]: lst.remove(item)
            data["user_agent_pool"] = lst
        else:
            data["user_agent_pool"] = []
        if self.ui.editorPage_ui.group_ipProxyPool.isChecked():
            lst = self.ui.editorPage_ui.tedit_ipProxy.c_getLines()
            for item in lst:
                if item in ["", " "]: lst.remove(item)
            data["ip_proxy_pool"] = lst
        else:
            data["ip_proxy_pool"] = []
        data["parser_enable"] = self.ui.editorPage_ui.group_parse.isChecked()
        data["data_type"] = self.ui.editorPage_ui.combo_dataType.currentText().lower()
        data["pretreatment_enable"] = self.ui.editorPage_ui.group_dataCut.isChecked()
        data["pretreatment_setting"] = {}
        data["pretreatment_setting"]["tag_name"] = self.ui.editorPage_ui.ledit_dataCut_tagName.text()
        for item in self.ui.editorPage_ui.tedit_dataCut_attrs.c_getLines():
            item = item.split("=")
            if item.__len__() == 2:
                dic[item[0].strip()] = item[1].strip()
        data["pretreatment_setting"]["attrs"] = deepcopy(dic)
        dic.clear()
        num = 1
        for item in self.ui.editorPage_ui.table_psetText.c_getData(widgetCols=[0]):
            index = []
            for e in [i.strip() for i in item[2].split(",")]:
                try:
                    index.append(int(e))
                except:
                    pass
            if item[3] == "": sep = " "
            else: sep = item[3]
            dic[F"{num}@{item[0].currentText().lower()}"] = {"selector": item[1], "index": index, "sep": sep}
            num += 1
        data["parser_text_setting"] = deepcopy(dic)
        dic.clear()
        data["file_save_enable"] = self.ui.editorPage_ui.group_save.isChecked()
        data["file_save_setting"] = {}
        data["file_save_setting"]["save_path"] = "default" if self.ui.editorPage_ui.combo_dataSavePath.currentIndex() == 0 else self.ui.editorPage_ui.ledit_dataSavePath.text()
        data["file_save_setting"]["text"] = {}
        data["file_save_setting"]["bin"] = {}
        data["file_save_setting"]["text"]["file_type"] = self.ui.editorPage_ui.combo_saveText_fileType.currentText().lower()
        data["file_save_setting"]["text"]["file_name"] = self.ui.editorPage_ui.ledit_saveText_fileName.text()
        data["file_save_setting"]["text"]["page_cut_enable"] = self.ui.editorPage_ui.check_saveText_paging.isChecked()
        data["file_save_setting"]["text"]["limit_per_page"] = self.ui.editorPage_ui.spin_saveText_dataLimit.value()
        data["file_save_setting"]["bin"]["file_type"] = self.ui.editorPage_ui.combo_saveImage_fileType.currentText().lower()
        data["file_save_setting"]["bin"]["file_name"] = self.ui.editorPage_ui.ledit_saveImage_fileName.text()
        return data

    def _editPageFormDataSet(self, data: dict) -> None:
        """依据数据字典设置编辑页面的内容"""
        self.ui.editorPage_ui.list_urlView.clear()
        self.ui.editorPage_ui.table_headers.clear()
        self.ui.editorPage_ui.table_dataForm.clear()
        self.ui.editorPage_ui.table_dataForm_script.clear()
        self.ui.editorPage_ui.table_cookies.clear()
        self.ui.editorPage_ui.tedit_userAgent.clear()
        self.ui.editorPage_ui.tedit_ipProxy.clear()
        self.ui.editorPage_ui.tedit_dataCut_attrs.clear()
        self.ui.editorPage_ui.table_psetText.clear()
        self.ui.editorPage_ui.list_urlView.c_addRows(data["urls"])
        self.ui.editorPage_ui.ledit_urlView_count.setText(str(self.ui.editorPage_ui.list_urlView.count()))
        self.ui.editorPage_ui.combo_requestMethod.setCurrentText(data["request_method"].upper())
        self.ui.editorPage_ui.combo_responseEncoding.setCurrentText(data["encoding"].upper())
        self.ui.editorPage_ui.spin_requestTimeout.setValue(data["timeout"])
        self.ui.editorPage_ui.check_verify.setChecked(data["verify"])
        dic = data["headers"]
        for key in dic.keys():
            self.ui.editorPage_ui.table_headers.c_addRow([key, dic[key]])
        dic = data["data_form"]
        if dic != {}: self.ui.editorPage_ui.group_dataForm.setChecked(True)
        for key in dic.keys():
            self.ui.editorPage_ui.table_dataForm.c_addRow([key, dic[key]])
        dic = data["data_form_script"]
        if dic != {}: self.ui.editorPage_ui.group_dataForm_script.setChecked(True)
        for key in dic.keys():
            self.ui.editorPage_ui.table_dataForm_script.c_addRow([key, dic[key][0], dic[key][1], dic[key][2]])
        dic = data["cookies"]
        for key in dic.keys():
            self.ui.editorPage_ui.table_cookies.c_addRow([key, dic[key]])
        lst = data["user_agent_pool"]
        if lst != []: self.ui.editorPage_ui.group_userAgentPool.setChecked(True)
        self.ui.editorPage_ui.tedit_userAgent.c_addLines(lst)
        lst = data["ip_proxy_pool"]
        if lst != []: self.ui.editorPage_ui.group_ipProxyPool.setChecked(True)
        self.ui.editorPage_ui.tedit_ipProxy.c_addLines(lst)
        self.ui.editorPage_ui.group_parse.setChecked(data["parser_enable"])
        self.ui.editorPage_ui.combo_dataType.setCurrentText(data["data_type"].upper())
        self.ui.editorPage_ui.group_dataCut.setChecked(data["pretreatment_enable"])
        self.ui.editorPage_ui.ledit_dataCut_tagName.setText(data["pretreatment_setting"]["tag_name"])
        dic = data["pretreatment_setting"]["attrs"]
        lst = []
        for key in dic.keys():
            lst.append(F"{key}={dic[key]}")
        self.ui.editorPage_ui.tedit_dataCut_attrs.c_addLines(lst)
        dic = data["parser_text_setting"]
        for key in dic.keys():
            func_name = key.split("@")[1]
            cbox = ComboBox(scrollParent=self.ui.editorPage_ui.table_psetText)
            cbox.addItems(["RE", "BS4", "XPATH"])
            cbox.setCurrentText(func_name.upper())
            item = dic[key]
            index = None
            if item["index"] is not None:
                index = ",".join(str(i) for i in item["index"])
            self.ui.editorPage_ui.table_psetText.c_addRow([cbox, item["selector"], index, item["sep"]])
        self.ui.editorPage_ui.group_save.setChecked(data["file_save_enable"])
        if data["file_save_setting"]["save_path"] == "default":
            self.ui.editorPage_ui.combo_dataSavePath.setCurrentIndex(0)
            self.ui.editorPage_ui.ledit_dataSavePath.setText(File.path(SysPath.OUTPUT))
            self.ui.editorPage_ui.ledit_dataSavePath.setEnabled(False)
            self.ui.editorPage_ui.btn_dataSavePath.setEnabled(False)
        else:
            self.ui.editorPage_ui.combo_dataSavePath.setCurrentIndex(1)
            self.ui.editorPage_ui.ledit_dataSavePath.setText(data["file_save_setting"]["save_path"])
            if self.ui.editorPage_ui.group_save.isChecked():
                self.ui.editorPage_ui.ledit_dataSavePath.setEnabled(True)
                self.ui.editorPage_ui.btn_dataSavePath.setEnabled(True)
        self.ui.editorPage_ui.combo_saveText_fileType.setCurrentText(data["file_save_setting"]["text"]["file_type"].upper())
        self.ui.editorPage_ui.ledit_saveText_fileName.setText(data["file_save_setting"]["text"]["file_name"])
        self.ui.editorPage_ui.check_saveText_paging.setChecked(data["file_save_setting"]["text"]["page_cut_enable"])
        self.ui.editorPage_ui.spin_saveText_dataLimit.setValue(data["file_save_setting"]["text"]["limit_per_page"])
        self.ui.editorPage_ui.combo_saveImage_fileType.setCurrentText(data["file_save_setting"]["bin"]["file_type"].upper())
        self.ui.editorPage_ui.ledit_saveImage_fileName.setText(data["file_save_setting"]["bin"]["file_name"])

    def _configCheck_ui(self) -> None:
        # TODO: 完成配置检查功能
        list_urlView = self.ui.editorPage_ui.list_urlView
        list_urlView.c_RemoveAllState()
        index = -1
        for data in list_urlView.c_getData():
            index += 1
            if data == "":
                list_urlView.c_setRowState(index, "warn", "存在无意义的空值")

    def _configCheck_json(self) -> None:
        pass
