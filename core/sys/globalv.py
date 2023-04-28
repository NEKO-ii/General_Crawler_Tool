# 全局变量模块
# ///////////////////////////////////////////////////////////////
from .settings import Settings
from .themes import Themes
from enum import Enum

_SETTINGS: Settings = None
_THEMES: Themes = None
_PATH = None

_GLOBAL_DICT: dict = {}


class GlvKey(Enum):
    SETTINGS = "SETTINGS"
    THEMES = "THEMES"
    PATH = "PATH"


class Globalv:
    """全局变量类"""

    @staticmethod
    def init() -> None:
        """初始化全局变量"""
        global _SETTINGS, _THEMES, _PATH
        global _GLOBAL_DICT
        _GLOBAL_DICT = {"SETTINGS": _SETTINGS, "THEMES": _THEMES, "PATH": _PATH}

    @staticmethod
    def get(key: GlvKey):
        """获取全局变量

        Args:
            key (GlvKey): 索引

        Returns:
            _type_: 返回全局变量值
        """
        global _GLOBAL_DICT
        return _GLOBAL_DICT[key.value]

    @staticmethod
    def set(key: GlvKey, value) -> None:
        """设置全局变量值

        Args:
            key (GlvKey): 索引
            value (Any): 设置值
        """
        global _GLOBAL_DICT
        _GLOBAL_DICT[key.value] = value
