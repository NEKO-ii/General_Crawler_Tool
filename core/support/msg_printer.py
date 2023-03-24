# 服务于消息输出的函数定义在这里
#
# 消息等级分为:
#   NONE        ->  普通(默认颜色)
#   INFOMATION  ->  信息(蓝色)
#   SUCCESS     ->  成功(绿色)
#   WARNING     ->  警告(黄色)
#   ERROR       ->  错误(红色)
# ///////////////////////////////////////////////////////////////
from enum import Enum


class MsgType(Enum):
    """消息类型枚举
    """
    NONE: str = "none"
    INFOMATION: str = "info"
    SUCCESS: str = "succ"
    WARNING: str = "warn"
    ERROR: str = "err"


# 消息类型对应输出前缀字典
msg_prefix: dict = {"none": "", "info": "[\033[1;34mInfo\033[0m] ", "succ": "[\033[1;32mSuccess\033[0m] ", "warn": "[\033[1;33mWarning\033[0m] ", "err": "[\033[1;31mError\033[0m] "}


def console_printer(type: MsgType, msg: str) -> None:
    """输出消息到控制台

    Args:
        type (MsgType): 消息类型
        msg (str): 消息内容
    """
    print(F"{msg_prefix[type.value]}{msg}")
