# 脚本管理页面函数模块
# ///////////////////////////////////////////////////////////////
from .Ui_ScriptPage import Ui_ScriptPage
from core.sys.file import File, SysPath, DataType
from ui.dialog import Question, Notice, ScriptMessageInput, ScriptTest
from core.static.define import Define
from core.support.tools import Tools
from core.support.coderunner import runpy, runjs
from ui.preload.imp_qt import QObject, Signal, QThread
from json import dumps


class Func_ScriptPage:
    ui: Ui_ScriptPage

    editPageMode: str = None
    currentTemplateIndex: int = 0
    editFilePath: str = None
    overviewTableEditRowIndex: int = None

    flag_currentTextChanged: bool = False
    flag_editComboBack: bool = True

    scriptTestThread: QThread = None

    def __init__(self, ui: Ui_ScriptPage) -> None:
        self.ui = ui
        self._createDialog()
        self._btnConnect()
        self._signalConnect()

    def _btnConnect(self) -> None:
        """按钮信号链接"""
        # 总览界面
        self.ui.overview_ui.btn_new.clicked.connect(self.btn_new_script)
        self.ui.overview_ui.btn_import.clicked.connect(self.btn_import_script)
        self.ui.overview_ui.btn_edit.clicked.connect(self.btn_edit_script)
        self.ui.overview_ui.btn_test.clicked.connect(self.btn_test_script)
        self.ui.overview_ui.btn_delete.clicked.connect(self.btn_delete_script)
        self.ui.overview_ui.btn_flush.clicked.connect(self.btn_flush_overview_table)
        self.ui.overview_ui.btn_clear.clicked.connect(self.ui.overview_ui.ledit_search.clear)
        # 编辑界面
        self.ui.editor_ui.btn_back.clicked.connect(self.btn_back_to_overview)
        self.ui.editor_ui.btn_default.clicked.connect(self.btn_back_to_default)
        self.ui.editor_ui.btn_test.clicked.connect(self.btn_test_script)
        self.ui.editor_ui.btn_save_as.clicked.connect(self.btn_save_as)
        self.ui.editor_ui.btn_save.clicked.connect(self.btn_save)

    def _signalConnect(self) -> None:
        """其他信号链接"""
        # 总览界面
        self.ui.overview_ui.table_overview.sig_open.connect(self.sig_overview_table_show)
        self.ui.overview_ui.table_overview.sig_dataChanged.connect(self.sig_overview_table_changed)
        self.ui.overview_ui.ledit_search.textChanged.connect(self.solt_search)
        # 编辑界面
        self.ui.editor_ui.combo_template.sig_currentIndexChanged.connect(self.sig_combo_template_current_index_changed)
        self.ui.editor_ui.tedit_editor.textChanged.connect(self.sig_edit_text_changed)
        self.stest.sig_btn_run_clicked.connect(self.sig_dialog_btn_run)
        self.stest.sig_stop.connect(self.sig_close_test)

    def _createDialog(self) -> None:
        """创建弹窗"""
        self.question = Question()
        self.notice = Notice()
        self.inputer = ScriptMessageInput()
        self.stest = ScriptTest()

    # 方法
    # ///////////////////////////////////////////////////////////////
    def createRunnerThread(self) -> None:
        if self.scriptTestThread is not None:
            if self.scriptTestThread.isRunning():
                self.scriptTestThread.quit()
                self.notice.exec("注意", "请等待上一进程退出后重试")
                return
        self.scriptTestThread = QThread()
        self.scriptRunner = ScriptRunner()
        self.scriptRunner.moveToThread(self.scriptTestThread)
        # 脚本测试窗口
        self.scriptTestThread.started.connect(self.scriptRunner.runtest)
        self.scriptTestThread.finished.connect(self.sig_close_test)
        self.scriptRunner.sig_result.connect(self.sig_result_get)

    # 按钮动作定义
    # ///////////////////////////////////////////////////////////////
    def btn_new_script(self) -> None:
        self.editPageMode = "new"
        self.ui.editor_ui.tedit_editor.clear()
        self.ui.editor_ui.tedit_editor.setReadOnly(True)
        self.flag_currentTextChanged = False
        self.ui.editor_ui.combo_template.setCurrentIndex(0)
        self.ui.editor_ui.combo_template.setEnabled(True)
        self.ui.editor_ui.btn_save_as.hide()
        self.ui.pages.setCurrentWidget(self.ui.editor)

    def btn_import_script(self) -> None:
        # TODO: 实现导入功能
        pass

    def btn_edit_script(self) -> None:
        self.editPageMode = "edit"
        table = self.ui.overview_ui.table_overview
        selectedItems = table.selectedItems()
        if selectedItems:
            currentRow = selectedItems[0].row()
            path = table.item(currentRow, 2).text()
            if File.isFileExists(path):
                self.editFilePath = path
                self.overviewTableEditRowIndex = currentRow
                extendName = path.rsplit(".", 1)[-1]
                if extendName == "py":
                    self.ui.editor_ui.combo_template.setCurrentIndex(1)
                    self.currentTemplateIndex = 1
                elif extendName == "js":
                    self.ui.editor_ui.combo_template.setCurrentIndex(2)
                    self.currentTemplateIndex = 2
                self.ui.editor_ui.combo_template.setEnabled(False)
                data = File.read_opt(path, DataType.STRING)
                self.ui.editor_ui.tedit_editor.setPlainText(data)
                self.flag_currentTextChanged = False
                self.ui.editor_ui.btn_save_as.show()
                self.ui.pages.setCurrentWidget(self.ui.editor)
            else:
                self.notice.exec("出现错误", "文件路径不存在,该脚本文件可能已被移动或删除", "error", "info")
        else:
            self.notice.exec("注意", "未选择任何脚本,请选择后进行编辑\n多选仅编辑第一个选中配置")

    def btn_test_script(self, objname: str) -> None:
        if objname == "overview_script_test_btn":
            table = self.ui.overview_ui.table_overview
            items = table.selectedItems()
            row = items[0].row() if items else None
            if row is not None:
                self.stest.exec(items[0].text(), items[2].text())
            else:
                self.notice.exec("提示", "在点击测试前请选择一个脚本")
        elif objname == "edit_script_test_btn":
            if self.ui.editor_ui.tedit_editor.toPlainText() == "":
                self.notice.exec("提示", "编辑器无内容,无法启动测试")
                return
            exname = {0: None, 1: "py", 2: "js"}
            if self.editPageMode == "new":
                path = File.path(SysPath.TEMP, "tmpscript", F"temp_script.{exname[self.currentTemplateIndex]}")
                File.write(path, self.ui.editor_ui.tedit_editor.toPlainText())
                self.stest.exec("临时测试脚本", path)
                File.delete(path)
            elif self.editPageMode == "edit":
                name = self.ui.overview_ui.table_overview.item(self.overviewTableEditRowIndex, 0).text()
                if self.flag_currentTextChanged:
                    path = File.path(SysPath.TEMP, "tmpscript", F"editing_script.{exname[self.currentTemplateIndex]}")
                    File.write(path, self.ui.editor_ui.tedit_editor.toPlainText())
                    self.stest.exec(F"{name}(正在编辑)", path)
                    File.delete(path)
                else:
                    self.stest.exec(name, self.editFilePath)

        # self.stest.exec()

    def btn_delete_script(self) -> None:
        table = self.ui.overview_ui.table_overview
        if table.c_getCurrentIndex()[0]:
            if self.question.exec(title="是否确认删除", msg="删除脚本会同时删除脚本文件,若需保留请提前备份", msgType="warn"):
                for item in table.c_getData(onlyCol=[2], onlySelectedRows=True):
                    File.delete(item[0])
                table.c_deleteSelectdRows()
        else:
            self.notice.exec("提示", "未选中任何脚本")

    def btn_flush_overview_table(self) -> None:
        table = self.ui.overview_ui.table_overview
        table.flag_initComplete = False
        table.clear()
        data = File.read_opt(File.path(SysPath.CACHE, "custom_script.dat"), DataType.LIST, "#")
        for row in data:
            table.c_addRow(eval(row))
        table.flag_initComplete = True

    def btn_back_to_default(self) -> None:
        f_continue = True
        if self.editPageMode == "new":
            if self.flag_currentTextChanged:
                if not self.question.exec("请确认", "执行该操作将丢失已编辑内容\n是否继续?", msgType="warn"):
                    f_continue = False
        elif self.editPageMode == "edit":
            if not self.question.exec("请确认", "执行该操作将丢失已有内容\n是否继续?", msgType="warn"):
                f_continue = False
        if f_continue:
            key = {1: "script_py", 2: "script_js"}
            if self.currentTemplateIndex == 0:
                self.ui.editor_ui.tedit_editor.clear()
                self.flag_currentTextChanged = False
            else:
                self.ui.editor_ui.tedit_editor.setText(Define.FILE_DEFAULT_CONTENT[key[self.currentTemplateIndex]])
                self.flag_currentTextChanged = False

    def btn_back_to_overview(self) -> None:
        if self.flag_currentTextChanged:
            if self.question.exec(title="请确认", msg="是否在未保存的情况下返回总览界面", msgType="warn"):
                self.ui.pages.setCurrentWidget(self.ui.overview)
        else:
            self.ui.pages.setCurrentWidget(self.ui.overview)

    def btn_save_as(self) -> None:
        # 修改编辑模式调用新建分支
        self.editPageMode = "new"
        self.btn_save()
        # 修改为原模式
        self.editPageMode = "edit"

    def btn_save(self) -> None:
        if self.editPageMode == "new":
            exname = {0: None, 1: "py", 2: "js"}
            code, data = self.inputer.exec(exname[self.currentTemplateIndex])
            if code:
                text = self.ui.editor_ui.tedit_editor.toPlainText()
                path = File.path(SysPath.SCRIPT, data["file_name"])
                File.write(path, text)
                self.ui.overview_ui.table_overview.c_addRow([data["script_name"], data["file_name"].rsplit(".", 1)[-1].upper(), path, Tools.datetime(), data["comment"]])
                self.ui.pages.setCurrentWidget(self.ui.overview)
        elif self.editPageMode == "edit":
            text = self.ui.editor_ui.tedit_editor.toPlainText()
            File.write(self.editFilePath, text)
            self.ui.overview_ui.table_overview.item(self.overviewTableEditRowIndex, 3).setText(Tools.datetime())
            self.notice.exec("提示", "保存成功", msgType="success")
            self.ui.pages.setCurrentWidget(self.ui.overview)

    # 信号动作定义
    # ///////////////////////////////////////////////////////////////
    def sig_overview_table_show(self) -> None:
        table = self.ui.overview_ui.table_overview
        datas = File.read_opt(File.path(SysPath.CACHE, "custom_script.dat"), DataType.LIST, "#")
        for row in datas:
            data = eval(row)
            table.c_addRow(data)
        table.flag_initComplete = True

    def sig_overview_table_changed(self, currentIndex: list) -> None:
        table = self.ui.overview_ui.table_overview
        currentRow = currentIndex[0]
        if currentRow: table.item(currentRow, 3).setText(Tools.datetime())
        data = table.c_getData()
        File.writeWithComment(File.path(SysPath.CACHE, "custom_script.dat"), data, top_comment=Define.FILE_DAT_TOP_COMMENT["custom_script"])

    def sig_combo_template_current_index_changed(self, index: int) -> None:
        # 只有当编辑页面模式为新建时才生效
        if self.flag_editComboBack and self.editPageMode == "new":
            f_continue = True
            if self.flag_currentTextChanged:
                if not self.question.exec(title="请确认", msg="切换模版将会清空当前编辑的内容\n是否确认切换?", msgType="warn"):
                    f_continue = False
                    # 退回旧模版索引,过程中加锁
                    self.flag_editComboBack = False
                    self.ui.editor_ui.combo_template.setCurrentIndex(self.currentTemplateIndex)
                    self.flag_editComboBack = True
            if f_continue:
                key = {1: "script_py", 2: "script_js"}
                if index == 0:
                    self.ui.editor_ui.tedit_editor.clear()
                    self.flag_currentTextChanged = False
                else:
                    self.ui.editor_ui.tedit_editor.setText(Define.FILE_DEFAULT_CONTENT[key[index]])
                    self.flag_currentTextChanged = False
        # 更新当前模版索引
        self.currentTemplateIndex = self.ui.editor_ui.combo_template.currentIndex()
        if self.currentTemplateIndex == 0:
            self.ui.editor_ui.tedit_editor.setReadOnly(True)
        else:
            self.ui.editor_ui.tedit_editor.setReadOnly(False)

    def sig_edit_text_changed(self) -> None:
        self.flag_currentTextChanged = True

    def sig_dialog_btn_run(self, path, args) -> None:
        self.createRunnerThread()
        self.scriptRunner.setargs(path, args)
        self.scriptTestThread.start()

    def sig_result_get(self, result: tuple[bool, dict, str]) -> None:
        self.sig_close_test()
        flag, data, msg = result
        if flag is True:
            if data:
                self.stest.msgAppend("SUCCESS", "success", "[", F"] {msg}")
            else:
                self.stest.msgAppend("SUCCESS", "success", "[", F"] {msg}")
            self.stest.msgAppend(dumps(data, indent=2), "info", "输出数据: \n")
        else:
            if data:
                self.stest.msgAppend("ERROR", "error", "[", "] 脚本生成数据解析失败,请检查脚本输出字符串数据是否为字典格式")
                self.stest.msgAppend("脚本输出内容如下:")
                self.stest.msgAppend(dumps(data, indent=2), "warn")
            else:
                self.stest.msgAppend("ERROR", "error", "[", "] 脚本执行失败,可能因为脚本语法错误")
            self.stest.msgAppend("错误信息如下:")
            self.stest.msgAppend(msg, "error")

    def sig_close_test(self) -> None:
        if self.scriptTestThread is not None:
            self.scriptTestThread.quit()

    def solt_search(self, text) -> None:
        if text == "":
            self.ui.overview_ui.table_overview.c_setAllHidden(False)
        else:
            self.ui.overview_ui.table_overview.c_search(text)

# TODO: 代码着色功能


class ScriptRunner(QObject):
    sig_result = Signal(tuple)

    args: list
    path: str

    dic: dict = {"py": runpy, "js": runjs}

    def __init__(self) -> None:
        super().__init__()

    def runtest(self) -> None:
        extendn = self.path.rsplit(".", 1)[-1]
        result = self.dic[extendn](self.path, self.args)
        # result = (str(item) for item in result)
        self.sig_result.emit(result)

    def setargs(self, path, args) -> None:
        self.path = path
        self.args = args
