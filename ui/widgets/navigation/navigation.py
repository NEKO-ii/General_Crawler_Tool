# 导航栏
# ///////////////////////////////////////////////////////////////
from core.static import Define
from .ui_navigation import Navigation_UI


class Navigation:
    """界面左侧导航栏
    """

    # 属性
    # ///////////////////////////////////////////////////////////////
    ui: Navigation_UI

    # ///////////////////////////////////////////////////////////////

    # 左侧导航栏菜单
    navigation_menus = [{
        "btn_icon": "icon_start.svg",
        "btn_id": "btn_nav_start",
        "btn_text": "快速开始",
        "btn_tooltip": "快速开始",
        "show_top": True,
        "is_active": True
    }, {
        "btn_icon": "icon_config.svg",
        "btn_id": "btn_nav_config",
        "btn_text": "编辑配置",
        "btn_tooltip": "编辑配置",
        "show_top": True,
        "is_active": False
    }, {
        "btn_icon": "icon_request.svg",
        "btn_id": "btn_nav_request",
        "btn_text": "端口请求",
        "btn_tooltip": "端口请求",
        "show_top": True,
        "is_active": False
    }, {
        "btn_icon": "icon_parse.svg",
        "btn_id": "btn_nav_parse",
        "btn_text": "数据解析",
        "btn_tooltip": "数据解析",
        "show_top": True,
        "is_active": False
    }, {
        "btn_icon": "icon_script.svg",
        "btn_id": "btn_nav_script",
        "btn_text": "用户脚本",
        "btn_tooltip": "用户脚本",
        "show_top": True,
        "is_active": False
    }, {
        "btn_icon": "icon_temp.svg",
        "btn_id": "btn_nav_temp",
        "btn_text": "临时数据",
        "btn_tooltip": "临时数据",
        "show_top": True,
        "is_active": False
    }, {
        "btn_icon": "icon_help.svg",
        "btn_id": "btn_nav_help",
        "btn_text": "帮助",
        "btn_tooltip": "帮助",
        "show_top": False,
        "is_active": False
    }, {
        "btn_icon": "icon_log.svg",
        "btn_id": "btn_nav_log",
        "btn_text": "日志",
        "btn_tooltip": "日志",
        "show_top": False,
        "is_active": False
    }, {
        "btn_icon": "icon_settings.svg",
        "btn_id": "btn_nav_settings",
        "btn_text": "设置",
        "btn_tooltip": "设置",
        "show_top": False,
        "is_active": False
    }]

    def __init__(self, container, central_widget, themes) -> None:
        """初始化导航栏

        Args:
            container (Any): 导航栏容器
            central_widget (Any): 窗口主组件
            themes (Themes): 样式封装对象
        """
        self.ui = Navigation_UI(container, central_widget, themes)
        self.ui.setObjectName("navigation")
        self.ui.add_menus(self.navigation_menus)
