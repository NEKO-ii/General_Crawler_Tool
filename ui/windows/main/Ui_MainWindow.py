# 主窗口UI
# ///////////////////////////////////////////////////////////////
from core.static import Define
from core.sys import Globalv, GlvKey, Settings, Themes
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

    centralWidgetLayout: QVBoxLayout
    centralWidget: QWidget
    window: Window

    navigationLayout: QHBoxLayout
    navigationFrame: QFrame
    navigation: Navigation

    rightAppFrame: QFrame
    rightAppLayout: QVBoxLayout

    titleBarFrame: QFrame
    titleBarLayout: QVBoxLayout
    titleBar: TitleBar

    workspaceFrame: QFrame
    workspaceLayout: QHBoxLayout

    creditsFrame: QFrame
    creditsLayout: QVBoxLayout
    credits: Credits

    leftGrip: Grips
    rightGrip: Grips
    topGrip: Grips
    bottomGrip: Grips
    topLeftGrip: Grips
    topRightGrip: Grips
    bottomLeftGrip: Grips
    bottomRightGrip: Grips

    # 主页面
    mainPages: Ui_MainPagesContainer

    # ///////////////////////////////////////////////////////////////

    def __init__(self) -> None:
        """初始化主界面UI"""
        super().__init__()

        self.settings = Globalv.get(GlvKey.SETTINGS)
        self.themes = Globalv.get(GlvKey.THEMES)

        # 窗口基本设置
        self.hideGrips = True
        if self.settings.hide_title_bar:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.themes.window_size["startup"][0], self.themes.window_size["startup"][1])
        self.setMinimumSize(self.themes.window_size["minimum"][0], self.themes.window_size["minimum"][1])

        # 装载UI
        self.setup()
        # 设置初始页面
        self.setPage(self.mainPages_ui.startPage)

    def setup(self) -> None:
        """装载UI
        """

        # 主要容器部件
        self.centralWidget = QWidget()
        self.centralWidget.setStyleSheet(F'''
            font: {self.settings.font["text_size"]}pt "{self.settings.font["family"]}";
            color: {self.themes.color["text_foreground"]};
        ''')
        self.centralWidgetLayout = QVBoxLayout(self.centralWidget)
        if self.settings.hide_title_bar: self.centralWidgetLayout.setContentsMargins(10, 10, 10, 10)
        else: self.centralWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.window = Window(self, self.themes, self.settings)
        if self.settings.hide_title_bar is False: self.window.c_setStylesheet(borderRadius=0, borderSize=0)
        self.centralWidgetLayout.addWidget(self.window)
        self.setCentralWidget(self.centralWidget)

        # 窗口边界
        if self.settings.hide_title_bar:
            self.leftGrip = Grips(self, "left", self.hideGrips)
            self.rightGrip = Grips(self, "right", self.hideGrips)
            self.topGrip = Grips(self, "top", self.hideGrips)
            self.bottomGrip = Grips(self, "bottom", self.hideGrips)
            self.topLeftGrip = Grips(self, "top_left", self.hideGrips)
            self.topRightGrip = Grips(self, "top_right", self.hideGrips)
            self.bottomLeftGrip = Grips(self, "bottom_left", self.hideGrips)
            self.bottomRightGrip = Grips(self, "bottom_right", self.hideGrips)

        # 左侧导航栏
        self.navigationFrame = QFrame()
        navigationMargin = self.themes.navigation["margins"]
        navigationMinimumWidth = self.themes.navigation["minimum_width"]
        self.navigationFrame.setMaximumSize(navigationMinimumWidth + (navigationMargin * 2), 17280)
        self.navigationFrame.setMinimumSize(navigationMinimumWidth + (navigationMargin * 2), 0)
        self.navigationLayout = QHBoxLayout(self.navigationFrame)
        self.navigationLayout.setContentsMargins(navigationMargin, navigationMargin, navigationMargin, navigationMargin)
        self.navigation = Navigation(self.navigationFrame, self.centralWidget, self.themes)
        self.navigationLayout.addWidget(self.navigation.ui)

        # 除左侧导航栏外的右侧部分
        self.rightAppFrame = QFrame()
        self.rightAppLayout = QVBoxLayout(self.rightAppFrame)
        self.rightAppLayout.setContentsMargins(3, 3, 3, 3)
        self.rightAppLayout.setSpacing(6)

        # 标题栏
        self.titleBarFrame = QFrame()
        self.titleBarFrame.setMinimumHeight(40)
        self.titleBarFrame.setMaximumHeight(40)
        self.titleBarLayout = QVBoxLayout(self.titleBarFrame)
        self.titleBarLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = TitleBar(self, self.centralWidget, self.settings.hide_title_bar, self.themes)
        self.titleBarLayout.addWidget(self.titleBar.ui)
        if self.settings.hide_title_bar: self.titleBar.ui.set_title(Define.APP_NAME)
        else: self.titleBar.ui.set_title("Welcome")

        # 主界面工作区
        self.workspaceFrame = QFrame()
        self.workspaceLayout = QHBoxLayout(self.workspaceFrame)
        self.workspaceLayout.setContentsMargins(0, 0, 0, 0)
        self.workspaceLayout.setSpacing(0)

        # 底部信息栏
        self.creditsFrame = QFrame()
        self.creditsFrame.setMinimumHeight(26)
        self.creditsFrame.setMaximumHeight(26)
        self.creditsLayout = QVBoxLayout(self.creditsFrame)
        self.creditsLayout.setContentsMargins(0, 0, 0, 0)
        self.credits = Credits(Define.COPYRIGHT, Define.VERSION, self.themes, self.settings.font)
        self.creditsLayout.addWidget(self.credits)

        # 主页面
        self.mainPages = QWidget()
        self.mainPages_ui = Ui_MainPagesContainer(self.mainPages)

        self.workspaceLayout.addWidget(self.mainPages)

        self.rightAppLayout.addWidget(self.titleBarFrame)
        self.rightAppLayout.addWidget(self.workspaceFrame)
        self.rightAppLayout.addWidget(self.creditsFrame)

        self.window.slayout.addWidget(self.navigationFrame)
        self.window.slayout.addWidget(self.rightAppFrame)

    # API
    # ///////////////////////////////////////////////////////////////
    def getBtns(self) -> QObject:
        if self.titleBar.ui.sender() is not None:
            return self.titleBar.ui.sender()
        elif self.navigation.ui.sender() is not None:
            return self.navigation.ui.sender()

    def setPage(self, page) -> None:
        self.mainPages_ui.pages.setCurrentWidget(page)

    def getTitleBarBtn(self, objectName) -> IconButton:
        return self.titleBarFrame.findChild(QPushButton, objectName)

    def getNavBtn(self, objectName):
        return self.navigation.ui.findChild(QPushButton, objectName)

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        if self.settings.hide_title_bar:
            self.leftGrip.setGeometry(5, 10, 10, self.height())
            self.rightGrip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.topGrip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottomGrip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.topRightGrip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottomLeftGrip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottomRightGrip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
