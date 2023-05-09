# 系统设置模块,服务于系统设置的读取与保存
# ///////////////////////////////////////////////////////////////
import json
from os import getcwd
from os.path import abspath, join, normpath

from core.static.define import Define
from core.support.json_minify import remove_json_comments
from core.support.decorator import Decorator as deco


class Settings:
    """设置类
    """

    # 设置文件路径(固定位置)
    __settings_file_path: str
    # 软件名称
    app_name: str = Define.APP_NAME

    # 设置项
    # ///////////////////////////////////////////////////////////////
    sleep: dict
    parser_message_out: dict
    asynchronous: dict
    folder_path: dict
    system_log_recording: dict
    hide_title_bar: bool
    font: dict
    theme_name: str

    def __init__(self) -> None:
        self.__settings_file_path = normpath(join(abspath(getcwd()), Define.PATH_SETTINGS, "settings.json"))
        self.sleep = {}
        self.parser_message_out = {}
        self.asynchronous = {}
        self.folder_path = {}
        self.system_log_recording = {}
        self.hide_title_bar = True
        self.font = {}
        self.theme_name = ""
        # 运行设置读取
        self.read_settings()

    # 方法定义
    # ///////////////////////////////////////////////////////////////

    @deco.settings_load
    def read_settings(self) -> None:
        """读取设置文件
        """
        json_str: str
        with open(self.__settings_file_path, "r", encoding="UTF-8") as file:
            json_str = file.read()
        settings: dict = self.__deserialize(json_str)
        # 设置应用
        self.sleep = settings["sleep"]
        self.parser_message_out = settings["parser_message_out"]
        self.asynchronous = settings["asynchronous"]
        self.folder_path = settings["folder_path"]
        self.system_log_recording = settings["system_log_recording"]
        self.hide_title_bar = settings["hide_title_bar"]
        self.font = settings["font"]
        self.theme_name = settings["theme_name"]

    def write_settings(self) -> None:
        """写入设置文件
        """
        json_str: str = self.__serialize()
        with open(self.__settings_file_path, "w", encoding="UTF-8") as file:
            file.write(json_str)
            file.write(Define.FILE_JSON_BOTTOM_COMMENT["settings"])

    def __serialize(self) -> str:
        """序列化设置项

        Returns:
            str: 返回JSON字符串
        """
        settings: dict = {}
        settings["sleep"] = self.sleep
        settings["parser_message_out"] = self.parser_message_out
        settings["asynchronous"] = self.asynchronous
        settings["folder_path"] = self.folder_path
        settings["system_log_recording"] = self.system_log_recording
        settings["hide_title_bar"] = self.hide_title_bar
        settings["font"] = self.font
        settings["theme_name"] = self.theme_name
        json_str: str = json.dumps(settings)
        return json_str

    def __deserialize(self, json_str: str) -> dict:
        """反序列化JSON字符串

        Returns:
            dict: 返回设置字典
        """
        json_str_woc: str = remove_json_comments(json_str)
        settings: dict = json.loads(json_str_woc)
        return settings
