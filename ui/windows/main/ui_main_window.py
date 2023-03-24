# 主窗口UI
# ///////////////////////////////////////////////////////////////
from core.static import Define
from core.sys import Settings, Themes
from ui.pages import Ui_MainPagesContainer
from ui.preload.imp_qt import (QFrame, QHBoxLayout, QMainWindow, QObject, QPushButton, Qt, QVBoxLayout, QWidget)
from ui.widgets import Credits, Grips, IconButton, Navigation, TitleBar, Window


class Ui_MainWindow(QMainWindow):
    """主窗口界面UI类
    """

    # 属性
    # ///////////////////////////////////////////////////////////////
    settings: Settings
    themes: Themes

    central_widget_layout: QVBoxLayout
    central_widget: QWidget
    window: Window

    navigation_layout: QHBoxLayout
    navigation_frame: QFrame
    navigation: Navigation

    right_app_frame: QFrame
    right_app_layout: QVBoxLayout

    title_bar_frame: QFrame
    title_bar_layout: QVBoxLayout
    title_bar: TitleBar

    workspace_frame: QFrame
    workspace_layout: QHBoxLayout

    credits_frame: QFrame
    credits_layout: QVBoxLayout
    credits: Credits

    left_grip: Grips
    right_grip: Grips
    top_grip: Grips
    bottom_grip: Grips
    top_left_grip: Grips
    top_right_grip: Grips
    bottom_left_grip: Grips
    bottom_right_grip: Grips

    # 主页面
    main_pages: Ui_MainPagesContainer

    # ///////////////////////////////////////////////////////////////

    def __init__(self, settings, themes) -> None:
        """初始化主界面UI

        Args:
            settings (Settings): 设置封装对象
            themes (Themes): 主题样式封装对象
        """
        super().__init__()

        self.settings = settings
        self.themes = themes

        # 窗口基本设置
        self.hide_grips = True
        if self.settings.hide_title_bar:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.themes.window_size["startup"][0], self.themes.window_size["startup"][1])
        self.setMinimumSize(self.themes.window_size["minimum"][0], self.themes.window_size["minimum"][1])

        # 装载UI
        self.setup()
        # 设置初始页面
        self.set_page(self.main_pages_ui.page_start)

    def setup(self) -> None:
        """装载UI
        """

        # 主要容器部件
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(F'''
            font: {self.settings.font["text_size"]}pt "{self.settings.font["family"]}";
            color: {self.themes.color["text_foreground"]};
        ''')
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        if self.settings.hide_title_bar: self.central_widget_layout.setContentsMargins(10, 10, 10, 10)
        else: self.central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.window = Window(self, self.themes, self.settings)
        if self.settings.hide_title_bar is False: self.window.set_stylesheet(border_radius=0, border_size=0)
        self.central_widget_layout.addWidget(self.window)
        self.setCentralWidget(self.central_widget)

        # 窗口边界
        if self.settings.hide_title_bar:
            self.left_grip = Grips(self, "left", self.hide_grips)
            self.right_grip = Grips(self, "right", self.hide_grips)
            self.top_grip = Grips(self, "top", self.hide_grips)
            self.bottom_grip = Grips(self, "bottom", self.hide_grips)
            self.top_left_grip = Grips(self, "top_left", self.hide_grips)
            self.top_right_grip = Grips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = Grips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = Grips(self, "bottom_right", self.hide_grips)

        # 左侧导航栏
        self.navigation_frame = QFrame()
        navigation_margin = self.themes.navigation["margins"]
        navigation_minimum_width = self.themes.navigation["minimum_width"]
        self.navigation_frame.setMaximumSize(navigation_minimum_width + (navigation_margin * 2), 17280)
        self.navigation_frame.setMinimumSize(navigation_minimum_width + (navigation_margin * 2), 0)
        self.navigation_layout = QHBoxLayout(self.navigation_frame)
        self.navigation_layout.setContentsMargins(navigation_margin, navigation_margin, navigation_margin, navigation_margin)
        self.navigation = Navigation(self.navigation_frame, self.central_widget, self.themes)
        self.navigation_layout.addWidget(self.navigation.ui)

        # 除左侧导航栏外的右侧部分
        self.right_app_frame = QFrame()
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setContentsMargins(3, 3, 3, 3)
        self.right_app_layout.setSpacing(6)

        # 标题栏
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setMinimumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = TitleBar(self, self.central_widget, self.settings.hide_title_bar, self.themes)
        self.title_bar_layout.addWidget(self.title_bar.ui)
        if self.settings.hide_title_bar: self.title_bar.ui.set_title(Define.APP_NAME)
        else: self.title_bar.ui.set_title("Welcome")

        # 主界面工作区
        self.workspace_frame = QFrame()
        self.workspace_layout = QHBoxLayout(self.workspace_frame)
        self.workspace_layout.setContentsMargins(0, 0, 0, 0)
        self.workspace_layout.setSpacing(0)

        # 底部信息栏
        self.credits_frame = QFrame()
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setContentsMargins(0, 0, 0, 0)
        self.credits = Credits(Define.COPYRIGHT, Define.VERSION, self.themes, self.settings.font)
        self.credits_layout.addWidget(self.credits)

        # 主页面
        self.main_pages = QWidget()
        self.main_pages_ui = Ui_MainPagesContainer(self.main_pages, self.themes)

        self.workspace_layout.addWidget(self.main_pages)

        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.workspace_frame)
        self.right_app_layout.addWidget(self.credits_frame)

        self.window.slayout.addWidget(self.navigation_frame)
        self.window.slayout.addWidget(self.right_app_frame)

    # API
    # ///////////////////////////////////////////////////////////////
    def get_btns(self) -> QObject:
        if self.title_bar.ui.sender() is not None:
            return self.title_bar.ui.sender()
        elif self.navigation.ui.sender() is not None:
            return self.navigation.ui.sender()

    def set_page(self, page) -> None:
        self.main_pages_ui.pages.setCurrentWidget(page)

    def get_title_bar_btn(self, object_name) -> IconButton:
        return self.title_bar_frame.findChild(QPushButton, object_name)

    def get_nav_btn(self, object_name):
        return self.navigation.ui.findChild(QPushButton, object_name)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        if self.settings.hide_title_bar:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
