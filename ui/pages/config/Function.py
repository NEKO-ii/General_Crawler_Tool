from copy import deepcopy
from json import loads, dumps

from core.static import Define
from core.support import MsgType, Tools, console_printer
from core.sys import DataType, File, SysPath
from ui.preload.imp_qt import QFileDialog, QUrl
from ui.dialog import Dialog_ConfigMessageInput, Question, Notice
from ui.widgets import ComboBox

from .Ui_ConfigurationPage import Ui_ConfigurationPage


class Func_ConfigPage:
    ui: Ui_ConfigurationPage

    edit_page_mode: str = None
    edit_data: dict = None
    edit_file_path: str = None
    overview_table_edit_row_index: int = None

    def __init__(self, ui: Ui_ConfigurationPage) -> None:
        self.ui = ui
        self.btn_connect()
        self.signal_connect()
        self.create_dialog()

    # 按钮事件链接
    # ///////////////////////////////////////////////////////////////
    def btn_connect(self) -> None:
        """按钮事件链接"""
        # 配置总览页面
        self.ui.page_overview_ui.btn_new_config.clicked.connect(self.btn_new_config)
        self.ui.page_overview_ui.btn_import.clicked.connect(self.btn_import_config)
        self.ui.page_overview_ui.btn_edit.clicked.connect(self.btn_edit_config)
        self.ui.page_overview_ui.btn_flush.clicked.connect(self.ov_table_overview_flush)
        self.ui.page_overview_ui.btn_delete.clicked.connect(self.btn_delete_config)

        # 配置编辑页面
        self.ui.page_editor_ui.btn_back.clicked.connect(self.btn_edit_back)
        self.ui.page_editor_ui.btn_default.clicked.connect(self.btn_edit_default)
        self.ui.page_editor_ui.btn_edit_json.clicked.connect(self.btn_edit_in_json)
        self.ui.page_editor_ui.btn_save.clicked.connect(self.btn_edit_config_save)
        self.ui.page_editor_ui.btn_choose_file.clicked.connect(self.btn_edit_choose_file)
        self.ui.page_editor_ui.btn_url_set_confirm.clicked.connect(self.btn_edit_url_set_confirm)

        self.ui.page_editor_ui.btn_parameter_add.clicked.connect(self.btns_add_items)
        self.ui.page_editor_ui.btn_url_view_add.clicked.connect(self.btns_add_items)
        self.ui.page_editor_ui.btn_headers_add.clicked.connect(self.btns_add_items)
        self.ui.page_editor_ui.btn_data_form_add.clicked.connect(self.btns_add_items)
        self.ui.page_editor_ui.btn_data_form_script_add.clicked.connect(self.btns_add_items)
        self.ui.page_editor_ui.btn_cookies_add.clicked.connect(self.btns_add_items)
        self.ui.page_editor_ui.btn_pset_text_add.clicked.connect(self.btns_add_items)

        self.ui.page_editor_ui.btn_parameter_delete.clicked.connect(self.btns_delete_items)
        self.ui.page_editor_ui.btn_url_view_delete.clicked.connect(self.btns_delete_items)
        self.ui.page_editor_ui.btn_headers_delete.clicked.connect(self.btns_delete_items)
        self.ui.page_editor_ui.btn_data_form_delete.clicked.connect(self.btns_delete_items)
        self.ui.page_editor_ui.btn_data_form_script_delete.clicked.connect(self.btns_delete_items)
        self.ui.page_editor_ui.btn_cookies_delete.clicked.connect(self.btns_delete_items)
        self.ui.page_editor_ui.btn_pset_text_delete.clicked.connect(self.btns_delete_items)

        # 配置编辑页面:JSON
        self.ui.page_json_ui.btn_back.clicked.connect(self.btn_json_back)
        self.ui.page_json_ui.btn_default.clicked.connect(self.btn_json_default)
        self.ui.page_json_ui.btn_confirm.clicked.connect(self.btn_json_confirm)

    def signal_connect(self) -> None:
        """自定义信号槽链接"""
        # 配置总览页面
        self.ui.page_overview_ui.table_overview.sig_open.connect(self.ov_table_overview_init_data)
        self.ui.page_overview_ui.table_overview.sig_data_changed.connect(self.ov_table_overview_data_changed)
        self.ui.page_overview_ui.table_overview.sig_flush.connect(self.ov_table_overview_flush)

        # 配置编辑页面
        self.ui.page_editor_ui.combo_data_type.sig_current_index_changed.connect(self.ed_combo_data_type_index_changed)
        self.ui.page_editor_ui.combo_url_source.sig_current_index_changed.connect(self.ed_combo_url_source_index_changed)

        # 配置编辑页面:JSON

    def create_dialog(self) -> None:
        """创建对话框"""
        self.dialog_config_save_msg_input = Dialog_ConfigMessageInput()
        self.question = Question()
        self.notice = Notice()

    # 函数定义
    # ///////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////
    def name(self) -> None:
        pass

    def btns_add_items(self, obj_name: str) -> None:
        """给按钮对应的列表或表格添加一行"""
        if obj_name == "btn_parameter_add": self.ui.page_editor_ui.table_parameter.add_row()
        if obj_name == "btn_url_view_add":
            self.ui.page_editor_ui.list_url_view.add_rows(["new url"])
            self.ui.page_editor_ui.ledit_url_view_count.setText(str(self.ui.page_editor_ui.list_url_view.count()))
        if obj_name == "btn_headers_add": self.ui.page_editor_ui.table_headers.add_row()
        if obj_name == "btn_data_form_add": self.ui.page_editor_ui.table_data_form.add_row()
        if obj_name == "btn_data_form_script_add": self.ui.page_editor_ui.table_data_form_script.add_row()
        if obj_name == "btn_cookies_add": self.ui.page_editor_ui.table_cookies.add_row()
        cbox = ComboBox(scroll_parent=self.ui.page_editor_ui.table_pset_text)
        cbox.addItems(["RE", "BS4", "XPATH"])
        cbox.setCurrentText("RE")
        if obj_name == "btn_pset_text_add": self.ui.page_editor_ui.table_pset_text.add_row([cbox])

    def btns_delete_items(self, obj_name: str) -> None:
        """删除按钮对应的列表或表格的所有选中行"""
        if obj_name == "btn_parameter_delete": self.ui.page_editor_ui.table_parameter.delete_selectd_rows()
        if obj_name == "btn_url_view_delete":
            self.ui.page_editor_ui.list_url_view.delete_selectd_rows()
            self.ui.page_editor_ui.ledit_url_view_count.setText(str(self.ui.page_editor_ui.list_url_view.count()))
        if obj_name == "btn_headers_delete": self.ui.page_editor_ui.table_headers.delete_selectd_rows()
        if obj_name == "btn_data_form_delete": self.ui.page_editor_ui.table_data_form.delete_selectd_rows()
        if obj_name == "btn_data_form_script_delete": self.ui.page_editor_ui.table_data_form_script.delete_selectd_rows()
        if obj_name == "btn_cookies_delete": self.ui.page_editor_ui.table_cookies.delete_selectd_rows()
        if obj_name == "btn_pset_text_delete": self.ui.page_editor_ui.table_pset_text.delete_selectd_rows()

    # 配置总览页面
    # ///////////////////////////////////////////////////////////////
    def ov_table_overview_init_data(self) -> None:
        """初始化配置总览信息"""
        table = self.ui.page_overview_ui.table_overview
        datas = File.read_opt(File.path(SysPath.CACHE, "local_configuration.dat"), DataType.LIST, "#")
        for data in datas:
            data_list = eval(data)
            table.add_row(data_list)
        rindex = 0
        for item in table.get_data(only_col=[3]):
            if item != []:
                if item[0] in Define.LOCAL_CONF_STATE_TYPE["success"]: table.set_cell_color(rindex, 3, "success")
                elif item[0] in Define.LOCAL_CONF_STATE_TYPE["error"]: table.set_cell_color(rindex, 3, "error")
                elif item[0] in Define.LOCAL_CONF_STATE_TYPE["warning"]: table.set_cell_color(rindex, 3, "warning")
            rindex += 1
        table.flag_init_complete = True

    def ov_table_overview_flush(self) -> None:
        """刷新配置总览信息"""
        table = self.ui.page_overview_ui.table_overview
        table.flag_init_complete = False
        table.clear()
        datas = File.read_opt(File.path(SysPath.CACHE, "local_configuration.dat"), DataType.LIST, "#")
        for data in datas:
            data_list = eval(data)
            table.add_row(data_list)
        rindex = 0
        for item in table.get_data(only_col=[3]):
            if item != []:
                if item[0] in Define.LOCAL_CONF_STATE_TYPE["success"]: table.set_cell_color(rindex, 3, "success")
                elif item[0] in Define.LOCAL_CONF_STATE_TYPE["error"]: table.set_cell_color(rindex, 3, "error")
                elif item[0] in Define.LOCAL_CONF_STATE_TYPE["warning"]: table.set_cell_color(rindex, 3, "warning")
            rindex += 1
        table.flag_init_complete = True

    def ov_table_overview_data_changed(self, current_index: list) -> None:
        """表格数据变化后更新文件数据"""
        table = self.ui.page_overview_ui.table_overview
        current_row = current_index[0]
        current_col = current_index[1]
        if current_row: table.item(current_row, 2).setText(Tools.datetime())
        data = table.get_data()
        File.write_with_comment(File.path(SysPath.CACHE, "local_configuration.dat"), data, top_comment=Define.FILE_DAT_TOP_COMMENT["local_configuration"])
        if current_col and current_col == 3:
            text = table.item(current_row, current_col).text()
            if text in Define.LOCAL_CONF_STATE_TYPE["success"]: table.set_cell_color(current_row, current_col, "success")
            elif text in Define.LOCAL_CONF_STATE_TYPE["error"]: table.set_cell_color(current_row, current_col, "error")
            elif text in Define.LOCAL_CONF_STATE_TYPE["warning"]: table.set_cell_color(current_row, current_col, "warning")
            else:
                table.item(current_row, current_col).setText("U")
                table.set_cell_color(current_row, current_col, "warning")
                self.notice.exec("注意", "输入状态标识无效, 请参考提示\n已修改为未知状态:U", title_type="warning", msg_type="info")

    def btn_new_config(self) -> None:
        """新建配置"""
        self.edit_page_mode = "new"
        default_data: dict = loads(Define.FILE_DEFAULT_CONTENT["configuration"])
        self.edit_page_form_data_set(default_data)
        self.ui.pages.setCurrentWidget(self.ui.page_editor)

    def btn_import_config(self) -> None:
        """导入配置"""
        console_printer(MsgType.INFOMATION, "btn import config clicked")

    def btn_edit_config(self) -> None:
        """编辑配置"""
        self.edit_page_mode = "edit"
        table = self.ui.page_overview_ui.table_overview
        selected_items = table.selectedItems()
        if selected_items:
            current_row = selected_items[0].row()
            self.overview_table_edit_row_index = current_row
            path = table.item(current_row, 1).text()
            # print(path)
            if File.file_exists(path):
                try:
                    self.edit_data = File.read_opt(path, DataType.DICTIONARY)
                    self.edit_file_path = path
                    self.edit_page_form_data_set(self.edit_data)
                    self.ui.pages.setCurrentWidget(self.ui.page_editor)
                except Exception as e:
                    console_printer(MsgType.ERROR, e)
                    table.item(current_row, 3).setText(Define.LocalConfigState.N)
                    table.set_cell_color(current_row, 3, "error")
                    self.notice.exec("出现错误", "配置文件解析失败,文件内容格式可能出现错误", "error", "info")
            else:
                console_printer(MsgType.ERROR, "该配置JSON文件已被移动")
                table.item(current_row, 3).setText(Define.LocalConfigState.FL)
                table.set_cell_color(current_row, 3, "error")
                self.notice.exec("出现错误", "文件路径不存在,该配置JSON文件可能已被移动或删除", "error", "info")
        else:
            self.notice.exec("注意", "未选择任何配置,请选择后进行编辑\n多选仅编辑第一个选中配置")

    def btn_delete_config(self) -> None:
        """删除配置"""
        table = self.ui.page_overview_ui.table_overview
        if table.get_current_index()[0]:
            if self.question.exec(title="是否确认删除", msg="删除配置会同时删除配置文件,若需保留请提前备份", msg_type="warning"):
                for item in table.get_data(only_col=[1], only_selected_rows=True):
                    # print(item[0])
                    File.delete(item[0])
                table.delete_selectd_rows()
        else:
            self.notice.exec("提示", "未选中任何配置文件")

    # 配置编辑页面
    # ///////////////////////////////////////////////////////////////
    def ed_combo_data_type_index_changed(self, index) -> None:
        self.ui.page_editor_ui.pset_pages.setCurrentIndex(index)

    def ed_combo_url_source_index_changed(self, index) -> None:
        if index == 0:
            self.ui.page_editor_ui.ledit_url_source.setPlaceholderText("输入网址基本路径")
            self.ui.page_editor_ui.btn_choose_file.setEnabled(False)
        elif index == 1:
            self.ui.page_editor_ui.ledit_url_source.setPlaceholderText("输入或选择网址导入文件路径")
            self.ui.page_editor_ui.btn_choose_file.setEnabled(True)

    def btn_edit_back(self) -> None:
        if self.edit_page_mode == "new": msg = "是否在未保存的情况下返回总览界面\n将不会创建新配置"
        elif self.edit_page_mode == "edit": msg = "是否在未保存的情况下返回总览界面\n本次所有修改将被舍弃"
        if self.question.exec(title="请确认", msg=msg, msg_type="warning"):
            self.ui.pages.setCurrentWidget(self.ui.page_overview)

    def btn_edit_in_json(self) -> None:
        """在JSON文件中编辑"""
        self.edit_data = self.edit_page_form_data_get()
        data_str = dumps(self.edit_data, indent=4)
        self.ui.page_json_ui.tedit_editor.setText(data_str)
        self.ui.pages.setCurrentWidget(self.ui.page_json)

    def btn_edit_config_save(self) -> None:
        if self.edit_page_mode == "new":
            if self.dialog_config_save_msg_input.exec():
                data = self.edit_page_form_data_get()
                path = File.path(SysPath.CONFIGURATION, self.dialog_config_save_msg_input.file_name)
                File.write_with_comment(path, data, bottom_comment=Define.FILE_JSON_BOTTOM_COMMENT["configuration"])
                self.ui.page_overview_ui.table_overview.add_row([self.dialog_config_save_msg_input.config_name, path, None, Define.LocalConfigState.U, self.dialog_config_save_msg_input.comment])
                self.notice.exec("提示", "保存成功", msg_type="success")
                self.ui.pages.setCurrentWidget(self.ui.page_overview)
        elif self.edit_page_mode == "edit":
            # TODO: 覆盖和另存为的选择
            data = self.edit_page_form_data_get()
            File.write_with_comment(self.edit_file_path, data, bottom_comment=Define.FILE_JSON_BOTTOM_COMMENT["configuration"])
            table = self.ui.page_overview_ui.table_overview
            table.item(self.overview_table_edit_row_index, 2).setText(Tools.datetime())
            self.notice.exec("提示", "保存成功", msg_type="success")
            self.ui.pages.setCurrentWidget(self.ui.page_overview)

    def btn_edit_default(self) -> None:
        if self.question.exec("注意", "是否确认恢复默认配置?"):
            default_data: dict = loads(Define.FILE_DEFAULT_CONTENT["configuration"])
            self.edit_page_form_data_set(default_data)

    def btn_edit_url_set_confirm(self) -> None:
        if self.ui.page_editor_ui.combo_url_source.currentIndex() == 0:
            url = self.ui.page_editor_ui.ledit_url_source.text()
            urls: list = []
            first_para = True
            if self.ui.page_editor_ui.group_parameter.isEnabled():
                for item in self.ui.page_editor_ui.table_parameter.get_data():
                    if first_para:
                        url = F"{url}?{item[0]}={item[1]}"
                        first_para = False
                    else:
                        url = F"{url}&{item[0]}={item[1]}"
            if self.ui.page_editor_ui.group_iteration.isEnabled():
                i_name = self.ui.page_editor_ui.ledit_iteration_name.text()
                i_start = self.ui.page_editor_ui.ledit_iteration_start.text()
                i_stop = self.ui.page_editor_ui.ledit_iteration_stop.text()
                i_step = self.ui.page_editor_ui.ledit_iteration_step.text()
                if i_name:
                    try:
                        start = int(i_start)
                        stop = int(i_stop)
                        step = int(i_step)
                        for i in range(start, stop + 1, step):
                            if first_para:
                                urls.append(F"{url}?{i_name}={i}")
                            else:
                                urls.append(F"{url}&{i_name}={i}")
                    except:
                        self.notice.exec("错误", "输入信息有误\n起始值,结束值以及步长只能输入数字", "error", "warning")
            if urls:
                self.ui.page_editor_ui.list_url_view.add_rows(urls)
            elif url:
                self.ui.page_editor_ui.list_url_view.add_rows([url])
            else:
                self.notice.exec("提示", "未输入任何信息")

        elif self.ui.page_editor_ui.combo_url_source.currentIndex() == 1:
            self.notice.exec("提示", "该功能暂未实现...")
            # TODO: 实现文件导入功能

        self.ui.page_editor_ui.ledit_url_view_count.setText(str(self.ui.page_editor_ui.list_url_view.count()))

    def btn_edit_choose_file(self) -> None:
        url: QUrl
        url, type = QFileDialog.getOpenFileUrl(None, "选择文件")
        if url: self.ui.page_editor_ui.ledit_url_source.setText(url.toLocalFile())

    # 配置编辑页面:JSON
    # ///////////////////////////////////////////////////////////////
    def btn_json_back(self) -> None:
        if self.question.exec(title="请确认", msg="是否在未保存的情况下返回总览界面\nJSON编辑页面的所有修改将被舍弃", msg_type="warning"):
            self.ui.pages.setCurrentWidget(self.ui.page_editor)

    def btn_json_default(self) -> None:
        if self.question.exec("注意", "是否确认恢复默认配置?"):
            self.ui.page_json_ui.tedit_editor.setText(Define.FILE_DEFAULT_CONTENT["configuration"])

    def btn_json_confirm(self) -> None:
        data = loads(self.ui.page_json_ui.tedit_editor.toPlainText())
        self.edit_page_form_data_set(data)
        self.ui.pages.setCurrentWidget(self.ui.page_editor)
        # TODO: 确认时的JSON格式检查

    # 中间函数
    # ///////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////
    def edit_page_form_data_get(self) -> dict:
        """获取编辑页面的数据打包为字典并返回"""
        data: dict = {}
        data["urls"] = self.ui.page_editor_ui.list_url_view.get_data()
        data["request_method"] = self.ui.page_editor_ui.combo_request_method.currentText().lower()
        data["encoding"] = self.ui.page_editor_ui.combo_response_encoding.currentText().lower()
        data["timeout"] = self.ui.page_editor_ui.spin_request_timeout.value()
        data["verify"] = self.ui.page_editor_ui.check_verify.isChecked()
        dic: dict = {}
        for item in self.ui.page_editor_ui.table_headers.get_data():
            dic[item[0]] = item[1]
        data["headers"] = deepcopy(dic)
        dic.clear()
        if self.ui.page_editor_ui.group_data_form.isChecked():
            for item in self.ui.page_editor_ui.table_data_form.get_data():
                if item[0]: dic[item[0]] = item[1]
            data["data_form"] = deepcopy(dic)
        else:
            data["data_form"] = {}
        dic.clear()
        if self.ui.page_editor_ui.group_data_form_script.isChecked():
            for item in self.ui.page_editor_ui.table_data_form_script.get_data():
                if item[0]: dic[item[0]] = [item[1], item[2], item[3]]
            data["data_form_script"] = deepcopy(dic)
        else:
            data["data_form_script"] = {}
        dic.clear()
        for item in self.ui.page_editor_ui.table_cookies.get_data():
            if item[0]: dic[item[0]] = item[1]
        data["cookies"] = deepcopy(dic)
        dic.clear()
        lst: list = []
        if self.ui.page_editor_ui.group_user_agent_pool.isChecked():
            lst = self.ui.page_editor_ui.tedit_user_agent.get_lines()
            for item in lst:
                if item in ["", " "]: lst.remove(item)
            data["user_agent_pool"] = lst
        else:
            data["user_agent_pool"] = []
        if self.ui.page_editor_ui.group_ip_proxy_pool.isChecked():
            lst = self.ui.page_editor_ui.tedit_ip_proxy.get_lines()
            for item in lst:
                if item in ["", " "]: lst.remove(item)
            data["ip_proxy_pool"] = lst
        else:
            data["ip_proxy_pool"] = []
        data["parser_enable"] = self.ui.page_editor_ui.group_parse.isChecked()
        data["data_type"] = self.ui.page_editor_ui.combo_data_type.currentText().lower()
        data["pretreatment_enable"] = self.ui.page_editor_ui.group_data_cut.isChecked()
        data["pretreatment_setting"] = {}
        data["pretreatment_setting"]["tag_name"] = self.ui.page_editor_ui.ledit_data_cut_tag_name.text()
        for item in self.ui.page_editor_ui.tedit_data_cut_attrs.get_lines():
            item = item.split("=")
            if item.__len__() == 2:
                dic[item[0].strip()] = item[1].strip()
        data["pretreatment_setting"]["attrs"] = deepcopy(dic)
        dic.clear()
        num = 1
        for item in self.ui.page_editor_ui.table_pset_text.get_data(widget_cols=[0]):
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
        data["file_save_enable"] = self.ui.page_editor_ui.group_save.isChecked()
        data["file_save_setting"] = {}
        data["file_save_setting"]["text"] = {}
        data["file_save_setting"]["bin"] = {}
        data["file_save_setting"]["text"]["file_type"] = self.ui.page_editor_ui.combo_save_text_file_type.currentText().lower()
        data["file_save_setting"]["text"]["file_name"] = self.ui.page_editor_ui.ledit_save_text_file_name.text()
        data["file_save_setting"]["text"]["page_cut_enable"] = self.ui.page_editor_ui.check_save_text_paging.isChecked()
        data["file_save_setting"]["text"]["data_count_limit_per_page"] = self.ui.page_editor_ui.spin_save_text_data_limit.value()
        data["file_save_setting"]["bin"]["file_type"] = self.ui.page_editor_ui.combo_save_image_file_type.currentText().lower()
        data["file_save_setting"]["bin"]["file_name"] = self.ui.page_editor_ui.ledit_save_image_file_name.text()
        return data

    def edit_page_form_data_set(self, data: dict) -> None:
        """依据数据字典设置编辑页面的内容"""
        self.ui.page_editor_ui.list_url_view.clear()
        self.ui.page_editor_ui.table_headers.clear()
        self.ui.page_editor_ui.table_data_form.clear()
        self.ui.page_editor_ui.table_data_form_script.clear()
        self.ui.page_editor_ui.table_cookies.clear()
        self.ui.page_editor_ui.tedit_user_agent.clear()
        self.ui.page_editor_ui.tedit_ip_proxy.clear()
        self.ui.page_editor_ui.tedit_data_cut_attrs.clear()
        self.ui.page_editor_ui.table_pset_text.clear()
        self.ui.page_editor_ui.list_url_view.add_rows(data["urls"])
        self.ui.page_editor_ui.ledit_url_view_count.setText(str(self.ui.page_editor_ui.list_url_view.count()))
        self.ui.page_editor_ui.combo_request_method.setCurrentText(data["request_method"].upper())
        self.ui.page_editor_ui.combo_response_encoding.setCurrentText(data["encoding"].upper())
        self.ui.page_editor_ui.spin_request_timeout.setValue(data["timeout"])
        self.ui.page_editor_ui.check_verify.setChecked(data["verify"])
        dic = data["headers"]
        for key in dic.keys():
            self.ui.page_editor_ui.table_headers.add_row([key, dic[key]])
        dic = data["data_form"]
        if dic != {}: self.ui.page_editor_ui.group_data_form.setChecked(True)
        for key in dic.keys():
            self.ui.page_editor_ui.table_data_form.add_row([key, dic[key]])
        dic = data["data_form_script"]
        if dic != {}: self.ui.page_editor_ui.group_data_form_script.setChecked(True)
        for key in dic.keys():
            self.ui.page_editor_ui.table_data_form_script.add_row([key, dic[key][0], dic[key][1], dic[key][2]])
        dic = data["cookies"]
        for key in dic.keys():
            self.ui.page_editor_ui.table_cookies.add_row([key, dic[key]])
        lst = data["user_agent_pool"]
        if lst != []: self.ui.page_editor_ui.group_user_agent_pool.setChecked(True)
        self.ui.page_editor_ui.tedit_user_agent.add_lines(lst)
        lst = data["ip_proxy_pool"]
        if lst != []: self.ui.page_editor_ui.group_ip_proxy_pool.setChecked(True)
        self.ui.page_editor_ui.tedit_ip_proxy.add_lines(lst)
        self.ui.page_editor_ui.group_parse.setChecked(data["parser_enable"])
        self.ui.page_editor_ui.combo_data_type.setCurrentText(data["data_type"].upper())
        self.ui.page_editor_ui.group_data_cut.setChecked(data["pretreatment_enable"])
        self.ui.page_editor_ui.ledit_data_cut_tag_name.setText(data["pretreatment_setting"]["tag_name"])
        dic = data["pretreatment_setting"]["attrs"]
        lst = []
        for key in dic.keys():
            lst.append(F"{key}={dic[key]}")
        self.ui.page_editor_ui.tedit_data_cut_attrs.add_lines(lst)
        dic = data["parser_text_setting"]
        for key in dic.keys():
            func_name = key.split("@")[1]
            cbox = ComboBox(scroll_parent=self.ui.page_editor_ui.table_pset_text)
            cbox.addItems(["RE", "BS4", "XPATH"])
            cbox.setCurrentText(func_name.upper())
            item = dic[key]
            index = None
            if item["index"] is not None:
                index = ",".join(str(i) for i in item["index"])
            self.ui.page_editor_ui.table_pset_text.add_row([cbox, item["selector"], index, item["sep"]])
        self.ui.page_editor_ui.group_save.setChecked(data["file_save_enable"])
        self.ui.page_editor_ui.combo_save_text_file_type.setCurrentText(data["file_save_setting"]["text"]["file_type"].upper())
        self.ui.page_editor_ui.ledit_save_text_file_name.setText(data["file_save_setting"]["text"]["file_name"])
        self.ui.page_editor_ui.check_save_text_paging.setChecked(data["file_save_setting"]["text"]["page_cut_enable"])
        self.ui.page_editor_ui.spin_save_text_data_limit.setValue(data["file_save_setting"]["text"]["data_count_limit_per_page"])
        self.ui.page_editor_ui.combo_save_image_file_type.setCurrentText(data["file_save_setting"]["bin"]["file_type"].upper())
        self.ui.page_editor_ui.ledit_save_image_file_name.setText(data["file_save_setting"]["bin"]["file_name"])
