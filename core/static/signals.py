# 自定义事件类型枚举
# ///////////////////////////////////////////////////////////////
from enum import Enum


class SigType(Enum):
    CLICKED: int = 1
    RELEASED: int = 2
