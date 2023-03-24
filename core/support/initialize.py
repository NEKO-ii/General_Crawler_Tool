# 初始化模块,所有初始化函数在此定义
# ///////////////////////////////////////////////////////////////
from os import getcwd
from os.path import abspath, join, normpath

from core.static.define import Define


def init_settings() -> None:
    """初始化设置文件
    """
    settings_file_path = normpath(join(abspath(getcwd()), Define.PATH_SETTINGS, "settings.json"))
    with open(settings_file_path, "w", encoding="UTF-8") as file:
        file.write(Define.FILE_DEFAULT_CONTENT["settings"])
        file.write(Define.FILE_JSON_BOTTOM_COMMENT["settings"])
