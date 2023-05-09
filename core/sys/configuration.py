# 网络请求与数据解析配置模块,服务于配置的读取与存储
# ///////////////////////////////////////////////////////////////
import json

from core.static.define import Define
from core.support.json_minify import remove_json_comments
from core.support.decorator import Decorator as deco


class Configuration:
    """配置类
    """

    # 路径
    __config_path: str

    # 网络请求配置项
    # ///////////////////////////////////////////////////////////////
    urls: list
    request_method: str
    encoding: str
    timeout: float
    verify: bool
    headers: dict
    data_form: dict
    data_form_script: dict
    cookies: dict
    user_agent_pool: list
    ip_proxy_pool: list
    # 数据解析配置项
    # ///////////////////////////////////////////////////////////////
    parser_enable: bool
    data_type: str
    pretreatment_enable: bool
    pretreatment_setting: dict
    parser_text_setting: dict
    # 数据保存配置
    # ///////////////////////////////////////////////////////////////
    file_save_enable: bool
    file_save_setting: dict

    def __init__(self, path: str) -> None:
        self.__config_path = path
        self.load()

    # 函数定义
    # ///////////////////////////////////////////////////////////////

    @deco.config_load
    def load(self) -> None:
        """读取配置文件"""
        json_str: str
        with open(self.__config_path, "r", encoding="UTF-8") as file:
            json_str = file.read()
        config: dict = self.__deserialize(json_str)
        # 配置应用
        self.urls = config["urls"]
        self.request_method = config["request_method"]
        self.encoding = config["encoding"]
        self.timeout = config["timeout"]
        self.verify = config["verify"]
        self.headers = config["headers"]
        self.data_form = config["data_form"]
        self.data_form_script = config["data_form_script"]
        self.cookies = config["cookies"]
        self.user_agent_pool = config["user_agent_pool"]
        self.ip_proxy_pool = config["ip_proxy_pool"]
        self.parser_enable = config["parser_enable"]
        self.data_type = config["data_type"]
        self.pretreatment_enable = config["pretreatment_enable"]
        self.pretreatment_setting = config["pretreatment_setting"]
        self.parser_text_setting = config["parser_text_setting"]
        self.file_save_enable = config["file_save_enable"]
        self.file_save_setting = config["file_save_setting"]

    def save(self) -> None:
        """写入配置到文件"""
        json_str: str = self.__serialize()
        with open(self.__config_path, "w", encoding="UTF-8") as file:
            file.write(json_str)
            file.write(Define.FILE_JSON_BOTTOM_COMMENT["configuration"])

    def path(self) -> str:
        """获取当前配置的文件路径"""
        return self.__config_path

    # TODO: 脚本生成的数据表单添加到数据表单

    def __serialize(self) -> str:
        """序列化配置项

        Returns:
            str: 返回JSON字符串
        """
        config: dict = {}
        config["urls"] = self.urls
        config["request_method"] = self.request_method
        config["encoding"] = self.encoding
        config["timeout"] = self.timeout
        config["verify"] = self.verify
        config["headers"] = self.headers
        config["data_form"] = self.data_form
        config["data_form_script"] = self.data_form_script
        config["cookies"] = self.cookies
        config["user_agent_pool"] = self.user_agent_pool
        config["ip_proxy_pool"] = self.ip_proxy_pool
        config["parser_enable"] = self.parser_enable
        config["data_type"] = self.data_type
        config["pretreatment_enable"] = self.pretreatment_enable
        config["pretreatment_setting"] = self.pretreatment_setting
        config["parser_text_setting"] = self.parser_text_setting
        config["file_save_enable"] = self.file_save_enable
        config["file_save_setting"] = self.file_save_setting
        json_str: str = json.dumps(config, indent=4)
        return json_str

    def __deserialize(self, json_str: str) -> dict:
        """反序列化JSON字符串

        Returns:
            dict: 返回配置字典
        """
        json_str_woc: str = remove_json_comments(json_str)
        config: dict = json.loads(json_str_woc)
        return config
