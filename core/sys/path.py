import os

from core.static import Define
from core.support.msg_printer import MsgType, console_printer
from core.sys import Settings
from core.support.decorator import Decorator as deco


class Path:
    # 系统根目录
    __base: str
    # 文件夹根目录
    __folder: str

    # 子文件夹路径
    # ///////////////////////////////////////////////////////////////
    p_configuration: str
    p_script: str
    p_themes: str
    p_settings: str
    p_temp: str
    p_log: str
    p_help: str
    p_input: str
    p_output: str

    # 文件路径
    # ///////////////////////////////////////////////////////////////
    f_settings: str
    f_help_main: str
    f_help_parse: str
    f_help_request: str
    f_help_script: str

    # 检查列表
    # ///////////////////////////////////////////////////////////////
    __folder_check_list: list
    __file_check_list: list

    def __init__(self) -> None:
        self.__base = os.path.abspath(os.getcwd())
        self.__folder = F"{self.__base}\\file"

        self.p_configuration = F"{self.__folder}\\configuration"
        self.p_script = F"{self.__folder}\\script"
        self.p_themes = F"{self.__folder}\\themes"
        self.p_settings = F"{self.__folder}\\settings"
        self.p_temp = F"{self.__folder}\\temp"
        self.p_log = F"{self.__folder}\\log"
        self.p_help = F"{self.__folder}\\help"
        self.p_input = F"{self.__folder}\\io\\input"
        self.p_output = F"{self.__folder}\\io\\output"
        self.p_cache = F"{self.__folder}\\cache"

        self.f_settings = F"{self.p_settings}\\settings.json"
        self.f_help_main = F"{self.p_help}\\help_main.txt"
        self.f_help_parse = F"{self.p_help}\\help_parse.txt"
        self.f_help_request = F"{self.p_help}\\help_request.txt"
        self.f_help_script = F"{self.p_help}\\help_script.txt"

        self.__folder_check_list = [self.__folder, self.p_configuration, self.p_script, self.p_themes, self.p_settings, self.p_temp, self.p_log, self.p_help, self.p_input, self.p_output, self.p_cache]
        self.__file_check_list = [self.f_settings, self.f_help_main, self.f_help_parse, self.f_help_request, self.f_help_script]

    # 方法定义
    # ///////////////////////////////////////////////////////////////
    def folder_check(self) -> None:
        """检查系统默认文件夹目录是否完整,不完整则重建目录
        """
        for path in self.__folder_check_list:
            if os.path.exists(path) is False:
                os.makedirs(path)
                console_printer(MsgType.WARNING, F"Path not found, it has been rebuild. @{path}")

    def file_check(self) -> None:
        """检查系统依赖文件是否存在,不存在则重新创建默认文件
        """
        for file in self.__file_check_list:
            if os.path.exists(file) is False:
                with open(file, "w", encoding="UTF-8") as f:
                    f.write(Define.FILE_DEFAULT_CONTENT[os.path.basename(file).rsplit(".", 1)[0]])
                console_printer(MsgType.WARNING, F"System file loss, it has been recreated. @{file}")

    @deco.settings_load
    def update(self) -> None:
        """依据系统设置更新路径
        """
        # 读取设置
        settings: Settings = Settings()
        path: dict = settings.folder_path
        # 应用设置
        self.p_input = F"{self.__folder}\\io\\input" if path["file_input_path"].lower() == "default" else path["file_input_path"]
        self.p_output = F"{self.__folder}\\io\\output" if path["file_output_path"].lower() == "default" else path["file_output_path"]
        self.p_configuration = F"{self.__folder}\\configuration" if path["configuration_path"].lower() == "default" else path["configuration_path"]
        self.p_script = F"{self.__folder}\\script" if path["script_path"].lower() == "default" else path["script_path"]
        self.p_temp = F"{self.__folder}\\temp" if path["temp_file_path"].lower() == "default" else path["temp_file_path"]
        self.p_log = F"{self.__folder}\\log" if path["log_path"].lower() == "default" else path["log_path"]
        self.__folder_check_list = [self.__folder, self.p_configuration, self.p_script, self.p_themes, self.p_settings, self.p_temp, self.p_log, self.p_help, self.p_input, self.p_output, self.p_cache]
