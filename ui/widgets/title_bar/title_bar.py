# 标题栏
# ///////////////////////////////////////////////////////////////
from .ui_title_bar import TitleBar_UI


class TitleBar:
    """标题栏类
    """

    # 属性
    # ///////////////////////////////////////////////////////////////
    ui: TitleBar_UI

    # ///////////////////////////////////////////////////////////////

    # 标题栏菜单
    titlebarMenus = [{"btn_icon": "icon_account.svg", "btn_id": "btn_top_account", "btn_tooltip": "账户", "is_active": False}]

    def __init__(self, container, centralWidget, hideTitleBar, themes):
        """初始化标题栏

        Args:
            container (Any): 导航栏容器
            central_widget (Any): 窗口主组件
            hide_title_bar (bool): 隐藏原有标题栏
            themes (Themes): 样式封装对象
        """
        self.ui = TitleBar_UI(container, centralWidget, hideTitleBar, themes)
        self.ui.setObjectName("title_bar")
        self.ui.add_menus(self.titlebarMenus)
