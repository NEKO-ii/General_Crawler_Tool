# 全局变量模块
# ///////////////////////////////////////////////////////////////
from .settings import Settings
from .themes import Themes
from .accountstate import AccountState
from enum import Enum

_SETTINGS: Settings = None
_THEMES: Themes = None
_PATH = None
_ACCOUNT_STATE: AccountState = None

_GLOBAL_DICT: dict = {}

IS_LOGIN_SUCCEED: bool = False
USER_INFO: dict = {}


class GlvKey(Enum):
    SETTINGS = "SETTINGS"
    THEMES = "THEMES"
    PATH = "PATH"
    ACCOUNT_STATE = "ACCOUNT_STATE"


class Globalv:
    """全局变量类"""

    @staticmethod
    def init() -> None:
        """初始化全局变量"""
        global _SETTINGS, _THEMES, _PATH, _ACCOUNT_STATE
        global _GLOBAL_DICT
        _GLOBAL_DICT = {"SETTINGS": _SETTINGS, "THEMES": _THEMES, "PATH": _PATH, "ACCOUNT_STATE": _ACCOUNT_STATE}

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
