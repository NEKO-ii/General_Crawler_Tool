# 主窗口函数
# ///////////////////////////////////////////////////////////////
from .Ui_MainWindow import Ui_MainWindow
from core.support.msg_printer import MsgType, console_printer


class Func_MainWindow:
    """主窗口函数类
    """

    # 属性
    # ///////////////////////////////////////////////////////////////
    ui: Ui_MainWindow

    btn_id_to_func: dict  # 按钮ID对应函数字典
    btn_id: str  # 用于存储当前点击的按钮ID

    # ///////////////////////////////////////////////////////////////

    def __init__(self, ui) -> None:
        self.ui = ui
        self.btn_id_to_func = {}
        self.initFuncDict()
        self.connect()

    def initFuncDict(self) -> None:
        """初始化字典
        """
        self.btn_id_to_func["btn_nav_start"] = self.nav_start
        self.btn_id_to_func["btn_nav_config"] = self.nav_config
        self.btn_id_to_func["btn_nav_cloud"] = self.nav_cloud
        self.btn_id_to_func["btn_nav_parse"] = self.nav_parse
        self.btn_id_to_func["btn_nav_script"] = self.nav_script
        self.btn_id_to_func["btn_nav_temp"] = self.nav_temp
        self.btn_id_to_func["btn_nav_help"] = self.nav_help
        self.btn_id_to_func["btn_nav_log"] = self.nav_log
        self.btn_id_to_func["btn_nav_settings"] = self.nav_settings

        self.btn_id_to_func["btn_top_account"] = self.top_account

    def connect(self) -> None:
        """链接按钮事件
        """
        self.ui.navigation.ui.clicked.connect(self.btn_clicked)
        self.ui.navigation.ui.released.connect(self.btn_released)
        self.ui.titleBar.ui.clicked.connect(self.btn_clicked)
        self.ui.titleBar.ui.released.connect(self.btn_released)
        self.ui.mainPages_ui.startPage_inner.ui.btnPage_ui.btn_config.clicked.connect(self.page_start_btn_config)
        self.ui.mainPages_ui.startPage_inner.ui.btnPage_ui.btn_help.clicked.connect(self.page_start_btn_help)

    def btn_clicked(self):
        """按钮点击事件分发
        """
        btn = self.ui.getBtns()
        self.btn_id = btn.objectName()
        if self.btn_id in self.btn_id_to_func:
            self.btn_id_to_func[self.btn_id]()
        else:
            console_printer(MsgType.ERROR, "btn func not found")

    def btn_released(self):
        """按钮释放事件分发
        """
        btn = self.ui.getBtns()
        self.btn_id = btn.objectName()

    # 按钮事件方法定义
    # ///////////////////////////////////////////////////////////////
    def nav_start(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        self.ui.mainPages_ui.startPage_inner.ui.pages.setCurrentWidget(self.ui.mainPages_ui.startPage_inner.ui.btnPage)
        self.ui.setPage(self.ui.mainPages_ui.startPage)
        # console_printer(MsgType.INFOMATION, "btn start clicked")

    def nav_config(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        self.ui.mainPages_ui.configPage_inner.ui.pages.setCurrentIndex(0)
        self.ui.setPage(self.ui.mainPages_ui.configPage)
        # console_printer(MsgType.INFOMATION, "btn configuration clicked")

    def nav_cloud(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        self.ui.setPage(self.ui.mainPages_ui.page_3)
        console_printer(MsgType.INFOMATION, "btn cloud clicked")

    def nav_parse(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        console_printer(MsgType.INFOMATION, "btn parse clicked")

    def nav_script(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        self.ui.mainPages_ui.scriptPage_inner.ui.pages.setCurrentIndex(0)
        self.ui.setPage(self.ui.mainPages_ui.scriptPage)
        # console_printer(MsgType.INFOMATION, "btn script clicked")

    def nav_temp(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        self.ui.mainPages_ui.tempviewPage_inner.ui.pages.setCurrentIndex(0)
        self.ui.setPage(self.ui.mainPages_ui.tempviewPage)
        # console_printer(MsgType.INFOMATION, "btn temp clicked")

    def nav_help(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        console_printer(MsgType.INFOMATION, "btn help clicked")

    def nav_log(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        console_printer(MsgType.INFOMATION, "btn log clicked")

    def nav_settings(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne(self.btn_id)
        console_printer(MsgType.INFOMATION, "btn settings clicked")

    # 标题栏按钮
    # ///////////////////////////////////////////////////////////////
    def top_account(self) -> None:
        console_printer(MsgType.INFOMATION, "btn top account clicked")

    # 起始页按钮
    # ///////////////////////////////////////////////////////////////
    def page_start_btn_config(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne("btn_nav_config")
        self.ui.setPage(self.ui.mainPages_ui.configPage)

    def page_start_btn_help(self) -> None:
        self.ui.navigation.ui.c_selectOnlyOne("btn_nav_help")
        console_printer(MsgType.INFOMATION, "start page btn2 clicked")
