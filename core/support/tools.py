# 实用小工具
# ///////////////////////////////////////////////////////////////
from time import strftime, time, localtime


class Tools:

    def __init__(self) -> None:
        pass

    @staticmethod
    def datetime(format: str = "%Y.%m.%d %H:%M:%S") -> str:
        return strftime(format, localtime(time()))
