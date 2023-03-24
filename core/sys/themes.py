# 界面主题样式加载模块,服务于主题样式读取
# ///////////////////////////////////////////////////////////////
import json
from os import getcwd
from os.path import abspath, join, normpath, isfile

from core.static.define import Define
from core.support.msg_printer import MsgType, console_printer


class Themes:
    """界面主题样式类
    """

    # 样式文件路径
    __theme_file_path: str

    # 样式属性
    # ///////////////////////////////////////////////////////////////
    theme_name: str
    window_size: dict
    navigation: dict
    right_column: dict
    color: dict

    def __init__(self, theme_name: str) -> None:
        self.__theme_file_path = normpath(join(abspath(getcwd()), Define.PATH_THEMES, F"{theme_name}.json"))
        self.theme_name = theme_name
        self.read_themes()

    # 方法定义
    # ///////////////////////////////////////////////////////////////

    def read_themes(self) -> None:
        """读取主题设置
        """
        # 若主题文件不存在则使用默认设置创建新主题文件
        if isfile(self.__theme_file_path) is False:
            with open(self.__theme_file_path, "w", encoding="UTF-8") as file:
                file.write(json.dumps(Define.DEFAULT_THEMES))
            console_printer(MsgType.WARNING, "Theme file not found, it has been created based on the default theme.")
        # 打开并读取主题文件内容
        with open(self.__theme_file_path, "r", encoding="UTF-8") as file:
            themes: dict = json.loads(file.read())
        # 应用设置
        self.time_animation = themes["time_animation"]
        self.window_size = themes["window_size"]
        self.navigation = themes["navigation"]
        self.right_column = themes["right_column"]
        self.color = themes["color"]
